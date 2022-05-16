#include <cstddef>
#include <cassert>
#include <exception>
#include <iostream>
#include <iomanip>
#include <stdexcept>
#include <limits>
#include <vector>

struct Node {
  Node *splayParent, *splayLeft, *splayRight;
  Node *hardParent; // not NULL only if splayParent == NULL
};

bool isLeftSon(const Node* const x) {
  if (x == NULL || x->splayParent == NULL)
    return false;
  return x->splayParent->splayLeft == x;
}

void rotr(Node* const leafing) {
  if (leafing == NULL || leafing->splayLeft == NULL)
    return;
  Node* const rooting = leafing->splayLeft;
  if (leafing->splayParent) {
    if (isLeftSon(leafing))
      leafing->splayParent->splayLeft = rooting;
    else
      leafing->splayParent->splayRight = rooting;
  }
  rooting->splayParent = leafing->splayParent;
  
  leafing->splayLeft = rooting->splayRight;
  if (leafing->splayLeft)
    leafing->splayLeft->splayParent = leafing;
  rooting->splayRight = leafing;
  rooting->splayRight->splayParent = rooting;

  if (leafing->hardParent) {
    rooting->hardParent = leafing->hardParent;
    leafing->hardParent = NULL;
  }
}

void rotl(Node* const leafing) {
  if (leafing == NULL || leafing->splayRight == NULL)
    return;
  Node* const rooting = leafing->splayRight;
  if (leafing->splayParent) {
    if (isLeftSon(leafing))
      leafing->splayParent->splayLeft = rooting;
    else
      leafing->splayParent->splayRight = rooting;
  }
  rooting->splayParent = leafing->splayParent;
  
  leafing->splayRight = rooting->splayLeft;
  if (leafing->splayRight)
    leafing->splayRight->splayParent = leafing;
  rooting->splayLeft = leafing;
  rooting->splayLeft->splayParent = rooting;

  if (leafing->hardParent) {
    rooting->hardParent = leafing->hardParent;
    leafing->hardParent = NULL;
  }
}

void splay(Node* const x) {
  if (x == NULL | x->splayParent == NULL)
    return;

  if (x->splayParent->splayParent == NULL) {
    if (isLeftSon(x))
      return rotr(x->splayParent);
    else
      return rotl(x->splayParent);
  }
  
  if (isLeftSon(x)) {
    if (isLeftSon(x->splayParent)) { // zigzig
      rotr(x->splayParent->splayParent);
      rotr(x->splayParent);
    }
    else { // zigzag
      rotr(x->splayParent);
      rotl(x->splayParent);
    }
  }
  else {
    if (isLeftSon(x->splayParent)) { //zagzig
      rotl(x->splayParent);
      rotr(x->splayParent);
    }
    else { // zagzag
      rotl(x->splayParent->splayParent);
      rotl(x->splayParent);
    }
  }

  return splay(x);
}

void access(Node* const x) {
  splay(x);
  if (x->splayRight) {
    x->splayRight->splayParent = NULL;
    x->splayRight->hardParent = x;
    x->splayRight = NULL;
  }
  if (x->hardParent) {
    access(x->hardParent);
    assert(x->hardParent->splayRight == NULL);
    x->hardParent->splayRight = x;
    x->splayParent = x->hardParent;
    x->hardParent = NULL;
    
    rotl(x->splayParent);
  }
}

void link(Node* const tree, Node* const branch) {
  access(tree); // on pourrait splay() à la place
  access(branch);
  
  if (tree == branch || tree->splayLeft != NULL || tree->splayParent != NULL || tree->hardParent != NULL)
    throw std::invalid_argument("Invalid link parameters (same tree, or non-root for [tree])");

  tree->splayLeft = branch;
  branch->splayParent = tree;
}

void cut(Node* const node) {
  access(node);
  if (node->splayLeft == NULL)
    throw std::invalid_argument("Invalid cut parameter (root vertex)");
  node->splayLeft->splayParent = NULL;
  node->splayLeft = NULL;
}

Node* getRoot(Node* node) {
  access(node);
  while (node->splayLeft)
    node = node->splayLeft;
  access(node);
  return node;
}

using namespace std;

vector<Node> makeVoidTree(int n) {
  return vector<Node>(n, Node({NULL,NULL,NULL,NULL}));
}

struct DummyNode {
  DummyNode* parent;
};

DummyNode* dummyroot(DummyNode* const c) {
  if (c->parent)
    return dummyroot(c->parent);
  return c;
}

void dummylink(DummyNode* const tree, DummyNode* const branch) {
  if (tree->parent != NULL || dummyroot(branch) == tree)
    throw std::invalid_argument("Dummy link invalid");
  tree->parent = branch;
}

void dummycut(DummyNode* const node) {
  if (node->parent == NULL)
    throw std::invalid_argument("Dummy cut invalid");
  node->parent = NULL;
}

int indexFromPointer(const vector<Node>& vec, const Node* const node) {
  if (node == NULL)
    return -1;
  return (node - &vec[0]);
};

// Depth-first search in the tree
// Displays the tree (favorite son last)
// Output is the real-depth of the rightmost node in the sub-splaytree
int doDisplay(const vector<Node>& vec, const vector<vector<int>>& sons, int pos, int depth, bool isFav) {
  if (vec[pos].splayLeft)
    depth = doDisplay(vec, sons, indexFromPointer(vec,vec[pos].splayLeft), depth, isFav)+1;
  std::cout << "[" << depth << "]" << std::setw(2 * depth + 1) << pos;
  if (vec[pos].splayLeft || isFav)
    std::cout << " Fav";
  if (vec[pos].splayParent == NULL)
    std::cout << " *";
  std::cout << std::endl;
  for (auto son : sons[pos])
    doDisplay(vec, sons, son, depth+1, false);
  if (vec[pos].splayRight)
    return doDisplay(vec, sons, indexFromPointer(vec, vec[pos].splayRight), depth+1, true);
  else
    return depth;
}

void display(const vector<Node>& vec) {
  vector<vector<int>> sons(vec.size());
  vector<const Node*> roots;

  /* For debugging
  cout << "brute data :" << endl;
  for (int i = 0; i < vec.size(); ++i) {
    cout << indexFromPointer(vec, vec[i].hardParent) << " "
         << indexFromPointer(vec, vec[i].splayParent) << " "
         << indexFromPointer(vec, vec[i].splayLeft) << " "
         << indexFromPointer(vec, vec[i].splayRight) << endl;
  }
  // */

  for (int i = 0; i < vec.size(); ++i) {
    if (vec[i].hardParent)
      sons[indexFromPointer(vec, vec[i].hardParent)].push_back(i);
    if (vec[i].hardParent == NULL && vec[i].splayParent == NULL)
      roots.push_back(&vec[i]);
  }

  for (auto r : roots) {
    cout << "_________" << endl;
    doDisplay(vec,sons,indexFromPointer(vec, r), 0, false);
  }
}

void readLink(vector<Node>& vec) {
  size_t branch, tree;
  if (cin >> branch >> tree) {
    if (tree >= vec.size() || branch >= vec.size())
      throw std::out_of_range("index above size");
    link(&vec[tree], &vec[branch]);
  }
  else
    throw invalid_argument("expected : L [branch start id] [tree root id]");
}

void readCut(vector<Node>& vec) {
  size_t node;
  if (cin >> node) {
    if (node >= vec.size())
      throw std::out_of_range("index above size");
    cut(&vec[node]);
  }
  else
    throw invalid_argument("expected : C [non-root id]");
}

void readRoot(vector<Node>& vec) {
  size_t node;
  if (cin >> node) {
    if (node >= vec.size())
      throw std::out_of_range("index above size");
    cout << "Root of " << node << " is " << indexFromPointer(vec, getRoot(&vec[node])) << endl;
  }
  else
    throw invalid_argument("expected : R [node id]");
}

void readAct(vector<Node>& vec) {
  while (true) {
    try {
      string str;
      if (!(cin >> str))
        assert(("Invalid read", false));
      if (str == "C")
        return readCut(vec);
      else if (str == "L")
        return readLink(vec);
      else if (str == "R")
        return readRoot(vec);
      else if (str == "D")
        return display(vec);
      else if (str == "Q")
        abort();
      else
        throw invalid_argument("expected command in {L,C,R,D,Q}");
    }
    catch (exception& e) {
      cerr << "ERROR : " << e.what() << endl;
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
  }
}

void autoRunDummyOnly(vector<Node>& empty, size_t nbRun, size_t probaCut) {
  const size_t n = empty.size();
  vector<DummyNode> stupid(n);
  srand(42);
  for (int i = 0; i < nbRun; ++i) {
    size_t param = rand()% n, param2;
    try {
      switch (rand() % probaCut) {
        case 0:
          dummycut(&stupid[param]);
          break;
        case 1:
          dummyroot(&stupid[param]);
          break;
        default:
          param2 = rand() % n;
          size_t theRoot = dummyroot(&stupid[param2])-&stupid[0];
          dummylink(&stupid[theRoot], &stupid[param]);
      }
    }
    catch(...) { continue; }
  }
}

void autoRunDummyCheck(vector<Node>& emptyVec, size_t nbRun, size_t probaCut) {
  const size_t n = emptyVec.size();
  vector<DummyNode> stupid(n);
  srand(42);
  for (int i = 0; i < nbRun; ++i) {
    size_t param = rand()% n, param2;
    switch (rand() % probaCut) {
      case 0:
        try {
          dummycut(&stupid[param]);
        }
        catch(...) { continue; }
        cut(&emptyVec[param]);
        break;
      case 1:
        getRoot(&emptyVec[param]);
        break;
      default:
        param2 = rand() % n;
        size_t theRoot = dummyroot(&stupid[param2])-&stupid[0];
        try {
          dummylink(&stupid[theRoot], &stupid[param]);
        }
        catch(...) {continue;}
        link(&emptyVec[theRoot], &emptyVec[param]);
    }
  }
}

void autoRun(vector<Node>& emptyVec, size_t nbRun, size_t probaCut) {
  const size_t n = emptyVec.size();
  srand(42);
  for (int i = 0; i < nbRun; ++i) {
    size_t param = rand()% n, param2;
    try {
      switch (rand() % probaCut) {
        case 0:
          cut(&emptyVec[param]);
          break;
        case 1:
          getRoot(&emptyVec[param]);
          break;
        default:
          param2 = rand() % n;
          size_t theRoot = indexFromPointer(emptyVec,getRoot(&emptyVec[param2]));
          link(&emptyVec[theRoot], &emptyVec[param]);
      }
    }
    catch(...) { continue; }
  }
}

int main() {
  size_t n, m;
  cout << "Number of elements : ";
  if (!(cin >> n))
    return 1;
  cout << "Number of inits : ";
  if (!(cin >> m))
    return 1;

  auto vec = makeVoidTree(n);

  autoRun(vec, m, 5);

  while (true) {
    readAct(vec);
  }

  return 0;
}




#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct Message Message;

/** classe Message
 *  virt_valeur() prend un Message et renvoie une chaîne de caractères (allouée, à détruire)
 *  afficherLog() affiche la valeur du message, avec le temps depuis la création
 */
struct Message {
  void (*virt_destruct)(Message* this);
  const char* (*virt_valeur)(Message* this);
  int dateCreation;
};
const char* valeurDefaut(Message* this) {
  return strdup("defaut");
}
void destructMessage(Message* this) {
  printf("détruit message base\n");
} // Rien de particulier à faire
void constructMessage(Message* this) {
  // Initialise la table virtuelle
  this->virt_valeur = valeurDefaut;
  this->virt_destruct = destructMessage;
  // Initialise les attributs
  this->dateCreation = time(NULL);

  printf("construit message base\n");
}

void afficherLog(Message* this) {
  // appelle la fonction virtuelle
  const char* texte = (this->virt_valeur)(this);
  printf("  [créé il y a %lus] %s\n", time(NULL) - this->dateCreation, texte);
  free((void*)texte);
}

typedef struct MessageTexte MessageTexte;
struct MessageTexte {
  // Les premières données sont celles de la classe parente
  Message super;
  char* texte;
};
const char* valeurTexte(MessageTexte* this) {
  printf("appel valeur texte\n");
  return strdup(this->texte);
}
void destructMessageTexte(MessageTexte* this) {
  free(this->texte);
  printf("détruit message texte\n");
  destructMessage((Message*) this);
}

void constructMessageTexte(MessageTexte* this, const char* texteParam) {
  // Initialise la classe parente
  constructMessage((Message*)this);
  // Enregistre l'implémentation de la fonction virtuelle
  ((Message*)this)->virt_valeur = valeurTexte;
  ((Message*)this)->virt_destruct = destructMessageTexte;
  
  // Initialise l'attribut
  this->texte = strdup(texteParam);
  printf("construit message texte\n");
}

typedef struct MessageErreur MessageErreur;
struct MessageErreur {
  MessageTexte super;
};
void destructMessageErreur(MessageErreur* this) {
  printf("détruit message erreur\n");

  destructMessageTexte((MessageTexte*) this);
}
void constructMessageErreur(MessageErreur* this) {
  constructMessageTexte((MessageTexte*)this, "ERREUR STANDARD");

  ((Message*)this)->virt_destruct = destructMessageErreur;

  printf("construit message erreur\n");
};

typedef struct MessageNombre MessageNombre;
struct MessageNombre { 
  Message super;
  float nombre;
};
const char* valeurNombre(MessageNombre* this) {
  printf("appel valeur nombre\n");
  char* texte = (char*) malloc(sizeof(char)*42);
  sprintf(texte, "nombre : %f", this->nombre);
  return texte;
}
void destructMessageNombre(MessageNombre* this) {
  printf("détruit message nombre\n");

  destructMessage((Message*) this);
}
void constructMessageNombre(MessageNombre* this, float valeur) {
  constructMessage((Message*)this);
  // Enregistre l'implémentation de la fonction virtuelle
  ((Message*)this)->virt_valeur = valeurNombre;
  ((Message*)this)->virt_destruct = destructMessageNombre;
  // Initialise l'attribut
  this->nombre = valeur;

  printf("construit message nombre\n");
}

void destruct(Message* this) {
  this->virt_destruct(this);
}



int main() {
  MessageTexte mt;
  constructMessageTexte(&mt, "essai message");
  sleep(1);
  MessageErreur me;
  constructMessageErreur(&me);
  sleep(1);
  MessageNombre mn;
  constructMessageNombre(&mn, 42.);

  Message* listeObjets[3] = {&mt, &me, &mn};

  for (int k = 0; k < 3; ++k) {
    printf("  Longueur de la valeur : %lu\n", strlen(listeObjets[k]->virt_valeur(listeObjets[k]))); // fuite mémoire mais chuuuuut
    afficherLog(listeObjets[k]);
    destruct(listeObjets[k]);
  }
}


type arbre = Noeud of float (*priority*) * arbre * int (*order*) * arbre | Feuille

let rec union (gauche : arbre) (droite : arbre) : arbre = match gauche, droite with
  | Feuille, a | a, Feuille -> a
  | Noeud(prem, gprem, oprem, dprem), Noeud(sec, _, _, _) when prem < sec -> Noeud(prem, gprem, oprem, (union dprem droite))
  | _, Noeud(prem,gprem, oprem, dprem) -> Noeud(prem, (union gauche gprem), oprem, dprem)

let rec split (a : arbre) (pivot : int) : arbre*arbre = match a with
  | Feuille -> Feuille,Feuille
  | Noeud(prio, g, order, d) when order < pivot -> let dessous, dessus = split d pivot in (Noeud(prio, g, order, dessous), dessus)
  | Noeud(prio, g, order, d) -> let dessous, dessus = split g pivot in (dessous, Noeud(prio, dessus, order, d))

let makeSingle ?(prio : float = Random.float 1.) (order : int) : arbre = Noeud(prio, Feuille, order, Feuille)

let rec insert ?(prio : float = Random.float 1.) (a:arbre) (order : int) : arbre = match a with
  | Feuille -> makeSingle ~prio order
  | Noeud(pnoeud, _,_,_) when prio < pnoeud -> let dessus, dessous = split a order in Noeud(prio, dessus, order, dessous)
  | Noeud(pnoeud, g, onoeud, d) when onoeud < order -> Noeud(pnoeud, g, onoeud, insert d ~prio order)
  | Noeud(pnoeud, g, onoeud, d) -> Noeud(pnoeud, insert g ~prio order, onoeud, d)

exception NotFound

let rec find (a:arbre) (order : int) : (float*int) = match a with
  | Feuille -> raise NotFound
  | Noeud(prio, _, on, _) when order = on -> (prio, on)
  | Noeud(_,g, on,_) when order < on -> find g order
  | Noeud(_,_,_,d) -> find d order

let rec remove (a:arbre) (order : int) : arbre = match a with
  | Feuille -> Feuille (* or raise NotFound, maybe ? *)
  | Noeud(prio, g, on, d) when order = on -> union g d
  | Noeud(prio, g, on, d) when order < on -> Noeud(prio, remove g order, on, d)
  | Noeud(prio, g, on, d) -> Noeud(prio, g, on, remove d order)

  

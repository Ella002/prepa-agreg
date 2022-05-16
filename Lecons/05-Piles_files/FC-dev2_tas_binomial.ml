type 'a arbre =
  {valeur : 'a;
   cle : int;
   ordre : int;
   descendants : 'a arbre list}

type 'a tas = 'a arbre list

let creer_tas () : 'a tas = []

let est_vide (t : 'a tas) : bool =
  t == []


let fusion_arbre (a1 : 'a arbre)  (a2 : 'a arbre) : 'a arbre =
  (* on ajoute l'un des arbres dans les descendants de l'autre,
  de manière à ce que la racine soit toujours plus petite que
  ses descendants *)
  if a1.cle < a2.cle then
    {a1 with descendants = a2::(a1.descendants);
    ordre = a1.ordre + 1}
  else
    {a2 with descendants = a1::(a2.descendants);
    ordre = a2.ordre + 1}


let fusion_tas (t1 : 'a tas) (t2 : 'a tas) : 'a tas =
  (* on parcourt les deux tas, dès qu'il y a deux arbres de même ordre, on les fusionne *)

  (* il faut aussi gérer les cas où l'on aurait un arbre de même ordre qu'un nouvellement généré, comme on parcourt les arbres
  par ordre croissant, il ne peut s'agir que du dernier, auquel
     cas on les fusionne aussi *)
  let fusion_resultat (a : 'a arbre) (resultat : 'a tas) : 'a tas =
    match resultat with
    | [] -> [a]
    | a_r::q ->
      if a.ordre == a_r.ordre then
        (fusion_arbre a a_r)::q
      else
        a::resultat
  in

       let rec aux_fusion (t1 : 'a tas) (t2 : 'a tas) (accu : 'a tas) : 'a tas =
    match (t1, t2) with
    | ([], []) -> accu
    | ([], a::q) | (a::q, []) ->
      let nouv_accu = fusion_resultat a accu in
      aux_fusion [] q nouv_accu
    | (a1::q1, a2::q2) ->
      if a1.ordre < a2.ordre then
        let nouv_accu = fusion_resultat a1 accu in
        aux_fusion q1 t2 nouv_accu
      else if a1.ordre == a2.ordre then
        aux_fusion q1 q2 ((fusion_arbre a1 a2)::accu)
      else
        let nouv_accu = fusion_resultat a2 accu in
        aux_fusion t1 q2 nouv_accu
  in

  List.rev (aux_fusion t1 t2 [])

let ajout (t : 'a tas) (c : int) (v : 'a) : 'a tas =
    (* on veut ajouter l'élément v de clé c au tas t *)
    let element = {valeur = v;
                   cle = c;
                   ordre = 0;
                   descendants = []
                  } in

    fusion_tas t [element]

let min_tas (t : 'a tas) : int * 'a =
  (* renvoie la valeur de l'élément du tas ayant la plus petite clé*)

  (* il suffit de parcourir les racines des arbres composant le tas *)
  let rec aux_min (t : 'a tas) (c : int) (v : 'a) : int * 'a =
    match t with
    | [] -> c, v
    | a::q ->
      if a.cle < c then
        aux_min q a.cle a.valeur
      else aux_min q c v
  in
  aux_min (List.tl t) (List.hd t).cle (List.hd t).valeur

let extraire_min (t : 'a tas) : 'a tas * 'a =
  (* on veut renvoyer le tas sans son élément minimal *)

  (* pour cela on fait une première passe pour
     identifier le minimum*)
  let cle_min, v = min_tas t in

  (* puis on retire l'arbre correspondant du tas *)
  let rec retire_arbre_min (t : 'a tas) : 'a tas * 'a arbre =
    match t with
    | [] -> raise (Failure "minimum non trouvé")
    | a::q ->
      if a.cle == cle_min then
        q, a
      else
        let (t', a') = retire_arbre_min q in
        a::t', a'
  in

  let nouv_t, arbre_min = retire_arbre_min t in

  (* enfin, on fusionne le tas obtenu avec le tas formé de
  arbre_min sans sa racine
     (la liste de ses descendants est un tas binomial)*)

  fusion_tas nouv_t (List.rev arbre_min.descendants), v


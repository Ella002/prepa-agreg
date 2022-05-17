open Array;;
open List;;

type dfa  = { nb_etats : int ;
              alphabet : int ;
              delta : int array array ;
              init : int ;
              accept : int list }


let d = Array.make_matrix 4 2 0 ;;
d.(1).(0) <- 2;;
d.(1).(1) <- 3;;
d.(2).(1) <- 3;;
d.(3).(0) <- 2;;

let aut_1 = {nb_etats = 3;
           alphabet = 2;
           delta = d;
           init = 1;
           accept = [2;3];};;

let d_2 = Array.make_matrix 7 2 0;;
d_2.(1).(0) <- 6 ;;
d_2.(6).(0) <- 2 ;;
d_2.(6).(1) <- 3 ;;
d_2.(2).(0) <- 6 ;;
d_2.(2).(1) <- 4 ;;
d_2.(3).(0) <- 5 ;;
d_2.(3).(1) <- 3 ;;
d_2.(4).(0) <- 5 ;;
d_2.(4).(1) <- 3 ;;

let aut_2 = {nb_etats = 6;
             alphabet = 2;
             delta = d_2;
             init = 1;
             accept = [5];
            };;


let run a m =
  let rec aux s m = match m with
    | [] -> s
    | t :: q -> aux a.delta.(s).(t) q
      in List.mem (aux a.init m) a.accept ;;

assert(run aut_1 [0 ; 1 ; 0 ; 1 ; 0 ; 1]);;

let is_partition p n =
(* teste si p est une partition de l'ensemble [|0,n|]*)

  if List.mem [] p
  then false
  else

  let l = List.flatten p in

  if List.for_all (fun k -> (k>=0 && k<=n)) l
   (* teste si les éléments de p sont dans [|0,n|]*)

  then
    let check = Array.make (n+1) 0 in

    List.iter ( fun t -> check.(t) <- check.(t)+1 ) (l);
    (* Pour chaque état i, compte dans check.(i) le nombre d'occurence de i dans l*)

    Array.for_all (fun k -> (k=1)) check
  else
    false ;;
    (*vérifie que toutes les case de check contiennent 1*)

assert (is_partition [[0;1];[2];[3]] 3);;

let accept_part aut =
(*créer la partition initiale séparant les états finaux des autres *)
  let states = List.init (aut.nb_etats+1) (fun k -> k) in
  let (l1,l2) = List.partition (fun k -> List.mem k aut.accept) states in
  if (l1 = []) then [l2] else
    if (l2 = []) then [l1] else
      [l1;l2];;

(accept_part aut_2) ;;

let rec eq q1 q2 p = match p with
(* teste si deux états sont dans la même classe d'équivalence dans la partition p*)
  | [] -> false
  | eqc :: p' -> if (List.mem q1 eqc) && (List.mem q2 eqc)
                 then true
                 else eq q1 q2 p';;

assert (eq 2 3 [[0;1];[2;3]]);;


let differentiate q1 q2 p aut =
  (*teste si q1 et q2 sont differentiables dans l'automate aut vis à vis de la partition p *)
  assert (is_partition p aut.nb_etats);
  let rec aux c =
    if c = aut.alphabet
    then false

    else if eq aut.delta.(q1).(c) aut.delta.(q2).(c) p

    then aux (c+1)
    else true
  in aux 0;;

assert(differentiate 2 3 [[1];[2;3];[0]] aut_1);;

let split eqc p aut =
(* sépare l'ensemble eqc (non vide) en deux ensembles: l2 la liste des éléments indifferentiables du premier élément de eqc et l2 le reste*)
  assert(eqc != []);
  assert (is_partition p aut.nb_etats);
  let t = List.hd eqc in
  List.partition (fun s -> differentiate t s p aut) eqc;;

split [2;3;0] [[1];[3;0]; [2]] aut_1;;

let update p aut =
(*met à jour la partition p en séparant les etats differentiables dans l'automate aut vis à vis de la partition p et renvoie la nouvelle partition et un booléen si la partition a changée *)
  assert(is_partition p aut.nb_etats);
  let rec aux acc eqs up = match eqs with
    | [] -> (acc,up)
    | eq::q -> let (l1, l2) = split eq p aut in
              if (l1 = [])
              then aux (l2::acc) q up
              else aux (l2::acc) (l1::q) true
  in aux [] p false;;

update (accept_part aut_2) aut_2;;

let (p, _) = update (accept_part aut_2) aut_2 in update p aut_2;;

let nerode_eq_moore aut =
(* calcul les classes d'équivalence de Nérode, i.e. la partition donnant les états de l'automate minimal *)
  let p_i = accept_part aut in
  let rec aux p aut up =
    if up
    then let (p',up') = update p aut in
         aux p' aut up'
    else p
  in aux p_i aut true;;

nerode_eq_moore aut_2;;

let rec remove_well_state p = match p with
(*Enleve la classe d'équivalence de l'état puits de la partition p*)
  | [] -> []
  | t::q when (List.mem 0 t) -> q
  | t::q -> t::(remove_well_state q);;

remove_well_state (nerode_eq_moore aut_2);;

let well_state p =
(* calcule la classe de l'état puits dans la partition p *)
  List.find (fun t -> List.mem 0 t) p;;

well_state (nerode_eq_moore aut_2);;

let equivalence_class_index s p =
(* renvoie l'index de la classe d'équivalence contenant s dans p *)
  let rec aux i p = match p with
  | [] -> raise Not_found
  | t::q when (List.mem s t) -> i
  | t::q -> aux (i+1) q
  in aux 0 p;;

equivalence_class_index 3 (nerode_eq_moore aut_2);;

let aut_min aut =
(*construit l'automate minimal reconnaissant le langage de aut à partir de la partition de Nérode calculée par l'algorithme de Moore*)

  let p = nerode_eq_moore aut in
  assert (is_partition p aut.nb_etats);

  let well = well_state p in
  let p' = remove_well_state p in
  let gp = (well::p') in
  assert (is_partition gp aut.nb_etats);

  let nb_etats_min = List.length p' in

  let delta_min = Array.make_matrix (nb_etats_min+1) (aut.alphabet) 0 in

  let rec aux accept_min i eqs = match eqs with
    (* mets à jour la table de transitions et collecte les classes d'états finaux*)
      | [] -> accept_min
      |t::q -> let s = List.hd t in

               for j = 0 to (aut.alphabet-1) do
                 delta_min.(i).(j) <- equivalence_class_index aut.delta.(s).(j) gp
               done;

               if (List.mem s aut.accept)
               then aux (i::accept_min) (i+1) q
               else aux accept_min (i+1) q
  in
  let accept_min = aux [] 0 gp in

  let init_min = equivalence_class_index aut.init p in
  let aut_min = {nb_etats = nb_etats_min;
                 alphabet = aut.alphabet;
                 delta = delta_min;
                 init = init_min;
                 accept = accept_min;} in
  aut_min;;

aut_min aut_2;;

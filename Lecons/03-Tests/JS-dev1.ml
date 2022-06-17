open Format

(* Langage *)
type terme =
    | Var  of string
    | App  of { fn: terme; arg: terme }
    | Abs  of { var: string; corps: terme }
    | Int  of int
    | Plus of terme * terme


(* Types *)
type typ =
    | Var    of string
    | Fleche of fleche
    | Nat
and fleche = { dep: typ; arv: typ }

(* Environnement *)
type env = (string * typ) list

(* Équations de type *)
type equas = (typ * typ) list
type equas_zip = { avant: equas; apres: equas }




(* Affichage *)

let rec affiche_terme fmt = function
    | Abs { var; corps } -> fprintf fmt "λ %s.@[@ %a@]" var affiche_terme corps
    | e -> affiche_expr fmt e
and affiche_expr fmt = function
    | Plus (e1, e2) -> fprintf fmt "%a@ + %a" affiche_expr e1 affiche_expr e2
    | c -> affiche_compo fmt c
and affiche_compo fmt = function
    | App { fn; arg } -> fprintf fmt "%a %a" affiche_compo fn affiche_facteur arg
    | f -> affiche_facteur fmt f
and affiche_facteur fmt = function
    | Var v -> fprintf fmt "%s" v
    | Int n -> fprintf fmt "%d" n
    | t -> fprintf fmt "@[(%a@])" affiche_terme t


let rec affiche_typ fmt = function
    | Fleche { dep; arv } -> fprintf fmt "%a → %a" affiche_dep_typ dep affiche_typ arv
    | dt -> affiche_dep_typ fmt dt
and affiche_dep_typ fmt = function
    | Var v -> fprintf fmt "%s" v
    | Nat   -> fprintf fmt "ℕ"
    | t -> fprintf fmt "@[(%a@])" affiche_typ t


(* Constructeurs intelligents *)

let var v: terme = Var v
let entier n = Int n
let app u v = App { fn = u; arg = v }
let abs x u = Abs { var = x; corps = u }
let plus a b = Plus (a, b)



(* Générateur de nom frais de variables de types *)
let nouvelle_variable: unit -> string =
    let compteur = ref 0 in
    function () ->
        compteur := !compteur + 1;
        "τ" ^ (Int.to_string !compteur)


(* PHASE 1 : GÉNÉRATION D'ÉQUATIONS *)

let rec cherche_type (var: string) (e: env): typ =
    match e with
    | [] -> raise Not_found
    | (v, t) :: _ when v = var -> t
    | _ :: q -> cherche_type var q


let rec genere_equas (t: terme) (tau: typ) (e: env): equas =
    match t with
    | Int _ -> (tau, Nat) :: []
    | Var v -> (tau, cherche_type v e) :: []
    | App { fn; arg } ->
            let var = Var (nouvelle_variable ()) in
            let eq1 = genere_equas fn (Fleche { dep = var; arv = tau }) e in
            let eq2 = genere_equas arg var e in
            eq1 @ eq2
    | Abs { var; corps } ->
            let vartyp1 = Var (nouvelle_variable ()) in
            let vartyp2 = Var (nouvelle_variable ()) in
            (tau, Fleche { dep = vartyp1; arv = vartyp2 })
            :: (genere_equas corps vartyp2 ((var, vartyp1) :: e))
    | Plus (t1, t2) ->
            let eq1 = genere_equas t1 Nat e in
            let eq2 = genere_equas t2 Nat e in
            (tau, Nat) :: (eq1 @ eq2)


(* PHASE 2 : RÉSOLUTION DES ÉQUATIONS *)

exception Echec_unification of string


(* Remplace var par tau dans t *)
let rec substitue_type (var: string) (tau: typ) (t: typ): typ =
    match t with
    | Fleche f ->
            Fleche { dep = substitue_type var tau f.dep;
                     arv = substitue_type var tau f.arv }
    | Var v when v = var -> tau
    | _ -> t


let substitue_type_equas (var: string) (tau: typ) (e: equas): equas =
    let subs = substitue_type var tau in
    List.map (fun (x, y) -> (subs x, subs y)) e


let substitue_type_zip (var: string) (tau: typ) (e: equas_zip): equas_zip =
    let subs = substitue_type_equas var tau in
    { avant = subs e.avant; apres = subs e.apres }


(* Indique si v apparaît dans t *)
let appartient_type (var: string) (t: typ): bool =
    let rec aux (t: typ): bool =
        match t with
        | Fleche f -> aux f.dep || aux f.arv
        | Var v -> v = var
        | Nat -> false
    in
    aux t


let unification (but: string) (e: equas_zip): typ =
    let rec unif: equas_zip -> typ = function
      (* Plus d'équations a traiter : fini *)
    | e when e.apres = [] ->
            let rec cherche_but: equas -> typ = function
                | [] -> raise (Echec_unification "but non trouvé")
                | (Var v, t) :: _ when v = but -> t
                | (t, Var v) :: _ when v = but -> t
                | _ :: q -> cherche_but q
            in
            cherche_but e.avant

      (* L'équation contient le but : on passe *)
    | { avant; apres = (Var v, t) :: apres } when v = but ->
            unif { avant = (Var v, t) :: avant; apres }

      (* Deux variables : fusion *)
    | { avant; apres = (Var v1, Var v2) :: apres } ->
            unif (substitue_type_zip v2 (Var v1) { avant; apres })

      (* Variable = type : vérification de cycle puis remplacement *)
    | { avant; apres = (Var v, t) :: apres }
    | { avant; apres = (t, Var v) :: apres } ->
            if appartient_type v t then
                begin
                    fprintf str_formatter
                        "La variable de type %s apparaît dans le type %a"
                        v affiche_typ t;
                    raise (Echec_unification (flush_str_formatter ()))
                end
            else
                unif (substitue_type_zip v t { avant; apres })

      (* Fleche = Fleche : on décompose *)
    | { avant; apres = (Fleche f1, Fleche f2) :: apres } ->
            unif { avant; apres = (f1.dep, f2.dep) :: (f1.arv, f2.arv) :: apres }

      (* Fleche = non Fleche : erreur *)
    | { avant; apres = (Fleche f, t) :: _ } | { avant; apres = (t, Fleche f) :: _ } ->
            fprintf str_formatter
                "Le type %a est incompatible avec le type %a"
                affiche_typ t affiche_typ (Fleche f);
            raise (Echec_unification (flush_str_formatter ()))

      (* Nat = Nat : ok *)
    | { avant; apres = (Nat, Nat) :: apres } ->
            unif { avant; apres }

      (* Nat = non Nat : erreur *)
    | { avant; apres = (Nat, t) :: _ } | { avant; apres = (t, Nat) :: _ } ->
            fprintf str_formatter
                "Le type %a est incompatible avec le type %a"
                affiche_typ t affiche_typ Nat;
            raise (Echec_unification (flush_str_formatter ()))
    in
    unif e


(* MAIN *)

let inference (t: terme): string =
    let but = "τ" in
    let e: equas_zip = { avant = []; apres = genere_equas t (Var but) [] } in
    begin try
        let res = unification but e in
        fprintf str_formatter "%a@\nTYPABLE@\n%a" affiche_terme t
            affiche_typ res
    with
    | Echec_unification msg ->
            fprintf str_formatter "%a@\nNON TYPABLE@\n%s" affiche_terme t msg
    end;
    flush_str_formatter ()



(* EXEMPLES *)

let x = "x"
let y = "y"
let z = "z"

let exemples = [
    abs x (var x);
    abs x (abs y (var x));
    abs x (abs y (abs z (app (app (var x) (var z)) (app (var y) (var z)))));
    app (abs x (plus (var x) (entier 1))) (entier 3);
    abs x (plus (var x) (var x));
    (let delta x = abs x (app (var x) (var x)) in app (delta x) (delta y));
    app (abs x (plus (var x) (var x))) (abs x (var x));
]

let () =
    List.iter (fun t ->
        print_endline "============";
        print_endline (inference t)
    ) exemples

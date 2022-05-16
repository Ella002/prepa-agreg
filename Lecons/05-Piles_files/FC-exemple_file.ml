open Tas_bino

let input = [("Bonjour", 1); ("exemple", 5); ("ceci", 2); ("un", 4); ("est", 3)]

let rec enfile (l : (string*int) list) : string tas =
  match l with
  | [] -> creer_tas ()
  | (v, c)::q -> ajout (enfile q) c v

let rec defile (t : string tas) : string =
  match est_vide t with
  | true -> "\n"
  | false ->
    let t', v = extraire_min t in
    v^" "^(defile t')

let print_input (l : (string*int) list) : unit =
  print_string (defile (enfile l))

let () = print_input input;;


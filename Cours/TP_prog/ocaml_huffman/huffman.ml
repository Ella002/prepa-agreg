type tree = Leaf of char | Node of tree * tree
type text = string
type data = string
type alphabet = (char, int) Hashtbl.t
type decoding_dictionary = tree
type encoding_dictionary = (char, data) Hashtbl.t

module type Q_type = sig
    type 'a queue
    val empty : 'a queue
    val is_empty : 'a queue -> bool
    val insert : int * 'a -> 'a queue -> 'a queue
    val extract : 'a queue -> (int * 'a) * 'a queue
    val iter : ((int * 'a) -> unit) -> 'a queue -> unit
end

module Q : Q_type = struct
    type 'a queue = (int * 'a) list
    let empty = []
    let is_empty q = match q with | [] -> true | _ -> false
    let insert (prio, x) q =
        let rec ins_aux acc q =
            match q with
            | [] -> List.rev ((prio, x)::acc)
            | (prio',x')::tl ->
                if prio' > prio then
                    (List.rev acc) @ ((prio, x)::q)
                else
                    ins_aux ((prio', x')::acc) tl
        in
        ins_aux [] q

    let extract q =
        if is_empty q then failwith "Extracting from an empty list" ;
        List.hd q, List.tl q
        
    let iter f q =
        List.iter f q
end

let pp_q_char (fmt : Format.formatter) (q : 'a Q.queue) : unit =
    Format.fprintf fmt "@[<hv>[ " ;
    Q.iter (fun (prio, x) -> Format.fprintf fmt "(%i, %c) " prio x) q ;
    Format.fprintf fmt "]@]"

let build_alphabet (t : text) : alphabet =
    let h = Hashtbl.create 256 in
    let add c =
        try 
            let v = Hashtbl.find h c in
            Hashtbl.replace h c (v+1)
        with Not_found ->
            Hashtbl.add h c 1
    in
    String.iter add t ; h
    
let pp_alphabet (fmt : Format.formatter) (a : alphabet) : unit =
    Format.fprintf fmt "{ @[<hv>" ;
    Hashtbl.iter
        (fun c v -> Format.fprintf fmt "%c -> %i, @;" c v)
        a ;
    Format.fprintf fmt "@]}"
    
let build_tree (a : alphabet) : tree =
    let prio_queue =
        Hashtbl.fold (fun c freq q -> Q.insert (freq, Leaf c) q) a Q.empty
    in
    let rec aux p_q =
        if Q.is_empty p_q then failwith "What are we doing? The queue is empty" ;
        let (freq0, tree0), tl = Q.extract p_q in
        if Q.is_empty tl then tree0
        else
            let (freq1, tree1), tl' = Q.extract tl in
            aux (Q.insert (freq0+freq1, Node (tree0, tree1)) tl')
    in
    aux prio_queue

let pp_tree (fmt: Format.formatter) (t : tree) : unit =
    let rec aux t =
        match t with
        | Leaf c -> Format.fprintf fmt "%c" c
        | Node (t1, t2) -> Format.fprintf fmt "/ |@." ; aux t1 ; aux t2
    in
    aux t

let build_encoding_dictionary (t : tree) : encoding_dictionary =
    let res = Hashtbl.create 256 in
    let rec aux t pref =
        match t with
        | Leaf c -> Hashtbl.add res c pref
        | Node (t0, t1) -> aux t0 (pref^"0") ; aux t1 (pref^"1")
    in
    aux t "" ;
    res
    
let pp_enc_dictionary (fmt : Format.formatter) (ed : encoding_dictionary) : unit =
    Format.fprintf fmt "@[<hv>{ " ;
    Hashtbl.iter (fun c s -> Format.fprintf fmt "%c -> %s " c s) ed ;
    Format.fprintf fmt "}@]"
    
let rec find (d : data) (i : int) (t : tree) : (char * int) =
    match t with
    | Leaf c -> (c, i)
    | Node (t0, t1) ->
        if i >= String.length d then failwith "Looking beyond the end of the string :o" ;
        let c = String.get d i in
        match c with
        | '0' -> find d (i+1) t0
        | '1' -> find d (i+1) t1
        | _ -> failwith "Why is there something other than 0 or 1 in the string?"
        
let write (t : tree) : data =
    let rec aux_cps t cont =
        match t with
        | Leaf c -> cont (Char.escaped c)
        | Node (t0, t1) -> (*let acc' = aux (acc^"0") t0 in aux acc' t1*)
            aux_cps t0 (fun res0 -> aux_cps t1 (fun res1 -> cont ("0"^res0^res1)))
    in
    aux_cps t (fun x -> x)
    
let read (d : data) : tree * int =
    let rec aux i =
        match String.get d i with
        | '0' ->
            let t0, i1 = aux (i+1) in
            let t1, i2 = aux i1 in
            Node (t0, t1), i2
        | c -> Leaf c, (i+1)
    in
    aux 0

let build_encoded_data (t : text) (ed : encoding_dictionary) : data =
    let len = String.length t in
    let rec aux i acc =
        if i >= len then acc
        else aux (i+1) (acc^(Hashtbl.find ed (String.get t i)))
    in
    aux 0 ""
            

let compress (txt : text) : data =
    let tree = txt |> build_alphabet |> build_tree in
    let dict = build_encoding_dictionary tree in
    let tree_data = write tree in
    let text_data = build_encoded_data txt dict in
    tree_data ^ text_data
    
let decompress (d : data) : text =
    let tree, id_data = read d in
    let len = String.length d in
    let rec aux i acc =
        if i >= len then acc
        else 
            let char, id = find d i tree in
            aux id (acc^(Char.escaped char))
    in
    aux id_data ""

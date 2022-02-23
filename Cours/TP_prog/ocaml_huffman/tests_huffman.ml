open Huffman

let test_q () =
    let q1 = Q.empty in
    Format.printf "%a, is empty: %B@." pp_q_char q1 (Q.is_empty q1) ;
    let q2 = Q.insert (1, 'a') q1 in
    Format.printf "%a, is empty: %B@." pp_q_char q2 (Q.is_empty q2) ;
    let q3 = Q.insert (3, 'b') q2 in
    Format.printf "%a@." pp_q_char q3 ;
    let q4 = Q.insert (0, 'c') q3 in
    Format.printf "%a@." pp_q_char q4 ;
    let (p, x), q5 = Q.extract q4 in
    Format.printf "min: (%i, %c), q: %a@." p x pp_q_char q5
    
let test_build_huffman () =
    let text = "abcdaecaaa" in
    let alph = build_alphabet text in
    Format.printf "%s : %a@." text pp_alphabet alph ;
    let tree = build_tree alph in
    (* Format.printf "%a@." pp_tree tree ; *)
    let ed = build_encoding_dictionary tree in
    Format.printf "%a@." pp_enc_dictionary ed ;
    let data = build_encoded_data text ed in
    let (c1, i1) = find data 0 tree in
    let (c2, i2) = find data i1 tree in
    let (c3, i3) = find data i2 tree in
    let (c4, i4) = find data i3 tree in
    let (c5, i5) = find data i4 tree in
    Format.printf "%s -> %c|%c|%c|%c|%c...@." data c1 c2 c3 c4 c5 ;
    let serialized_tree = write tree in
    Format.printf "%s@." serialized_tree ;
    let tree_data = serialized_tree ^ data in
    let deserialized_tree, id = read tree_data in
    Format.printf "%a@." pp_enc_dictionary (build_encoding_dictionary deserialized_tree) ;
    let compressed_text = compress text in
    Format.printf "%s@." compressed_text ;
    let decompressed_text = decompress compressed_text in
    Format.printf "%s@." decompressed_text 
    
    
let () =
    test_q () ; 
    test_build_huffman () ;
    Format.printf "done@."

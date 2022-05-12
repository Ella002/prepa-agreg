let gen n =
    Array.init n (fun _ ->
        List.map fst
            (List.filter snd
                (List.init n (fun i -> (i, Random.float 1.0 < 0.1)))))

let p g =
    let n = Array.length g in
    let e = Array.make n 0 in
    let x = ref 0 in  let f = ref true in
    let c = ref 0 in
    while !f do while !x < n && e.(!x) <> 0 do incr !x done;
    f := !x < n;
    if f then begin
        incr c; let p = ref [!x] in
            while !p <> [] do
        let v = List.hd !p in p := List.tl !p;
            e.(v) <- c; let vl = ref g.(v) in
    while !vl <> [] do let y = List.hd !vl in
                vl := List.tl !vl;
        if e.(y) == 0 then p = y :: !p
            done
        done
    end done;
    e

let _ =
    let g = gen 10 in
    let c = p g in
    for i = 0 to 9 do
        Printf.printf "%d->%d\n" i c.(i)
    done

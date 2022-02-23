CC = ocamlc

all: tests

%.cmo: %.ml
	$(CC) -c $<

tests: huffman.cmo tests_huffman.ml
	$(CC) $^ -o $@

clean:
	rm -f tests *.cmo *.cmi

# 25 - Analyses lexicale et syntaxique. Applications. #

## Version Yaëlle ##

### Source ###

- [Compilation: analyse lexicale et syntaxique, Legendre et Schwarzentruber](https://www.amazon.fr/Compilation-Lexicale-Syntaxique-Structure-Informatique/dp/2340003660)

### [Notes](notesYV.md) ###

### Plan ###

[Plan détaillé](planYV.pdf)
NB: y a erreur dans l'algo d'analyse lexicale, il manque le texte dans les entrées

1. Motivation: compilation
2. Analyse lexicale
  1. Principe: lexèmes, règle d'analyse lexicale, utilisation automates
  2. Algorithme
  3. Applications
	* Dev 1 = utilisation ocamllex
3. Analyse syntaxique
  1. Contexte: grammaire, dérivation
  2. Analyse descendante
  3. Analyse LL(1)
	* Dev 2 = analyse LL(1) sur langage arithmétique
4. Applications

### Développements ###

- Dev 1 : exemple d'utilisation d'OCamllex -> ne fonctionne pas, pas assez de contenu

- Dev 2 : analyse LL(1): calcul de null / first / follow pour une grammaire donnée
  [Notes](YV-LL1.pdf)

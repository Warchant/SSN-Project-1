#!/usr/bin/env make

TEX = latexmk -pdf -pdflatex="pdflatex -file-line-error -interaction=nonstopmode" -use-make
BIB = bibtex


main.pdf: main.tex main.bib main.aux main.bbl main.blg
	$(TEX) main.tex

.PHONY: clean
clean: 
	latexmk -C && rm -f *.fls *.swp *.aux *.bbl *.pyg *-blx.bib *.run.xml *.synctex.gz; rm -r _minted*

main.bbl main.blg: main.bib main.aux
	$(BIB) main

main.aux: 
	$(TEX) main.tex

main.bib: 
	$(TEX) main.tex

.PHONY: all
all: main.pdf

open: main.pdf
	evince main.pdf

#!/usr/bin/env make

TEX = latexmk -pdf -pdflatex="pdflatex -file-line-error -shell-escape -interaction=nonstopmode" -use-make
BIB = bibtex

.PHONY: main.pdf all clean

all: main.pdf

main.pdf: main.tex 
	$(TEX) main.tex

clean:
	latexmk -CA; rm main.bbl

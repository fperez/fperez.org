# Simple makefile to keep html versions up to date

all: README.html numpy-pep225.html

# Suffix rules
# make html out of rest
%.html : %.txt
	rst2html $< $*.html

%.html : %.rst
	rst2html $< $*.html

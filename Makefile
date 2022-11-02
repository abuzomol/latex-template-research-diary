
YEAR := 2022
AUTHOR := Muzamil Yahia
INSTITUTION := University of Hawaii

# Do not edit past this line
RM := rm -rf
SHELL := /bin/bash

TEXFILE := $(YEAR)-Research-Diary.tex
LOGFILE := $(YEAR)-Research-Diary.log
DVIFILE := $(YEAR)-Research-Diary.dvi
PSFILE := $(YEAR)-Research-Diary.ps
PDFFILE := $(YEAR)-Research-Diary.pdf
AUXFILE := $(YEAR)-Research-Diary.aux
OUTFILE := $(YEAR)-Research-Diary.out
AUX := $(YEAR)-Research-Diary.fls
AUXX := $(YEAR)-Research-Diary.fdb_latexmk
.PHONY : clean

anthology:
	-@echo 'Creating anthology for research diary entries from the year $(YEAR)'
	-$(RM) $(YEAR)-Research-Diary.*
	-python3 create_anthology.py "--year=$(YEAR)" "--author=$(AUTHOR)" "--institute=$(INSTITUTION)"
	latexmk -pdf $(TEXFILE)

all:
	cd $(YEAR);  latexmk -pdf ; ./clean.sh ; cd ..


clean:
	-$(RM) $(TEXFILE)
	-$(RM) $(LOGFILE) $(DVIFILE) $(PSFILE) $(AUXFILE) $(OUTFILE)
	-$(RM) $(AUX) $(AUXX)
	-$(RM) *.tmp
	-@echo 'Done cleaning'

#!/bin/bash
#takes a directory of pdfs, performs ocr on them using
#tesseract and then adds the text back into the pdf

for i in `ls *.pdf`; do
    mkdir temp
    mv $i temp
    cd temp
    pdftoppm -gray $i sample
    for x in `ls *.pgm`; do
        tesseract $x outputtext hocr
        hocr2pdf -i $x -o $x'.pdf' < outputtext.html
        rm outputtext.html
    done
    rm $i
    pdfunite *.pdf $i
    rm sample*
    mv $i ..
    rm -r temp
done

#!/bin/bash
#takes a directory of folders containing pdf files, runs them through
#unpaper and then collates the pdfs into single files based on their
#directory name

for dir in `ls`; do
    NUM=1
    for pdf in `ls $dir/*.pdf`; do
        pdftoppm -gray $pdf $NUM'sample'
        NUM=`expr $NUM + 1`
    done

    for i in `ls *.pgm`; do
        unpaper $i 'un'$i
        pnmtotiff 'un'$i > 'un'$i.tiff
    done

    tiffcp *.tiff all.tiff

    for i in `ls *sample*`; do
        rm $i
    done

    tiff2pdf -z -o Document.pdf all.tiff
    rm all.tiff
    rm $dir/*.pdf
    mv Document.pdf $dir/$dir.pdf
done

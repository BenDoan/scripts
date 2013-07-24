#!/bin/bash
# unzips all .zip files in the cwd into folders with the names of the zip files

for x in *.zip; do
    mkdir `basename $x .zip`
    mv $x `basename $x .zip`
    cd `basename $x .zip`
    unzip $x
    mv $x ..
    cd ..
done

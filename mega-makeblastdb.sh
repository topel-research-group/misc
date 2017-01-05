#!/bin/bash

for file in $(ls *.proteins.fasta);
do
makeblastdb -in $file -out $(echo $file | sed -e 's/\.proteins.fasta//g') -dbtype prot
done;

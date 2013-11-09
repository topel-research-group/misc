#!/bin/bash

for file in $(ls *_peptide.fa);
do
makeblastdb -in $file -out $(echo $file | sed -e 's/\_peptide.fa//g') -dbtype prot
done;

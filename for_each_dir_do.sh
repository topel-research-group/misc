#!/bin/bash

# This script will execute a command ($1) in
# each subdirectory from where it is executed.
#
# Usage: for_each_dir_do.sh "ls -l *.txt"
#	 for_each_dir_do.sh "fastqc *.fastq"
#
# Warning: Use with CAUTION. 

HERE=`pwd`

for DIR in `find . -type d`
do
cd $DIR
$*
cd $HERE
done

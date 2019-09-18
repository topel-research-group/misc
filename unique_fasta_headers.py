#!/usr/bin/env python3

# Input: fasta file
# output: fasta to STDOUT where each header 
# has been prefixed with a unique number.

import sys

file = open(sys.argv[1], "r")
num = 1

for line in file:
	if line[0] == ">":
		print(line.rstrip()[0] + str(num) + "_" + line.rstrip()[1:])
		num += 1
	else:
		print(line.rstrip())

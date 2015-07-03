#!/usr/bin/env python

# This program takes a fasta file as input and tries to 
# move the sequence name to the beginning of the line. 
# This simplifies viewing of multiple sequence alignments 
# in alignments editors like SeaView.
#
# Usage:	names_first.py all.mafft.fst > all.mafft.names.fst

import sys
in_file = sys.argv[1]  
file = open(in_file, "r")

for line in file:
	if line[0] == ">":
		if "[" in line:
			first = line.split("[")[0].replace(">","")
			name = line.split("[")[1].split("]")[0]
			last = line.split("]")[1]
			name = name.replace(" ", "_")
			print "%s%s_%s%s" % (">", name, first, last)
		else:
			print line,
	else:
		print line,
file.close()

#!/usr/bin/env python

# Syntax:	names_first.py all.mafft.fst > all.mafft.names.fst


import sys

in_file = sys.argv[1]  # Input xml file

file = open(in_file, "r")

for line in file:
	if line[0] == ">":
		if "@" in line:
			line.split("@")
			first = line.split("@")[0]
			print "%s%s_%s%s" % (">", line.split("@")[1], first.split(">")[1], line.split("@")[2])
		else:
			print line,
	else:
		print line,
file.close()

#!/usr/bin/env python


import sys

in_file = open(sys.argv[1], "r")

contig_names = {}

for line in in_file.readlines():
	contig = line.split()[0]
	if contig in contig_names:
		contig_names[contig] += 1
	else:
		contig_names[contig] = 1
for i in contig_names:
	print i, contig_names[i]

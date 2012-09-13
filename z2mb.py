#!/usr/bin/env python

import sys

in_file = sys.argv[1]
cutoff = float(sys.argv[2])
print type(cutoff)			# Devel
print cutoff				# Devel.
file = open(in_file, "r")
line_nr = 1
excluded = "F"

# For the MrBayes block
print "exclude",
for line in file:
	line = float(line)
	if line < cutoff:
		print line_nr,
		excluded = "T"
	line_nr += 1
if excluded == "F":
	print "all",
print ";"

#!/usr/bin/env python

import sys

in_file = sys.argv[1]
cutoff = sys.argv[2]
file = open(in_file, "r")
line_nr = 1
excluded = "F"
print "exclude",
for line in file:
	if line < cutoff:
		print line_nr,
		line_nr += 1
		excluded = "T"
if excluded == "F":
	print "all",
print ";"

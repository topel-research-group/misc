#!/usr/bin/env python3

import sys

infile = open(sys.argv[1])
suffix = 1
for line in infile.readlines():
	if line[:4] == "@/?/":
		print(line.rstrip().replace("/?/", "") + "_" + str(suffix))
		suffix += 1
	else:
		print(line.rstrip())


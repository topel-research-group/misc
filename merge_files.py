#!/bin/env python

# This script takes two tab separated files and meges the lines. 
# The result is printed to STDOUT. The code asumes that the first 
# column of both files contains something that can be used as a 
# key in a python dictionary. The two input files does not have 
# to have the same number of rows, an the content of the second 
# file will be merged to the first line.

# Syntax: merge_files.py <file1> <file2> > <merged_file>

import sys

file1 = open(sys.argv[1], "r")
file2 = open (sys.argv[2], "r")

# Parse an input files and store the content in two dictionaries.
def parse_file(inputFile1, inputFile2):
	dict1 = {}
	dict2 = {}
	# Parse the first file
	for line in inputFile1.readlines():
		dict1[line.split()[0]] = line.rsplit()
	# Pares the second file
	for line in inputFile2.readlines():
		dict2[line.split()[0]] = line.rsplit()

	# Loop over the elements in the first dictionary
	# and merge it with the corresponding element in
	# the second dictionary.
	for key, value in dict1.iteritems():
		try:
			new_line = dict1[key] + dict2[key]
			print str(new_line).replace("'", "").replace(",", "").replace("[", "").replace("]", "")
		except KeyError:
			print dict1[key]
			print "Error"


if __name__ == "__main__":
	parse_file(file1, file2)


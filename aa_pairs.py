#!/usr/bin/env python

# aa_pairs.py finds pairs, triplets and so on, of residues in amino acid sequences.
# Requires: BioPython
# Input: integer [2 for pairs, 3 for triplets etc.] and a fasta file with sequens(es).
#
# 	$ cat test.fst
#	>seq1
#	MATV
#	>seq2
#	MASS
#			
# Output:
#
#	>seq1
#	MATV
#	TV: 1
#	MA: 1
#	AT: 1
#
#	>seq2
#	MASS
#	SS: 1
#	MA: 1
#	AS: 1
#
#	Combined result for 2 sequences:
#	aa  nr:
#	MA: 2   100.0 %
#	TV: 1   50.0 %
#	SS: 1   50.0 %
#	AT: 1   50.0 %
#	AS: 1   50.0 %
#
# Usage: ./aa_pairs.py 2 test.fst > out.txt


import sys
from Bio import SeqIO

length = int(sys.argv[1])
in_file = sys.argv[2]  	# Import fasta file
finalDict = {}			# Will hold the combined results from all sequences


def getPairs(header, sequence):
#	Identify all diferent pairs of amino 
#	acids in a sequence.
#
#	Input: An amino acid sequence.
#
#	Return: Prints the name of the sequence, the 
#	amino acid sequencea and a  dictionary of amino acid 
#	pairs (key) and their number of 
#	occurrences (value) in the input sequence
#	to STDOUT. 

	dictionary = {}
	count = 0
	
	print ">%s" % header
	print sequence
	
	for aa in sequence:
		pair = sequence[count:count + length]
		if len(pair) == length:
			if str(pair) in dictionary:
				dictionary[str(pair)] += 1 
			else:
				dictionary[str(pair)] = 1
			count += 1
	sortDict(dictionary)
	combineDicts(dictionary)


def sortDict(dictionary, nr_seq=0, calc_percent=False):
#	Sorts a dictionary according to values.
#
#	Input: A dictionary and optionally the number 
#		   (as an int) of files in the analysis and 
#		   a bolean "True" if percentage of sequences 
#		   with the motif sould be calculated.
	sorted_dict = {}
	for key, value in sorted(dictionary.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		if calc_percent == True:
			percent = round((float(value)/nr_seq)*100, 1)
			print "%s: %s   %s %s" % (key, value, percent, "%")
		else:
			print "%s: %s" % (key, value)
	print ""


def combineDicts(dictionary):
#	Combines the results from the 
#	analyses of individual sequences.
#
#	Input: Dictionary that should be 
#		   included in the combined result.
#
#	Return: Dictionary of combined results.
	if perSeq == False:
		for key, value in dictionary.iteritems():
			if key in finalDict:
				finalDict[key] += 1
			else:
				finalDict[key] = 1
		return finalDict


if __name__ == "__main__":
	nr_seq = 0
	for record in SeqIO.parse(in_file, "fasta"):
		getPairs(record.id, record.seq)
		nr_seq += 1
	print "Combined result for %s sequences:" % nr_seq
	print "aa  nr:"
	sortDict(finalDict, nr_seq, True)

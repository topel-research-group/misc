#!/usr/bin/env python3.7

# This script takes one or several fastq files as input

import argparse
import random
import sys
from Bio import SeqIO

###########################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*", type=str, help="The name(s) of the fastq input file(s).")
parser.add_argument("-n", "--sample", help="Number of sequences to sample")
parser.add_argument("-r", "--remove", help="File with fastq headers from sequences to remove")
args = parser.parse_args()
###########################################################################################

def read_fastq_file(infile):
	my_file = SeqIO.parse(infile, "fastq")
	for fastq_seq in my_file:
#		sampleDict[fastq_seq.id] = fastq_seq
		yield fastq_seq
	my_file.close()


### Print random sample of sequences to STDOUT ###
def sample():
	sampleDict = {}
	for infile in args.files:
		my_file = SeqIO.parse(infile, "fastq")
#		with SeqIO.parse(infile, "fastq") as my_file:
		for fastq_seq in my_file:
			sampleDict[fastq_seq.id] = fastq_seq
	# Make sure that the number of sequences in the 
	# input file(s) are greater then the desired sample.
	try:
		randomList = random.sample(sampleDict.items(), int(args.sample))
	except ValueError:
		sys.exit("[Error] The requested random sample is greater than the total number of sequences.")
	for seq in randomList:
		print(seq[1].format("fastq").rstrip("\n"))
	my_file.close()
	exit("Process exited successfully")

def remove_seq():
	remove_file = open(args.remove, "r")
	# Store the headers in a set
	headers = set()
	for header in remove_file:
		headers.add(header.rstrip())
#	print(headers)
	# parse the fastq file(s)
	for infile in args.files:
		for fastq_seq in read_fastq_file(infile):
			if fastq_seq.id in headers:
				pass
			else:
				print(fastq_seq.format("fastq").rstrip("\n"))
		
	
				
if __name__ == "__main__":
	
#	if args.sample == True:
#		sample()
	
	if args.remove:
		remove_seq()


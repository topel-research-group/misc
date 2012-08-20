#!/usr/bin/env python

from optparse import OptionParser
from Bio.Blast.Applications import NcbiblastpCommandline
import sys
from Bio import SeqIO
from Bio.Blast import NCBIXML
import subprocess
import os

# Figure out the options and arguments
def input(option, opt_str, value, parser):
	assert value is None
	value = []
	for arg in parser.rargs:
		# Stop on --foo like option
		if arg[:2] == "--" and len(arg) > 2:
			break
		# Stop on -a
		if arg[:1] == "-" and len(arg) > 1:
			break
		value.append(arg)
	del parser.rargs[:len(value)]
	setattr(parser.values, option.dest, value)


###################################################################

# Options, arguments and help
usage = "\n  %prog -p [PATR to db dir] -d [blast_db-1 blast_db-2 ...] -q [fasta file] -l [or] -m"
opts=OptionParser(usage=usage, version="%prog v.1.0.1")

opts.add_option("--path", "-p", dest="db_dir", action="callback",
callback=input, help="Path to directory with blast formated databases")

opts.add_option("--database", "-d", dest="databases", action="callback",
callback=input, help="Blast databases to use")

opts.add_option("--query", "-q", dest="query_file", action="callback",
callback=input, help="Query sequene used for the BLAST analyses")

opts.add_option("--all", "-a", dest="all_db", action="store_true", 
default=False, help="Use all BLAST databases in indicated directory")

opts.add_option("--mafft", "-m", dest="mafft_alignment", action="store_true",
default=False, help="Use mafft to align the sequences")

opts.add_option("--linsi", "-l", dest="linsi_alignment", action="store_true",
default=False, help="Use linsi to align the sequences")

opts.add_option("--nr_hits", "-n", dest="nr_of_hits", action="callback",
callback=input, default=['1'], help="Same as the BLAST option 'max_target_seqs' that indicates the number of hits to save")

options, arguments = opts.parse_args()

####################################################################


def xml_to_fasta(xml_file, db_dir, database, query_file):
	hit_id_list = ""
	for record in NCBIXML.parse(open(xml_file)):
		if record.alignments:
			for align in record.alignments:
				for hsp in align.hsps:
					hit_id_list = hit_id_list + align.hit_id + ","
	run_blastdbcmd(hit_id_list[0:-1], db_dir, database, query_file)


def run_blastdbcmd(xml_file, db_dir, database, query_file):
	args = ["blastdbcmd", "-entry", '%s' % xml_file, '-db', 
	'%s/%s' % (db_dir, database), '-out', '%s_%s.fasta' 
	% (query_file[:-4], database)]
	subprocess.call(args)


### Run the actuall BLAST analyses
def blast(query_file, blast_db, out_file):
	blast_cmd = NcbiblastpCommandline(  query = query_file,
										db = blast_db,
										out = out_file,
										task = "blastp",
										outfmt = 5,
#										evalue = 1000)              # Hack. Better to check if "*.fasta" file exists.
#										max_target_seqs = options.nr_of_hits[0])
										max_target_seqs = options.nr_of_hits[0])
	stdout, stderr = blast_cmd()


def alignment(method, query_file, database):
	# Append the query sequence to the file with 
	# the sequences found in the BLAST search
	file1 = open("%s_%s.fasta" % (query_file[:-4], database), "a")
	file2 = open(query_file, "r")
	file1.write(file2.read())
	file1.close()
	file2.close()
	# Run the alignment analysis
	out = subprocess.Popen([method, "--reorder", "%s_%s.fasta" 
	% (query_file[:-4], database)], stdout=subprocess.PIPE)
	file3 = open("%s_%s.%s.fasta" % (query_file[:-4], database, method), "w")
	file3.write(out.communicate()[0])
	file3.close()


def identify_databases():
	database_list = []
	for filename in os.listdir(options.db_dir[0]):
		if filename[-4:] == ".psq":
			database_list.append(filename[:-4])
	return database_list


def run_analysis():
	# When the -a flag is used
	if options.all_db == True:
		my_databases = identify_databases()
	# When the -a flag is NOT in use
	if options.all_db == False:
		my_databases = options.databases

	for query_file in options.query_file:
		for database in my_databases:
			blast(query_file, "%s/%s" % (options.db_dir[0], database), 
			"%s_%s.xml" % (query_file[:-4], database))
			xml_to_fasta("%s_%s.xml" % (query_file[:-4], database), 
			"%s" % options.db_dir[0], database, query_file)

			if options.mafft_alignment == True:
				alignment("mafft", query_file, database)
			if options.linsi_alignment == True:
				alignment("linsi", query_file, database)



if __name__ == "__main__":
	run_analysis()

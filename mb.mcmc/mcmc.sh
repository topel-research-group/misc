#!/usr/bin/env bash

# This script, together with "mcmc.mix.mb-3.2.R" is 
# used to visualise the content of the *.mcmc file 
# produced by MrBayes (http://mrbayes.sourceforge.net/download.php).

R --no-restore --no-save --slave -f ./mcmc.mix.mb-3.2.R --args $1

#!/bin/bash
#This script runs a given scenario simulation

echo "Running scenario!"

#exit on error
set -e
#turn on command echoing
set -v

#process
sh ./1_run.sh
echo "Script ran"
sh ./2_process.sh
echo "Script ran"
sh ./3_plot.sh
echo "Script ran"


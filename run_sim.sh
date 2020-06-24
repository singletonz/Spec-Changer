#!/bin/bash
#This script runs a given scenario simulation

echo "Running scenario!"

#exit on error
set -e
#turn on command echoing
set -v

#process
( "/home/midnight/Documents/partmc-2.5.0/scenarios/4_chamber/1_run.sh" )
echo "Script one finished!"
( "/home/midnight/Documents/partmc-2.5.0/scenarios/4_chamber/2_process.sh" )
echo "Script two finsihed!"
( "/home/midnight/Documents/partmc-2.5.0/scenarios/4_chamber/3_plot.sh" )
echo "Script three finished!"


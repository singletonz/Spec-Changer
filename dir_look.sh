#!/bin/bash

#clear
echo "Hi $USER!"
#echo "Running simulation"

ls -l

read -p "Enter file to display contents: " f1

if [ -r $f1 ]; then
        #content=$(cat urban_plume.spec)
        cat $f1
elif [ -f $f1 ]; then
        echo "The file '$f1' exists but is not readable to the script."
else
    	echo "The file '$f1' does not exist."
fi

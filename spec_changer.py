#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 07:04:05 2020

@author: singletonz
"""
#Rough draft or python code for partmc model
#This is in no means to replace current code apart of partmc-mosaic model
#

import os
import subprocess

value = input("Enter value to replace: \n")
value1 = input("Enter value: \n")




#read input file
fin = open("urban_plume.spec", "rt")

#read file contents to string
data = fin.read()

#replace all occurrences of the required string
data = data.replace(value, value1)

#close the input file
fin.close()

#open the input file in write mode
fin = open("urban_plume.spec", "wt")

#overrite the input file with the resulting data
fin.write(data)

#close the file
fin.close()

subprocess.call(['./test.sh'])



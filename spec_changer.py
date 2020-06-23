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

value = input("Enter file name: \n")
#value1 = input("Enter value: \n")

#spec input
spec1 = input("Enter spec to change: \n")
spec2 = input("Enter value: \n")


#read input file
fin = open(value, "rt")
data = fin.read()

data = data.replace(spec1, spec2)

#close the input file
fin.close()

#open the input file in write mode
fout = open(value, "wt")

#overrite the input file with the resulting data
fout.write(data)

#close the file
fout.close()

subprocess.call(['./test.sh'])



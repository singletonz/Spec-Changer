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
import sys

#Display directory
#if subprocess.call(['./test.sh']):
#    print("It works!")
#elif print("It didn't work")
#    sys.exit()

while True:
   answer = input('Check directory contents? "y" to run, "n" to cancel, "c" to continue')
   if answer.lower().startswith("y"):
      subprocess.call(['./test.sh'])
   elif answer.lower().startswith("n"):
      sys.exit()
   elif answer.lower().startswith("c"):
       break
       
       
value = input("Enter file to modify: \n")
#value1 = input("Enter value: \n")

#spec input
spec1 = input("Enter spec to change:\n Ex: t_max 100\n")
spec2 = input("Enter new value:\n Ex: t_max 50\n")


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
print("End of job")

#subprocess.call(['./test.sh'])

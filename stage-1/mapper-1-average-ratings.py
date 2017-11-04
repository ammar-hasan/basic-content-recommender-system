#!/usr/bin/env python

''' 
[Mapper - Stage 1 - Average User Ratings]
Author: Ammar Hasan Razvi
'''

import sys
import csv

'''
Algorithm:
'''

for row in csv.reader(iter(sys.stdin.readline, '')):
  if row[0] == 'userId':
    continue

  print('%s,%s' % (row[1], row[2]))

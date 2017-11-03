#!/usr/bin/env python

''' 
[Mapper - Stage 1 - Join Movies and Ratings]
Author: Ammar Hasan Razvi
Roll no: CT-088
NED-MSCSIT-2016/17
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

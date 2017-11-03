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
  a = row[0].strip()
  b = row[1].strip()
  c = row[2].strip()

  if a == 'movieId':
    continue

  writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
  if len(row) == 4:
    writer.writerow([int(a), 'rating', float(b), int(c)])
  else:
    writer.writerow([int(a), 'profile', b, c])

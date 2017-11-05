#!/usr/bin/env python

''' 
[Mapper - Stage 2 - Join Movies and Ratings]
Author: Ammar Hasan Razvi
'''

import sys
import csv

'''
Algorithm:
'''

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
for row in csv.reader(iter(sys.stdin.readline, '')):
  a = row[0].strip()
  b = row[1].strip()
  c = row[2].strip()

  if a == 'movieId':
    continue

  if len(row) == 4:
    writer.writerow([int(a), 'rating', float(b), int(c)])
  else:
    writer.writerow([int(a), 'profile', b, c])

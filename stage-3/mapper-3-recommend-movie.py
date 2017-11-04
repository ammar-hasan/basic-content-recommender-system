#!/usr/bin/env python

''' 
[Mapper - Stage 3 - Recommend Movies]
Author: Ammar Hasan Razvi
'''

import sys
import csv

'''
Algorithm:
'''

originalId = 11

for row in csv.reader(iter(sys.stdin.readline, '')):
  if row[0] == 'movieId':
    continue

  movieId = int(row[0])

  writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
  
  if movieId == originalId:
    row.insert(0, 'a')
  else:
    row.insert(0, 'b')

  writer.writerow(row)

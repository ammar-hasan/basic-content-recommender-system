#!/usr/bin/env python

''' 
[Mapper - Stage 4 - Make Recommendations]
Author: Ammar Hasan Razvi
'''

import sys
import csv

'''
Algorithm:
'''

for row in csv.reader(iter(sys.stdin.readline, '')):
  writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
  key = '%s-%s-%s' % (row[4], row[5], row[0])
  row.insert(0, key)
  writer.writerow(row)
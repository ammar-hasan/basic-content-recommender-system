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

writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
for row in csv.reader(iter(sys.stdin.readline, '')):
  key = '%s-%s-%s' % (row[4].strip(), row[5].strip(), row[0].strip())
  row.insert(0, key)
  writer.writerow(row)
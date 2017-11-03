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
movie = None
accumulatedRatings = 0
totalRatings = 0

print('movieId,rating,totalRatings,type')

for row in csv.reader(iter(sys.stdin.readline, '')):
  current = int(row[0].strip())

  if movie != current:
  	if movie is not None and totalRatings > 0:
		writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
		writer.writerow([movie, round(accumulatedRatings / totalRatings, 4), totalRatings, 'r'])

  	movie = current
  	accumulatedRatings = float(row[1].strip())
  	totalRatings = 1
  else:
  	accumulatedRatings += float(row[1].strip())
  	totalRatings += 1

if movie is not None and totalRatings > 0:
	writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
	writer.writerow([movie, round(accumulatedRatings / totalRatings, 4), totalRatings, 'r'])

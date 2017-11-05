#!/usr/bin/env python

''' 
[Reducer - Stage 1 - Average User Ratings]
Author: Ammar Hasan Razvi
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

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
for row in csv.reader(iter(sys.stdin.readline, '')):
  current = int(row[0].strip())

  if movie != current:
    if movie is not None and totalRatings > 0:
      writer.writerow([movie, round(accumulatedRatings / totalRatings, 4), totalRatings, 'r'])

    movie = current
    accumulatedRatings = float(row[1].strip())
    totalRatings = 1
  else:
  	accumulatedRatings += float(row[1].strip())
  	totalRatings += 1

if movie is not None and totalRatings > 0:
	writer.writerow([movie, round(accumulatedRatings / totalRatings, 4), totalRatings, 'r'])

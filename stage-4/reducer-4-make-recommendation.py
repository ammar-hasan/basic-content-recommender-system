#!/usr/bin/env python

''' 
[Reducer - Stage 4 - Make Recommendations]
Author: Ammar Hasan Razvi
'''

import sys
import csv

'''
Algorithm:
'''
MAX_RECOS = 14
MIN_RATING = 3.0
MIN_SIMILAR = 0.95

recos = 0

print('movieId,title,genre,rating,totalRatings')
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

for row in csv.reader(iter(sys.stdin.readline, ''), delimiter='\t'):
  rating = float(row[5].strip())

  if rating < MIN_RATING:
    continue

  similarity = float(row[1].strip())
  if similarity < MIN_SIMILAR:
    continue

  if recos >= MAX_RECOS:
    continue

  movieId = int(row[2].strip())
  title = row[3].strip()
  genre = row[4].strip()
  totalRatings = int(row[6].strip())

  writer.writerow([movieId, title, genre, rating, totalRatings])

  recos += 1
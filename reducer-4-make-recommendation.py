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
MAX_RECOS = 14
MIN_RATING = 3.0
MIN_SIMILAR = 0.95

recos = 0

print('movieId,title,genre,rating,totalRatings')

for row in csv.reader(iter(sys.stdin.readline, '')):
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

  writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
  writer.writerow([movieId, title, genre, rating, totalRatings])

  recos += 1
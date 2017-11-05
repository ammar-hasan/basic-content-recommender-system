#!/usr/bin/env python

''' 
[Reducer - Stage 3 - Recommend Movies]
Author: Ammar Hasan Razvi
'''

import sys
from math import sqrt
import csv

'''
Algorithm:
'''

GENRE_FACTOR = 1
RATING_FACTOR = 4

movieId = None
genres = None
rating = 0
totalRatings = 0
setA = None

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
for row in csv.reader(iter(sys.stdin.readline, '')):
  kind = row[0]
  cMovieId = row[1]
  cTitle = row[2]
  cAllGenre = row[3]
  cGenres = cAllGenre.split('|')
  cRating = float(row[4])
  cTotalRatings = int(row[5])

  if kind == 'a':
    movieId = cMovieId
    genres = cGenres
    rating = cRating
    totalRatings = cTotalRatings
    setA = []
    for genre in genres:
      setA.append(GENRE_FACTOR)

    setA.append(cRating * RATING_FACTOR)
    setA.append(cTotalRatings ** (1. / 3)) # cube root
    continue

  setB = []

  for genre in genres:
    if genre in cGenres:
      setB.append(GENRE_FACTOR)
    else:
      setB.append(0)

  if sum(setB) == 0:
    continue
  
  setB.append(cRating * RATING_FACTOR)
  setB.append(cTotalRatings ** (1. / 3))

  numerator = 0
  denomenatorA = 0
  denomenatorB = 0

  for idx, val in enumerate(setA):
    numerator += (val*setB[idx])
    denomenatorA += (val*val)
    denomenatorB += (setB[idx]*setB[idx])

  denomenator = sqrt(denomenatorA) * sqrt(denomenatorB)

  factor = round(numerator / denomenator, 5) # using cosine similarity

  writer.writerow([float(factor), int(cMovieId), cTitle, cAllGenre, float(cRating), int(cTotalRatings)])
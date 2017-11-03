#!/usr/bin/env python

''' 
[Mapper - Stage 1 - Join Movies and Ratings]
Author: Ammar Hasan Razvi
Roll no: CT-088
NED-MSCSIT-2016/17
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

  factor = round(numerator / denomenator, 5)

  writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
  writer.writerow([float(factor), int(cMovieId), cTitle, cAllGenre, float(cRating), int(cTotalRatings)])
#!/usr/bin/env python

''' 
[Reducer - Stage 2 - Join Movies and Ratings]
Author: Ammar Hasan Razvi
'''

import sys
import csv

'''
Algorithm:
'''

class Profile:
  movieId = None
  title = None
  genre = None
  rating = None
  totalRatings = None

def setProfile(row, profile=Profile()):
  if row[1] == 'profile':
    profile.movieId = int(row[0].strip())
    profile.title = row[2].strip()
    profile.genre = row[3].strip()
  elif row[1] == 'rating':
    profile.movieId = int(row[0].strip())
    profile.rating = float(row[2].strip())
    profile.totalRatings = int(row[3].strip())
  return profile

movieId = None
profile = None

print('%s,%s,%s,%s,%s' % ('movieId', 'title', 'genre', 'rating', 'totalRatings'))

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
for row in csv.reader(iter(sys.stdin.readline, '')):
  cid = row[0].strip()

  if movieId != cid:
    if movieId is not None:
      writer.writerow([profile.movieId, profile.title, profile.genre, profile.rating, profile.totalRatings])

    movieId = cid
    profile = setProfile(row)
  else:
    profile = setProfile(row, profile)

if movieId is not None:
  writer.writerow([profile.movieId, profile.title, profile.genre, profile.rating, profile.totalRatings])
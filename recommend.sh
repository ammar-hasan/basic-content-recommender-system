#!/bin/bash
echo "Executing stage-1 (Calculating average ratings), result will go to ${PWD}/output/stage-1-out.txt";
cat "data/ratings.csv" | python "stage-1/mapper-1-average-ratings.py" | sort | python "stage-1/reducer-1-average-ratings.py" > "output/stage-1-out.txt";
echo "Executing stage-2 (Joining movies with ratings), result will go to ${PWD}/output/stage-2-out.txt";
cat "data/movies.csv" "output/stage-1-out.txt" | python "stage-2/mapper-2-join-ratings.py" | sort | python "stage-2/reducer-2-join-ratings.py" > "output/stage-2-out.txt";
echo "Executing stage-3 (Calculating recommendations), result will go to ${PWD}/output/stage-3-out.txt";
cat "output/stage-2-out.txt" | python "stage-3/mapper-3-recommend-movie.py" | sort | python "stage-3/reducer-3-recommend-movie.py" > "output/stage-3-out.txt";
echo "Executing stage-4 (Final Stage: Make recommendations), result will go to ${PWD}/output/final-out.txt";
cat "output/stage-3-out.txt" | python "stage-4/mapper-4-make-recommendation.py" | sort -r | python "stage-4/reducer-4-make-recommendation.py" > "output/final-out.txt";
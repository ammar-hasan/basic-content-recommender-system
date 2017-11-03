call cat ratings.csv | python "mapper-1-average-ratings.py" | sort | python "reducer-1-average-ratings.py" > "stage-1-out.txt"
call cat movies.csv "stage-1-out.txt" | python "mapper-2-join-ratings.py" | sort | python "reducer-2-join-ratings.py" > "stage-2-out.txt"
call cat "stage-2-out.txt" | python "mapper-3-recommend-movie.py" | sort | python "reducer-3-recommend-movie.py" > "stage-3-out.txt"
call cat "stage-3-out.txt" | python "mapper-4-make-recommendation.py" | sort /R | python "reducer-4-make-recommendation.py" > "stage-4-out.txt"
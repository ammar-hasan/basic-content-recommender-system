# بسم اللہ الرحمن الرحیم

## Basic Recommender System
This repository contains a Basic Product Recommender Systen to be used with native and AWS EMR Hadoop. It's actually a collection of mapper and reducer files to be run on different stages in Hadoop or Amazon's AWS Elastic MapReduce.

This recommendation engine is based on Similarity matching (cosine similarity) algorithm.

## Datasource
The data used for this engine is from [MovieLens](https://grouplens.org/datasets/movielens/), I am using small data-set from MovieLens to include in GitHub Repo, but this program also works with the larger data-set from MovieLens. The data provided by MovieLens contains 4 CSV files

1. [links.csv](data/links.csv): Provides relational data of Movie IDs against IMDB links
2. [movies.csv](data/movies.csv): Provides the details about all movies
3. [ratings.csv](data/ratings.csv): Provides relational data of Movie IDs against individual ratings
4. [tags.csv](data/tags.csv): Provides relational data of Movie IDs against tags added by users per movie

## Description
The workflow is broken in 4 stages (or 4 MapReduce Jobs) to allow more flexibility and control in making recommendations.

### Stage-1: Calculating Average User Ratings
Because User Ratings are essential part in recommending a movie, so prior to further processing, average user ratings are needed, therefore we calculate average rating and total ratings number per movie id and store the interim result in [output](output)/stage-1-out.txt file.

### Stage-2: Joining Average Ratings with Movies
After Stage-1, we join Average Ratings with the Movies listing itself provided in movies.csv. This is needed because we need to be able to relate a movie alongwith its average ratings and total number of ratings. Interim output is stored in [output](output)/stage-2-out.txt file.

### Stage-3: Preparing list of Recommended Movies
Now since upto this step we have all the required data in our desired format, in this stage we perform the actual recommendation algorithm, based on Cosine Similarity. Here we consider Genre, Average Rating and Total Ratings as features or driving factors to calculate the similarity. This recommendation list is calculated against a Movie ID, and can be limited to output only few movies as recommendations. Interim output is stored in [output](output)/stage-3-out.txt file.

### Stage-4: Makes Recommendation
Finally, we do reverse sorting over the recommended list, and recommend the top matches only, upto 12 recommendations. Final output is stored in [output](output)/final-out.txt file.

## License
MIT

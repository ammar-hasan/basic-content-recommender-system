#!/bin/bash
echo "Current working directory is ${PWD}";

echo "Clearing '/reco' old folder in HDFS.";
hadoop fs -rm -r -f /reco;

echo "Creating a fresh '/reco' folder in HDFS.";
hadoop fs -mkdir /reco; 

echo "Copying 'data' folder to '/reco/data' in HDFS.";
hadoop fs -copyFromLocal $PWD/data /reco/data;

echo "Creating the output folder '/reco/output' in HDFS to store results.";
hadoop fs -mkdir /reco/output;

HDJAR_PATH='/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar';
echo "Hadoop Streaming Jar => $HDJAR_PATH";

echo "Executing stage-1 (Calculating average ratings), result will go to /reco/output/stage-1 in HDFS.";
hadoop jar $HDJAR_PATH \
 -mapper $PWD/stage-1/mapper-1-average-ratings.py \
 -reducer $PWD/stage-1/reducer-1-average-ratings.py \
 -input /reco/data/ratings.csv \
 -output /reco/output/stage-1 \
;

echo "Executing stage-2 (Joining movies with ratings), result will go to /reco/output/stage-2 in HDFS.";
hadoop jar $HDJAR_PATH \
 -mapper $PWD/stage-2/mapper-2-join-ratings.py \
 -reducer $PWD/stage-2/reducer-2-join-ratings.py \
 -input /reco/data/movies.csv \
 -input /reco/output/stage-1 \
 -output /reco/output/stage-2 \
;

echo "Executing stage-3 (Calculating recommendations), result will go to /reco/output/stage-3 in HDFS.";
hadoop jar $HDJAR_PATH \
 -mapper $PWD/stage-3/mapper-3-recommend-movie.py \
 -reducer $PWD/stage-3/reducer-3-recommend-movie.py \
 -input /reco/output/stage-2 \
 -output /reco/output/stage-3 \
;

echo "Executing stage-4 (Final Stage: Make recommendations), result will go to /reco/output/stage-4 in HDFS.";
hadoop jar $HDJAR_PATH \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keycomparator.options=-k1,1r \
 -mapper $PWD/stage-4/mapper-4-make-recommendation.py \
 -reducer $PWD/stage-4/reducer-4-make-recommendation.py \
 -input /reco/output/stage-3 \
 -output /reco/output/stage-4 \
;

echo "Downloading the output file from HDFS to $PWD/output/recos.csv";
rm -f $PWD/output/recos.csv;
hadoop fs -getmerge /reco/output/stage-4 $PWD/output/recos.csv;

echo "Program has finished execution.";
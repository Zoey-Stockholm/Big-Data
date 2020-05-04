# LDSA Assignment

The A2/mapreduce_tweets directory is for analyzing twitter data using Hadoop streaming and Python.


While Hadoop/MapReduce is based on Java, it is not necessary to use Java to write your mapper and reducers. 
The Hadoop framework provides the “Streaming API”, which lets you use any command line executable that reads
from ​standard input​ and writes to standard output​ as the mapper or reducer. The following tutorial, although 
a bit old, provides an excellent introductory example to using Python and Hadoop streaming:
http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

It is done based on the tutorial above.
Info:
Platform: Ubuntu linux
Hadoop is install in 'usr/local/hadoop'.

Word Count Example:
wget http://www.gutenberg.org/ebooks/20417.txt.utf-8
Tutorial:
https://mapr.com/docs/61/ReferenceGuide/hadoop-jar.html
First letter Count in HDFS:
1.configuration and setup:
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation
2.stage the file in HDFS:
/usr/local/hadoop/bin/hdfs dfs -put /home/ubuntu/wordcount/input
3.run the job
/usr/local/hadoop/bin/hadoop jar wordcount.jar WordCount input <output_dir>
4. check the result
/usr/local/hadoop/bin/hdfs dfs -ls <output_dir>


Aalyzing twitter data using Hadoop streaming and Python

Use the command to make it run using MapReduce.

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files /home/ubuntu/tweets/tweets/mapper1.py,/home/ubuntu/tweets/tweets/reducer.py -input input -output output10 -mapper /home/ubuntu/tweets/tweets/mapper1.py -reducer /home/ubuntu/tweets/tweets/reducer.py

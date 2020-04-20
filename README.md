# LDSA Assignment

The A2 directory is for analyzing twitter data using Hadoop streaming and Python.

While Hadoop/MapReduce is based on Java, it is not necessary to use Java to write your mapper and reducers. 
The Hadoop framework provides the “Streaming API”, which lets you use any command line executable that reads
from ​standard input​ and writes to standard output​ as the mapper or reducer. The following tutorial, although 
a bit old, provides an excellent introductory example to using Python and Hadoop streaming:
http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

It is done based on the tutorial above.

Use the command to make it run as MapReduce.

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files /home/ubuntu/tweets/tweets/mapper1.py,/home/ubuntu/tweets/tweets/reducer.py -input input -output output10 -mapper /home/ubuntu/tweets/tweets/mapper1.py -reducer /home/ubuntu/tweets/tweets/reducer.py

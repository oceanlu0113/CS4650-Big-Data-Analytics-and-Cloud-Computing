from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("wordCt")
sc = SparkContext(conf=conf)

rdd = sc.textFile("Complete_Shakespeare.txt")		#read in data sets to RDD
rdd.count()     				#number of lines
words = rdd.flatMap(lambda x: x.split() )	#word split
words.count()   				#number of total words
words.distinct().count()    			#number of distinct words
word_counts = words.map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)  #create an rdd of tuples #reduce tuples by word
result = word_counts.map(lambda x: (x[1], x[0])).sortByKey(False)	  #swap key and value #sort by key, descending
#now the result contains a list of (count, word) tuples
#where count is the frequency of a word with most frequent word on top
result.saveAsTextFile("Output")   	            #save to Output directory

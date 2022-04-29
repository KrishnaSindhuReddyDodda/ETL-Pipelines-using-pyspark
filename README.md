# ETL pipeline flow
                        Text file         Extract         Pyspark on                            Load          Postgresql Database
                         in DBFS    =================>    Databricks notebook            ===================>   in AWS RDS
                                                          to perform some transformations
                                                  
1) Initially I created a cluster in Databrick and uploaded WordData.txt file into DBFS in databrick FileStore.
2) Now I created a notepad and named **First Spark code**; now read this file in the notebook => This is how the data extraction is performed here from text file to    spark.
3) Now in pyspark, I did few transformations for counting the words in the WordData text file => This is the transformation in pyspark.
4) Later in AWS RDS, I created a postgresql database and added 2 in-bound rules to allow traffic from pgAdmin. 
5) I downloaded jdbc driver in my PC, and created a connection between pgAdmin and AWS RDS using database endpoints.
6) Now created a schema in postgresql and executed a load command in pyspark and then executed a select * from wordcount; in pgAdmin to load the data from databrick to pgAdmin through AWS RDS.

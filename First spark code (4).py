# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, explode
import pyspark.sql.functions as f

# COMMAND ----------

# Extract

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()
WordDataDF = spark.read.text("/FileStore/tables/WordData.txt")
display(WordDataDF)

# COMMAND ----------

# Transformation

DF1 = WordDataDF.withColumn("Splitted Data", f.split("value", " "))
DF2 = DF1.withColumn("Words",explode("Splitted Data"))
Word_DF2 = DF2.select("Words")
WordCount = Word_DF2.groupBy("Words").count()
display(WordCount)

# COMMAND ----------

#Load

driver = "org.postgresql.Driver"
url="jdbc:postgresql://database-1.ctohhpvxjxxw.us-east-2.rds.amazonaws.com/"
table = "RDS_pyspark.WordCount"
user = "postgres"
password = "Jaisriram143$"


WordCount.write.format("jdbc").option("driver" , driver).option("url",url).option("dbtable",table).option("mode", "append").option("user",user).option("password",password).save()

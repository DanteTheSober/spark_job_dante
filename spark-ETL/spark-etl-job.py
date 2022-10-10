

import os

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, filter, when


def main():
    """Main ETL script definition.

    :return: None
    """

    # start Spark application and get Spark session
    print(os.getcwd() + "\\jars\\postgresql-42.4.0.jar")
    spark = (
        SparkSession.builder.config("spark.jars", os.getcwd() + "\\jars\\postgresql-42.4.0.jar")
            .master("local")
            .appName("PySpark_Postgres")
            .getOrCreate()
    )
    
    # execute ETL pipeline
    data = extract_data(spark)
    data_transformed = transform_data(data)
    load_data(data_transformed)


    spark.stop()
    return None


def extract_data(spark):
    """Load data from postgresql database.

    :param spark: Spark session object.
    :return: Spark DataFrame.
    """
    df = (
        spark.read.format("jdbc")
        .option("url", "jdbc:postgresql://localhost:5432/sensor_data")
        .option("driver", "org.postgresql.Driver")
        .option("dbtable", "sensor_data") \
        .option("user", "root")
        .option("password", "root")
        .load()
    )

    return df


def transform_data(df):
    """Transform original dataset.

    :param df: Input DataFrame.
    :return: Transformed DataFrame.
    """
    df_transformed = (
        df
        # scale temperature
        .withColumn("reading",when((col("sensor_type") == "temperature"), col("reading")/100) 
                             .otherwise(col("reading")))
        
        # filter out error humidity record
        .withColumn("reading", when((col("sensor_type") == "humidity") & (col("reading") < 0), None) \
                            .when((col("sensor_type") == "humidity") & (col("reading") > 100), None)
                            .otherwise(col("reading"))) 
        .filter(~col("reading").isNull())
        
        # calculating dew point
        .withColumn("dewpoint", 25 - ((100 - col("reading"))/ 5))
    )

    return df_transformed


def load_data(df):
    """Collect data locally and write to CSV.

    :param df: DataFrame to print.
    :return: None
    """
    (df
     .write.option("header", True)
     .csv("./result.csv")
    )
    return None



# entry point for PySpark ETL application
if __name__ == '__main__':
    main()

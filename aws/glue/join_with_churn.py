import sys

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from features.join_with_churn import spark_job

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'dt',
    'input_subscription',
    'input_performance',
    'input_activity',
    'output_path'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

spark_job.run(spark, args)

job.commit()

import boto3

s3 = boto3.resource("s3", aws_access_key_id="xx", aws_secret_access_key="xx", region_name="us-east-1")

for bucket in s3.buckets.all():
    print(bucket.name)

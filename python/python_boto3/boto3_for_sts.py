import boto3

sts = boto3.client("sts", aws_access_key_id="xx", aws_secret_access_key="xx", region_name="us-east-1")

print(sts.get_caller_identity())

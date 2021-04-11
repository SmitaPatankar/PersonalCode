import boto3

sts = boto3.client("sts", aws_access_key_id="xx", aws_secret_access_key="xx", region_name="us-east-1")

print(sts.get_caller_identity())
# {
#   'UserId': 'abcdef',
#   'Account': '123456',
#   'Arn': 'arn:aws:iam::123456:user/cloud_user',
#   'ResponseMetadata': {
#       'RequestId': 'f7e99de7-177b-4c0a-b567-6012a373a56d',
#       'HTTPStatusCode': 200,
#       'HTTPHeaders': {
#           'x-amzn-requestid': 'f7e99de7-177b-4c0a-b567-6012a373a56d',
#           'content-type': 'text/xml',
#           'content-length': '407',
#           'date': 'Sat, 30 May 2020 10:21:58 GMT'
#       },
#       'RetryAttempts': 0}}

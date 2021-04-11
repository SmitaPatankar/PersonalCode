import boto3

sqs = boto3.resource(service_name="sqs", region_name="us-east-1", aws_access_key_id="{aws_access_key_id}", aws_secret_access_key="{aws_secret_access+key}")
queue = sqs.get_queue_by_name(QueueName="{queuename}")

# estimate before polling
approx_msgs = queue.attributes.get("ApproximateNumberOfMessages")

# poll if msgs are estimated
msgs = queue.receive_messages(QueueUrl="https://sqs.us-east-1.amazonaws.com/{accountid}/{queuename}", MessageAttributeNames=["All"], WaitTimeSeconds=20, MaxNumberOfMessages=10)

# process as needed

# put msg back to queue if needed
for msg in msgs:
    msg.change_visibility(VisibilityTimeout=0)

# delete msgs if done
entries = [{"Id": msg.message_id, "ReceiptHandle": msg.receipt_handle} for msg in msgs]
sqs_resp = queue.delete_messages(Entries=entries)

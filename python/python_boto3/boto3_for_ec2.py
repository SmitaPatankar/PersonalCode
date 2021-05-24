import boto3

###################################################################################

ec2_client = boto3.client("ec2", aws_access_key_id="xx", aws_secret_access_key="xx", region_name="us-east-1")
print(ec2_client.run_instances(ImageId="ami-09d95fab7fff3776c", InstanceType="t2.micro", SubnetId="subnet-017e12e5dec40a0f7", KeyName="smitakeypair", MinCount=1, MaxCount=1))

account_id = "12345"
response = ec2_client.describe_snapshots(OwnerIds=[account_id])
snapshots = response["Snapshots"]
snapshots.sort(key=lambda x: x["StartTime"])
snapshots = snapshots[:-2]
for snapshot in snapshots:
    id = snapshot["SnapshotId"]
    try:
        ec2_client.delete_snapshot(SnapshotId=id)
        print("Deleted Snapshot:", id)
    except Exception as e:
        if "InvalidSnapshot.InUse" in e.message:
            print("Snapshot {} in use, skipping.".format(id))
            continue

###################################################################################

ec2_resource = boto3.resource("ec2", region_name="us-east-1", aws_access_key_id="xx", aws_secret_access_key="xx")
instances = ec2_resource.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
for i in instances:
    i.stop()
    print("Stopped instance {}".format(i.id))

instances = ec2_resource.instances.filter(Filters=[{"Name": "tag:backup", "Values": ["true"]}])
for i in instances.all():
    for v in i.volumes.all():
        desc = "Creating backup of {0}, volume {1}".format(i.id, v.id)
        print(desc)
        snapshot = v.create_snapshot(Description=desc)
        print("Created snapshot:", snapshot.id)

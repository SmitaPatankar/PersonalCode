import boto3

ec2_client = boto3.client("ec2", aws_access_key_id="xx", aws_secret_access_key="xx", region_name="us-east-1")
ec2_resource = boto3.resource("ec2", region_name="us-east-1", aws_access_key_id="xx", aws_secret_access_key="xx")

print(ec2_client.run_instances(ImageId="ami-09d95fab7fff3776c", InstanceType="t2.micro", SubnetId="subnet-017e12e5dec40a0f7", KeyName="smitakeypair", MinCount=1, MaxCount=1))
# {
#   "Groups": [],
#   "Instances": [
#     {
#       "AmiLaunchIndex": 0,
#       "ImageId": "ami-09d95fab7fff3776c",
#       "InstanceId": "i-0d620bfa73b0ebda3",
#       "InstanceType": "t2.micro",
#       "KeyName": "smitakeypair",
#       "LaunchTime": datetime.datetime(2020, 5, 30, 11, 20, 36, tzinfo=tzutc()),
#       "Monitoring": {
#         "State": "disabled"
#       },
#       "Placement": {
#         "AvailabilityZone": "us-east-1b",
#         "GroupName": "",
#         "Tenancy": "default"
#       },
#       "PrivateDnsName": "ip-172-31-95-254.ec2.internal",
#       "PrivateIpAddress": "172.31.95.254",
#       "ProductCodes": [],
#       "PublicDnsName": "",
#       "State": {
#         "Code": 0,
#         "Name": "pending"
#       },
#       "StateTransitionReason": "",
#       "SubnetId": "subnet-017e12e5dec40a0f7",
#       "VpcId": "vpc-0309b3faca89bd46e",
#       "Architecture": "x86_64",
#       "BlockDeviceMappings": [],
#       "ClientToken": "",
#       "EbsOptimized": false,
#       "Hypervisor": "xen",
#       "NetworkInterfaces": [
#         {
#           "Attachment": {
#             "AttachTime": datetime.datetime(2020, 5, 30, 11, 20, 36, tzinfo=tzutc()),
#             "AttachmentId": "eni-attach-01b8ed0f0256898a6",
#             "DeleteOnTermination": true,
#             "DeviceIndex": 0,
#             "Status": "attaching"
#           },
#           "Description": "",
#           "Groups": [
#             {
#               "GroupName": "default",
#               "GroupId": "sg-017e0cb1051671923"
#             }
#           ],
#           "Ipv6Addresses": [],
#           "MacAddress": "12:b3:88:9b:30:95",
#           "NetworkInterfaceId": "eni-02d2a357d65025e1c",
#           "OwnerId": "037291448658",
#           "PrivateDnsName": "ip-172-31-95-254.ec2.internal",
#           "PrivateIpAddress": "172.31.95.254",
#           "PrivateIpAddresses": [
#             {
#               "Primary": true,
#               "PrivateDnsName": "ip-172-31-95-254.ec2.internal",
#               "PrivateIpAddress": "172.31.95.254"
#             }
#           ],
#           "SourceDestCheck": true,
#           "Status": "in-use",
#           "SubnetId": "subnet-017e12e5dec40a0f7",
#           "VpcId": "vpc-0309b3faca89bd46e",
#           "InterfaceType": "interface"
#         }
#       ],
#       "RootDeviceName": "/dev/xvda",
#       "RootDeviceType": "ebs",
#       "SecurityGroups": [
#         {
#           "GroupName": "default",
#           "GroupId": "sg-017e0cb1051671923"
#         }
#       ],
#       "SourceDestCheck": true,
#       "StateReason": {
#         "Code": "pending",
#         "Message": "pending"
#       },
#       "VirtualizationType": "hvm",
#       "CpuOptions": {
#         "CoreCount": 1,
#         "ThreadsPerCore": 1
#       },
#       "CapacityReservationSpecification": {
#         "CapacityReservationPreference": "open"
#       },
#       "MetadataOptions": {
#         "State": "pending",
#         "HttpTokens": "optional",
#         "HttpPutResponseHopLimit": 1,
#         "HttpEndpoint": "enabled"
#       }
#     }
#   ],
#   "OwnerId": "037291448658",
#   "ReservationId": "r-0b431d8299e2a412f",
#   "ResponseMetadata": {
#     "RequestId": "0267ea8f-c966-4273-bb81-d286eece68d2",
#     "HTTPStatusCode": 200,
#     "HTTPHeaders": {
#       "x-amzn-requestid": "0267ea8f-c966-4273-bb81-d286eece68d2",
#       "content-type": "text/xml;charset=UTF-8",
#       "content-length": "4761",
#       "vary": "accept-encoding",
#       "date": "Sat, 30 May 2020 11:20:36 GMT",
#       "server": "AmazonEC2"
#     },
#     "RetryAttempts": 0
#   }
# }

print([region["RegionName"] for region in ec2_client.describe_regions()["Regions"]])
# ["us-east-1", "us-west-1"]

instances = ec2_resource.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
for i in instances:
    i.stop()
    print("Stopped instance {}".format(i.id))
    # Stopped instance i-02a0c88c6012f42b0

instances = ec2_resource.instances.filter(Filters=[{"Name": "tag:backup", "Values": ["true"]}])
for i in instances.all():
    for v in i.volumes.all():
        desc = "Creating backup of {0}, volume {1}".format(i.id, v.id)
        print(desc)
        # Creating backup of i-05b2b9829b5155d74, volume vol-03d9357160cd83e9f
        snapshot = v.create_snapshot(Description=desc)
        print("Created snapshot:", snapshot.id)
        # Created snapshot: snap-03f4eb057e4c1e48d

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
        # Deleted Snapshot: snap-03f4eb057e4c1e48d
    except Exception as e:
        if "InvalidSnapshot.InUse" in e.message:
            print("Snapshot {} in use, skipping.".format(id))
            continue

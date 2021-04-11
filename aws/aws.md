# IAM

## IAM - root user

- global
- set password
- set MFA
- do not set keys
- handle users and their sigin
- handle groups, users, roles and their policies
- arn:partition:service:region:accountid:resource or resource_type/resource or resource_type/resource/qualifier or resource_type/resource:qualifier or resource_type:resource  or resource_type:resouce:qualifier  

## IAM - roles
- for resources to access other resources

## IAM - policies (attach to user/group/role)

can have conditions also

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:Get*", "s3:List*"],
            "Resource": "*",
            "Sid": "mypolicy"
        }
    ]
}
```

### IAM - policies - AWS managed (can change)
- admin(everything but billing)
- power (everything but IAM)
- readonly
- s3admin
- dynamodbadmin
- dynamodbreadonly

### IAM - policies - Customer managed (in our account)

### IAM - policies - Inline

## IAM - credential report

- all users' pwd, keys, MFA

# Organizations

- Organization has OUs with service control policies
- OUs have accounts
- consolidated handling and billing

# S3

## S3 - Miscellaneous

- cross region replication is possible
- using cloudfront with custom/specific certs is possible
- pre-signed urls are possible
- only flat files like videos, images etc
- object storage i.e. not something that changes
- universal name space
- file upto 5 TB
- key is name and value is data
- updation/deletion takes some time
- standard, IA, one zone IA, intelligent tiering, glacier(mins to hours for retrieval), glacier deep archive(12 hrs for retrieval)
- transfer acceleration using cloudfront and internal n/w
- can host static websites
- has versioning
- encryption
- MFA delete
- lifecycle management
- object lock
- prefix i.e. folders
- multipart uploads
- byte range fetches
- can be shared in accounts

## s3 - select
- fetch partial data using sql queries

## S3 - bucket policies

- useful for cross account access
- useful when IAM policies bump up

```
{
    "Id": "Policy1234"
    "Version": "2012-10-17"
    "Statement": [
    {
        "Sid": "Stm6767",
        "Resource": "arn:aws:s3:::mybucketname/*",
        "Action": ["s3:DeleteObject"],
        "Effect": "Allow",
        "Principal": ["arn:aws:iam::myaccountid:user/myuser"]
    }]
}
```
```
{
    "Id": "Policy1234"
    "Version": "2012-10-17"
    "Statement": [
    {
        "Sid": "Stm6767",
        "Resource": "arn:aws:s3:::mybucketname/*",
        "Action": ["s3:*"],
        "Effect": "deny",
        "Principal" "AWS": "*",
        "Condition": {
            "Bool": {
                "aws:SecureTransport": false
                    }
                }
        }
    ]
}
```

## S3 - object ACLs

- useful when bucket permission also gets full

## S3 - Glacier vault lock policy (cannot be changed/deleted)

- WORM, data retention etc

# CloudTrail (specific services)

- records API calls for account in s3
- near real time (not exactly)
- can send sns notification
- hourly hashes are created to check validity
- SSE-S3/SSE-KMS can be used
- IAM policies to prevent deletion
- s3 lifecycle management
- cache cleaning is chargeable

# Cloudwatch

## Cloudwatch - main

- monitor resources - utilization, performance
- real time can be enabled
- can raise SNS notifications
- can monitor on prem resources also
- raises alarms based on metrics
- recipient needs to subscribe from mail

## CloudWatch - logs

- pushed from ec2 with the help of agent, cloudtrail etc into log group

## Cloudwatch - events

- near real time
- between event and event target

## Cloudwatch - metrics

- for alarms

# Config

- audits and fixes config of resources
- can send sns notifications
- region/organization/account level
- uses service linked role

# Secure token service / web identity federation

- for access via AD, fb, google, diff account
- STS:AssumeRoleWithWebIdentity (fb)
- STS:AssumeRoleWithSAML (ad)
- STS:AssumeRole (aws)

# Cognito user pool

- for indirect access to AWS services

# Hardware security model

- dedicated h/w for encryption
- symmetric/asymmetric keys

# Inspector
- assessment inside EC2 via agent on AMI

# Trusted advisor

- for best practices
- full for business and enterprise users only
- rest all have basic

# VPC

## VPC - flow logs

- traffic for vpc/subnet/ENI
- instance to dns is not monitored
- windows license auth is not monitored
- instance metadata is not monitored
- DHCP is not monitored
- reserved IP address on default vpc router is not monitored
- uses cloudwatch/s3

## VPC - main

- virtual data center in cloud
- can create h/w vpn between our corporate n/w and vpc
- internet gateway/virtual private gateway - router - route table(subnet association) - nacl - public/private subnet - sec group - instance
- NACL is separate for inbound and outbound unlike sec groups
- NACLs can block, sec groups cant
- soft limit of 5 VPCs per region
- 1 subnet = 1 AZ (public and private subnet)
- shared/dedicated h/w

- CIDR /16 largest in aws i.e. 65536
- CIDR /28 smallest in aws i.e. 16

- can peer one vpc with another via direct network using private ip address
- can peer vpc across accounts also and across regions also
- no transitive peering

- default vpc in every region
- default vpc has subnet for each AZ, default route table and internet gateway
- all subnets in default vpc have route out to internet
- ec2 has public and private ip address in default vpc

- on creation of vpc with cidr range, default route table is created, nacl is created, default sec group is created, igw is not created, subnets are not created
- create subnet on AZ and sub cidr
- AZs with same names are diff in diff a/cs
- .0,.1,.2,.3 and .255 - n/w address, router, dns, future use, n/w broadcast(not supported) address
- create igw on vpc

- main route table is for communication between subnets
- by default new subnet is in main route table
- hence create new subnet for internet access

- can use hardware vpn between datacenter and vpc

- interney gateway -> router -> route table -> NACL(stateless - allow/deny - can work on specific IP address) -> public subnet -> sec group(stateful) -> instance  
- virtual private gateway -> router -> route table -> NACL(stateless - allow/deny - can work on specific IP address) -> private subnet -> sec group(stateful) -> instance

## VPC - endpoints

- via private network
- via ENI

## VPC - private link
- make services from one vpc available to another

# DNS
- for name resolution

# Transit Gateway
- between vpcs and data center
- better than VPN and vpc peering
- doesnt use internet
- encrypted

# NAT gateway

- public to private instance
- make in each AZ
- automatic failover
- NAT AMI, public subnet, public sec group, volume, kp
- private subnet -nat gateway - public subnet - internet gateway
- no sec group

# NAT instance

- use as bastion host as NAT gateway doesnt support it

# NACL

- default NACL allows all traffic in and out by default
- subnet can have one NACL only
- rule numbers in increments of 100
- our own NACL denies everything by default
- deny on top sequentially

# Network load balancer

- for performance

# Application load balancer

- for http requests
- port, vpc, all AZs
- can add to target group name for our instances
- healthcheck
- dns name

# KMS

## KMS - main

- for encryption keys
- regional
- key admin and key users
- if key is lost, data is gone
- cannot be autorotated/exported
- key deletion takes 7 days
- symmetric(others), asymmetric(ec2)

## KMS - customer managed

- can be used across accounts

## KMS - customer managed with key material

- for compliance reason

## KMS - key rotation options

- aws managed - in 3 yrs - old key is intact for older data - cant delete
- customer managed - on demand/enable for 1 year - update older data to use new one
- customer managed with imported material - on demand - update resource to use new - delete old

## KMS - Grants

- temporary access for operation via token

# Marketplace

- for images like splunk, fw etc

# WAF

- monitors http and https requests to cloudfront, ALB and API gateway
- controls IPs, query string parameters, country, header, length, sql presence, cross site scripting etc
- allow/block/count
- for layer 7 attacks

# Shield

- standard - n/w, ddos protection
- advanced - ddos mitigation, monitoring, cost protection, history, support
- protection on ELB, cloudfront and route53, ec2, global accelerator
- for layer 3 and 4 attacks

# dedicated instances

- instances on vpc meant for our own account

# dedicated host

- deploy on specific host for compliance

# ECS/EKS

- runs containers
- platform managed by aws
- fargate for serverless
- cluster - service - task - container
- use ecs interface emdpoint to avoid sending traffic on internet
- use tls encryption

# session manager
- for ec2
- logs in cloudtrail and cloudwatch

# cloudfront
- edge locations for caching i.e. content delivery network
- for laws, latency
- georestriction
- whitelist/blocklist
- origin access identity for s3
- cached until TTL
- use cloudfront domain name on browser
- has signed urls or cookies
- has caching

# Certificate manager

- for route53, cloudfront, ALB
- automatic renewal
- cannot export certs

# API Gateway

- has throttling and caching for TTL
- for loose coupling
- doorway to aws
- versioned
- https with ACM

# Parameter store

- string/secure string/list
- mainly for license codes, param values, config data
- caching
- versioned

# Systems manager

- manage fleet of instances via agent on instance

# Athena

- query s3,cloudtrail,elb logs etc using sql
- csv, json etc
- serverless
- db table gets created which can be queried

# MAcie

- uses ML and MLP to protect sensitive information in s3
- has service role for s3 and cloudtrail

# GuardDuty

- uses ML for threat detection
- alerts go on guardduty console and cloudwatch
- response can be automated
- takes few days to set baseline

# secrets manager

- automatically rotates(first time also)
- app can make api call to secrets manager

# simple email service

- send mail from app

# security hub

- central hub for security alert for aws services
- automatic audit for accounts
- has dashboard
- integrated with other tools

# network packet inspection

- inspect header and content and take action

# artifacts

- NDA signing

# lambda

- event driven
- has function policy for invocation
- has execution role for accessing resources  
```
def lambda_handler(event, context):  
   print("here")    
   return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": "Smita"}  
```

# ec2

## ec2 - main

- virtual server in cloud
- on demand, reserved(standard,convertible,scheduled), spot, dedicated hosts(reserved/on demand)
- AMI, instance type, network, subnet, ebs, tags, sec group(stateful) - linux ssh port 22, windows RDP 3389, http 80, https 443, key pair
- bootstrap script

# ec2 - hibernate
- volume stays, RAM to EBS
- faster than reboot
- instance id remains same
- root volume must be encrypted
- not more than 60 days
- for on demand and reserved instances

# ec2 - placement groups
- clustered - single AZ
- spread - opp - distinct h/w racks n/ws powers - critical  - diff AZs in region   
- partitioned - multiple instances in a partition  and multiple partitions  - each partition in own rack  - diff AZs in region  

# ebs
- virtual hard disk used by ec2
- block storage i.e. can have db, os etc
- volumes for ec2
- volume and ec2 must be in same az
- volume is replicaed across AZ
- ssd(provisioned/general purpose IOPS), magnetic(throught put optimized, cold HDD)
- can create snapshot
- can be encrypted

# command line
- aws configure (access key, secret key, region, data format)
- aws s3 ls

# RDS
- OLTP
- sql server, oracle, mysqlserver(opensource), postgresql(opensource), amazon aurora(6 copies in 3 azs, serverless, auotosacling, ss), mariadb
- multi az
- read replicas(upto 5 copies)
- username, password
- db instance class - standard/memory optimized/burstable
- storage - provisioned iops/general purpose ssd  
- auto scaling
- vpc
- security group
- automatic failover
- automated backups as snapshots in s3
- encrypted at rest

# DynamoDB
- NoSQL
- non relational
- kv pairs
- columns can vary in records
- across 3 data centers
- serverless
- on demand capacity available
- can backup
- point in time recovery available
- streams available
- migration service available (homeogenous automated schema conversion, heterogenous manual schema conversion)
- kms, site to site vpn, direct connect

# DAX
- deynamodb accelerator
- in memory cache

# redshift
- data warehousing
- business intelligence
- OLAP
- backups
- secure

# elastic cache
- retrieve data for common queries from in memory cache instead of disk space
- memcached, redis(advanced,multiaz,backups,advanceddatatype) engine

# autoscaling
- using ec2 snapshot
- vpc, all AZs, healthcheck on lb
- using template and launch conf
- test using stress tools
- lifecycle hooks to wait until instance is properly configured

# route53
- dns
- target eg: s3 bucket
- ttl for caching
- cName, alias
- simple, weighted, latency based, failover, geolocation, geoproximity for traffic flow, multivalue answer routing

# elastic beanstalk
- automated deployment of apps

# cloudformation
- infrastructure as code
- create stack from template
- give variable values

# sqs
- for asynchronous integration
- between 2 components
- stores msgs
- fail safe
- pull based
- retention period
- std and fifo queue
- short and long polling

# Neptune
- graph db

# snowball
- load data from on prem to s3

# snowball edge
- deploy lambda functions on prem

# storage gateway
- on prem caching to s3

# codedeploy
- to ec2/on prem

# opsworks
- chef for onprem/ec2 deploy

# iot greengrass
- connect deviced to cloud

# billing dashboard
- to create budget

# budget
- alert before exceeding

# cost explorer
- after cost is incurred

# support plans
- basic
- developer
- business
-enterprise

# resource groups
- as per tags

# quickstart
- deploy already designed solutions

# landing zone    
multi account aws env  - creates 4 accounts  - org account, shared services account, sec account, log archive account    

# cost calculator
- for monthly cost

# aws data sync
- move large data in aws

# ENI
- elastic n/w interface
- virtual network card for management interface etc

# EFA
- elastic fabric adaptor
- n/w device for high computing apps

# EN
- enhanced networking - SRIOV - ENA adapter/virtual function

# spot fleet
- combination of spot and on demand instances

# EFS
- instance cant share volumes but can share EFS
- AZs, sec group, vpc, encryption , lifecycle
- install amazon-efs-utils in ec2

# Amazon FSx
- for windows for AD, MS Apps etc
- for lustre for ML

# EMR
- elastic map reduce
- big data

# AWS directory service
- connects aws resources with onprem AD
- provides DCs
- can extend existing onprem AD to AWS

# Resource Access Manager
- share between accounts
- ec2, aurora, route53

# single sign on
- use corporate identity for aws

# bastion
- between internet and private host
- bastion AMI

# direct connect
- dedicated n/w connection from onprem to aws
- encryption
- using along with aws vpn

# global accelerator
- uses optimal endpoints

# VPN cloud hub
- users can connect to single VPGW  
- communication over vpn  
- customer on one site can talk to other site  

# SMS
- server migration

# AWS app discovery
- plan migration

# simple workflow service
- coordinate distributed tasks
- combines digital and manual tasks

# SNS
- simple notification service
- services can also subscribe to topics

# elastic transcoder
- change format of media files

# kinesis
- load streaming data and build custom apps

# HSM
- dedicated h/w for managing our own keys

# AWS X-Ray
- debug serverless apps

# serverless application model
- for building serverless apps

# ECS
- manage containerized apps
- cluster, task definition, container definition, task, service, regsitry

# ECR
- for container images

# fargate
- serverless engine for ecs and eks
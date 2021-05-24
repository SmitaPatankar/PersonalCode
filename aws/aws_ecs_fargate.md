# task definition  
image, cpu, memory  
immutable and versioned  
upto 10 container definitions  
on same host  
```  
{  
    "family": "scorekeep",  
    "cpu": "1 vCpu",  
    "memory": "2 gb",  
    "networkMode": "awsvpc",  
    "taskRoleArn": "xx",  
    "executionRoleArn": "xx",  
    "requiresCompatibilities": ["FARGATE"],  
    "containerDefinitions": [  
        {  
            "name": "scorekeep-frontend",  
            "image": "xx.dkr.ecr.us-east-1.amazonaws.com/fe",  
            "cpu": 256,  
            "memoryReservation": 512,  
            "portMappings": [  
                {"containerPort": 8080}  
            ],  
            "logConfiguration": {  
            "logDriver": "awslogs",  
            "options": {  
                "aws-logs-group": "scorekeep",  
                "aws-logs-region": "us-east-1",  
                "aws-logs-stream-prefix": "scorekeep/frontend"  
        }  
    }  
        },  
        {  
            "name": "scorekeep-api",  
            "image": "xx.dkr.ecr.us-east-1.amazonaws.com/api",  
            "cpu": 768,  
            "memoryReservation": 512  
            "portMappings": [  
                {"containerPort": 5000}  
            ],  
            "logConfiguration": {  
            "logDriver": "awslogs",  
            "options": {  
                "aws-logs-group": "scorekeep",  
                "aws-logs-region": "us-east-1",  
                "aws-logs-stream-prefix": "scorekeep/api"  
        }  
        },  
        "environment": [xx=xx]  
    ]  
}  
```  
  
# cluster  
iam permissions boundary  
isolation boundary for app  
  
# task  
running instantiation of task definition  
houses container  
fargate/ecs(ec2) mode  
  
# service  
maintain copies of task definition  
recover after death of task  
integrates with ELB  
  
# private architecture  
internet - internet gateway - vpc - public subnet with nat gw with public EIP - private subnet - eni with private ip - fargate task  
public rt - destination=private subnet target=local, destination=all, target=igw  
private rt - destination=private target=local, destination=all, target=igw  
out sec group - type=all traffic, port=all, destination=all  
  
# public architecture
internet - igw - public subnet - task - eni  
public rt - destination=private target=local, destination=all target=igw  
out sec group - type=all traffic, port=all, destination=all  
in sec group - type=http traffic, port=8080, source=all  
  
# load balancer  
IP of task in target group  
ALB or NLB  
  
# complete architecture  
internet - public subnet - ALB with public IP - private subnet - fargate task with private ENI  
lb sec grp - accept all traffic from internet on port 80  
task sec group - accept tcp traffic on port 8080 from alb sec grp  
lb and task in same az  
  
# storage  
layers or volume for sharing across containers  
volumes are also ephemeral  
else use db etc  
  
# permissions  
cluster - who can launch/describe tasks in cluster  
app - app to access other resources like db - task role  
housekeeping - for aws to do its tasks like cloudwatch, ecr etc - execution role(ecr,cloudwatch), ecs service linked role(eni,elb)(created at the time of cluster)  
  
# commands  
```
aws ecs register-task-definition --cli-input-json file:////xx.json  
aws ecs create-cluster --cluster-name xx  
  
aws ecs run-task --cluster xx --task-definition scorekeep:1 --launch-type FARGATE --count 1 --network-configuration "awsvpcConfiguration" = {  
    subnets = [subnet1-id],  
    securityGroups=[sg-id],  
}"   
  
aws ecs create-service --service-name xx --cluster xx --launch-type FARGATE --desired-count 5 --load-balancers  
--network-configuration "awsvpcConfiguration" = {  
    subnets = [subnet1-id],  
    securityGroups=[sg-id],  
}"  
[  
    {  
        "targetGroupArn": "xx",  
        "containerName": "scorekeep-frontend",  
        "containerPort": 8080  
    }  
]  
"  
```
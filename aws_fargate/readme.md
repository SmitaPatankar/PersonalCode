Just need to manage containerized app, not the EC2 instance, its OS, docker daemon, ecs agent.  
scalable  
integrated with aws features, aws features available on container level  
  
task definition  - image url, cpu and memory requirements  - networkmode - awsvpc
cluster - group ec2 instances  - isolation boundary  
task in cluster - running instantiation of task definition    
service in cluster - no of copies  - integrated with ELB  
  
task definition - immutable - can version  - upto 10 container definitions  - on same host  - name and image url  - cpu and memory  - common/per container sharing  
billing as per task level cpu and memory  
  
vpc  - launch task in subnet  
elastic network interface gets created which has a private IP  from subnet IP range  
this ip is attached to fargate task  
so our task has an IP now, it will use this to talk to other entities in VPC in private manner i.e. LB, EC2, DB etc  
there are also provisions for public ip to be accessible via internet  
sec groups are also supported  
  
aws ecs run-task -- task-definition myapp:1 --network-configuration "awsvpcconfiguration" = {subnets=[subnet1-id,subnet2-id],securityGroups=[sg-id]}"  
multiple subnets for across az  
  
ENI to pull image, push cloudwatch logs  - outbound internet access 
vpc will have internet gateway  
inside it has public subnet  - route table  Destination private ip of vpc target local, destination anything else 0.0.0.0/0 target internet gateway  
public subnet has NAT gateway - NAT has public IP and route traffic come from private IP to internet  
private subnet route table - Destination private ip of vpc target local, destination anything else 0.0.0.0/0 target nat gateway  
sec group - type all traffic - port all - destination 0.0.0.0/0  
  
when entire task is public  
vpc has public subnet only, route table private local, other internet gateway  - task in public subnet  - subnet will be public and assignPublicIp=ENABLED while running  
sec group - type all traffic - port all - destination 0.0.0.0/0  
sec group - type HTTP - port 8080 - source 0.0.0.0/0  

app lb with target groups  ip type  
task definition - port Mappings - "portMappings": {"containerPort": 8080 or 5000}   
app will listen on these ports    
  
containers in same host can talk to one another as localhost  
  
run as --load-balancers "[{"targetGroupArn": "<insert arn>", "containerName": "scorekeep-frontend", "containerPort": 8080}]"  
  
LB has public IP as it is internet facing  
LB and task should have subnets in same AZ else routing wont work  
LB sec group - type HTTP - port 80 - source 0.0.0.0/0  
task sec group - type custom TCP - port 8080 - source ALB security group  
  
storage  
layer storage - images are layers  
10GB layer storage for task  
writes are not visible across containers  
  
storage is ephemeral i.e. not available after task stops  
  
volume storage - containers to share same file system, - 4GB per task  - mount volumes  - not available after task stops  
  
cluster permissions  - who(users/roles) can launch/describe tasks  
app permissions - containers can access aws resources securely  
task housekeeping permissions - image pull, cloudwatch logs, eni creation, register/remove LB  
  
cluster permissions - {effect: allow, action: [ecs:runtask], condition: {arnequals: {ecs:cluster: cluster-arn}}, resource: ["task-def-family:*"]}  
eg: {effect: allow, action: [ecs:listtasks, ecs:describetasks], condition: {arnequals: {ecs:cluster: cluster-arn}}, resource: ["*"]}  
  
app permissions - aws creds to talk to other services like db, sns etc  
Task Role  - establish trust relationship with ecs-tasks.amazonaws.com  

task def - "taskRoleArn": "arn:aws...role/scorekeepRole"  
  
cli/sdk will use task role credentials  
  
housekeeping permissions  
execution role - image pull and cloudwatch logs  
iam role - ecr:GetAuthorizationToken ecr:BatchGetImage  or AmazonEC2ContainerRegistryReadOnly  
logs:CreateLogStream logs:PutLogEvents  or CloudWatchLogsFullAccess  
establish trust relationship with ecs-tasks.amazonaws.com  
task def - executionRoleArn: arn:aws...role/scorekeepExecutionRole    
  
ecs service linked role - eni mgmt, elb mgmt  
automatically  
immutable  
no need to pass  
  
logging  
stdout -> cloudwatch  
awslogs  driver  
log group in cloudwatch logs  
task def - "logConfiguration": {"logDriver": "awslogs", "options: {awslogs-group: scorekeep, awslogs-region: us-east-1, awslogs-stream-prefix: scorekeep/frontend}}
add permission via task execution role  
  
ecs console -> task -> logs  
  
cloudwatch stream  
cloudwatch metrics - cpu/memory  
  
task def - requiresCompatibilities: FARGATE  
  
run-task /create-service  

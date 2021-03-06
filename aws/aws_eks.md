# eks  
managed k8s cluster  
aws will manage master for us, install necessary apps in master like container runtime, kubernetes master processes, scaling, backups etc  
we can focus on deploying apps in k8s  
we have to create worker nodes  
  
# steps  
create aws acount  
create a vpc  
create IAM role with security group(permissions to operate on cluster) for user  
  
create cluster control plane i.e. master node with the role - details needed - name of cluster k8s version, region, security etc  
create worker nodes and connect them to cluster - nodes are EC2 instances with cpu and storage - create node group - select cluster - select sec group - select instance type of ec2 i.e. resources, auto scaling i.e. max and min no. of nodes  
connect to cluster from local machine for deploying app using kubectl via configuration for communicating with remote cluster  
  
# eksctl  
above process is complex hence thirdparty eksctl  
uses default values  
can be customized  
  
# steps  
install eksctl - https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html  
authenticate to aws  
```
sudo apt install awscli  
aws configure # access key id, secret access key, default region, default output format  
eksctl create cluster --name test-cluster --version 1.17 --region us-east-1 --nodegroup-name linux-nodes --node-type t2.micro --nodes 2  
```
kubeconfig is set automatically now for kubectl to connect with cluster  
```
eksctl delete cluster --name test-cluster  
```
container orchestrators - docker swarm, ECS, kubernetes, EKS, fargate  
ECS - control plane managed by aws  
kubernetes - manage control plane - cost - worker node  
EKS - aws manages controlplane - cost - for control plane and worker nodes  
Fargate - serverless - no need to create cluster - cost - not for controlplane and worker node - only for tasks  
  
ECS cluster - control plane managed by aws, ec2 instances managed by us - pay for ec2 - specific to aws - do not pay for control plane  
ECS + Fargate - hosting also will be managed by aws - pay for time and cpu  
EKS - manages kubernetes cluster - specific to kubernetes - on prem also - pay for control plane - create ec2 - connect using kubectl  
EKS + Fargate - worker nodes are also managed  
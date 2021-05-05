# EKS with fargate
## EKS
- control plane managed by aws
- you deploy pods on worker nodes i.e. ec2 which are managed by you or aws
- control plane will pick ec2, put pod on it and connect ec2 with vpc through ENI

## fargate
- aws manages control plane and worker node and attaches the worker ec2 to our vpc via ENI
- deploy pods on serverless
- fargate profile template with selectors, role, subnet etc
- if pod deployment via kubectl matches profile, prod gets deployed on fargate

### hands on
- install eksctl
https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html
- install kubectl
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux
- install awscli
sudo snap install aws-cli --classic
- configure aws
aws configure
enter access key
enter secret key
enter default region
enter default output format
- installl docker
sudo snap install docker
- install kubernetes
https://www.techrepublic.com/article/how-to-quickly-install-kubernetes-on-ubuntu/
(kubeadm join 172.31.30.195:6443 --token 2wwc6c.0vd94ymn79jafgrl --discovery-token-ca-cert-hash sha256:8fcda8b44493998f7317ee5a44f68494496338fad8f8ebbc8c0f2cd0f6c9733b)
- create fargate eks cluster
eksctl create cluster --zones us-east-1c,us-east-1b --name eksfargate --fargate
- get pods in cluster
kubectl gets pods -A
- get nodes in cluster
kubectl get nodes
- make kubernetes template
```
apiVersion: apps/v1
kind: Deployment
metadata:
    name: myweb
spec:
    selector:
        matchLabels:
            run: myweb
    replicas: 1
    template:
        metadata:
            labels:
                run: myweb
        spec:
                containers:
                    - name: my-nginx
                      image: nginx
                      ports:
                        -   containerPort: 80
```
- apply kubernetes template
kubectl apply -f myweb.yaml
- get pods
kubectl get pods -a
one to one mapping between pods and nodes
multiaz
  
### more hands on
create fargate profile with namespace and label for matching pod
kubectl apply -f myweb.yml -n default
kubectl get ns
kubectl create ns demo
kubectl apply -f myweb.yml -n demo  

#### diff hands on

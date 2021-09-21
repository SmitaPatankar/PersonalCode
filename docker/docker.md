# image  
- layer of images  
- base is mostly linux/alpine  
- application image eg: postgres  
  
# container  
- running instance of image  
  
# docker vs vm  
- h/w -> OS kernel layer -> applications layer  
- docker virtualizes application layer  
- vm virtualizes kernel and app layer - can use diff OS  
  
# download and install  
- docker community edition above windows 10 native - else docker toolbox  
- linux - setup stable repo, setup https connection and add docker GPG key, download  
  
# port mapping  
eg: two redis containers listening on 6379  
- map host port to container port  
- connect to container using port of the host  
  
# networking  
docker has isolated network within host  
containers within network can talk to each other via container name  
from outside browser they are connected to as localhost:port  
  
# network types  
bridge - default - private internal on host - internal ip 172.17.xx.xx - can talk to each container - for external use map host port to it  
host n/w - same for docker and host  
none - no access  
overlay n/w - spans across all nodes in cluster  
ingress n/w  - load balancer - route to correct container although exposed on same port  
  
# volumes  
host FS mounted to container - volumes  
volumes on host are at /var/lib/docker/volumes  
  
# docker compose file - common network created  
```  
version: '3'  # of docker-compose  
services:  
    {servicename}:  # container name  
        image: {image}:{version}  
         ports:  
            - {hostport}:{containerport}  
         volumes:  
            - xx:/abc/pqr
         environment:  
            - key:value  
volumes:  
    xx:  # to use for multiple containers  
        driver: local  
```  
  
# Dockerfile for building images - name should be as it is  
```  
FROM {baseimage}  
ENV key=value  
RUN {somelinuxcommand}  
RUN mkdir -p /home/app  # in container  
COPY ./app /home/app  # on host  
CMD ["python", "/home/app/main.py"]  # entrypoint command  
```  
  
# aws ecr  
aws ecr - repo for each image's versions  
set aws cli and creds  
execute commands for login and image push  
registry domain is like 1234.dkr.ecr.us-east-1.amazonaws.com  
  
# docker hub  
dockerhub pull's registry is docker.io/library/mongo:4.2  
  
# commands  
```  
docker pull {image}  
docker images  
docker run --detach {image}  
docker ps  
docker stop {id}  
docker ps -a  # not running container also  
docker start {id}  
docker run --detached -p6000:6379 {image}  
docker logs {id}  
docker run -d -p6000:6379 --name mycontainer {image}:{version}  
docker exec -it {id} /bin/bash - ls - env - exit  # use /bin/sh if bash doesnt work  
docker network ls  
docker network create {networkname}  
docker run -p 27017:27107 -d -e key=value --name {name} --network {network} {image}  
docker-compose -f xx.yaml up  # containers and networks take dir name as prefix  
docker-compose -f xx.yaml down  
docker build -t my-app:1.0 .  
$(aws ecr get-login --no-include-email --region us-east-1)  
docker tag my-app:latest registryDomain/imageName:tag  
docker push {image}:{version}  
docker run -v {hostdir}:{containerdir} - host volumes  
docker run -v {containerdir} - anonymous volumes  
docker run -v name:{containerdir} - named volumes - recommended - automatically creates on host  
```  
  
# swarm  
cluster of machines running docker  
swarm is built in docker engine  
convert machines to swarm manager and worker nodes  
machines should be in same subnet so they are reachable  
ports should be open i.e. 2377, 4789 and 7946  
node that first initializes swarm becomes the swarm manager  
if container is accessed on a diff IP, it's routed  
if node goes down, services shifted to other  
  
# commands  
```
docker swarm init --listen-addr localip:2377  
docker node ls  # on manager only  
docker swarm join managerip:2377  
# on manager:  
docker service create --name xx --publish 80:80 {image} ping {managervm} # can go to any vm including master  
docker service ls  
docker service tasks {servicename}  
docker service inspect xx --pretty  
docker service update --replicas 10 {servicename}  
# on node:  
docker ps
```
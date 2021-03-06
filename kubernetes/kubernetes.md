# kubernetes  
- container orchestration  
- helps manage apps containing many containers in diff envs eg: physical machines, VM, cloud env, hybrid envs  
- containers are for small independent micro services  
  
# offers  
- HA  
- scalable  
- disaster recovery  
  
# components  
- pod - kubernetes layer on container - eg: app pod, db pod - recommended 1 to one, but can have more containers - pod has internal ip - can die  
- service - permanent IP address for pod - so pod's dying doesn't matter - has LB  
- external service - open communication from external sources like browser - http://nodeip:8080 - not good - needs https and dns  
- ingress - external request will go to ingress and then to service - has https and dns  
- internal service - for db  
- node - server/physical/vm  
- ConfigMap - service urls etc  eg: which db service url app service connects to, so that renaming won't cause huge rework if it's in image  - connect to app pod - get used as env vars/property files  
- Secret - secret data like db creds, certs etc in base64 encoded format - connect to app pod - get used as env vars/property files  
- volume - physical storage on harddrive attached to pod - so dying of pod doesn't matter  - can be on local or remote machine, cloud, onprem etc - k8s doesn't take care of persistence  
- deployment - replicate everything on another server, which is also connected to the service - add blueprint of pods and number of replicas  
- StatefulSet - coz db replicas should be consistent and hence can't be replicated via deployments - difficult - better to keep db out of k8's cluster  
- replicaset - layer between deployment and pods  
  
# architecture  
- install on every worker node  
    - container runtime eg: docker  
    - kubelet - schedules containers in pods and gives node resources to it like cpu and memory  
    - kubeproxy - makes communication performant eg: app to db in same node  
- master node processes  
    - API Server - for user to communicate with kubernetes dashboard i.e. ui or kubelet i.e. CLI or kubernetes api - like cluster gateway - gets initial request for updates/queries - gatekeeper for auth  
    - Scheduler - start app pod on one of the worker nodes - intelligent logic to select worker node based on resources needed and already used on node - just decides where to put  
    - controller manager - to detect state changes eg: died pods and notifies to recover them  
    - etcd - kvstore of cluster state - has all changes updated - cluster brain  
- k8s cluster has multiple master nodes where api server is load balanced and etcd is in sync  
- master needs less resources than workers  
  
# scaling  
- get server  
- install all processes  
- add it to cluster  
  
# minikube  
- for testing  
- master and worker on same server - has docker already installed - access via virtualbox/some other hypervisor  
- system will have virtualbox, virtualbox will have node  
- 1 node k8s cluster  
  
# kubectl  
- command line tool to interact with k8s cluster i.e. API Server  
- most powerful than UI and API  
- kubectl is for any cluster like minikube, cloud, hybrid etc  
  
# install docker, minikube and kubectl on system:  
- https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker (https://itsfoss.com/could-not-get-lock-error/)  
- https://kubernetes.io/docs/tasks/tools/install-minikube  
- https://kubernetes.io/docs/tasks/tools/install-kubectl  
  
# add user to docker group
```
sudo usermod -aG docker $USER && newgrp docker  
```

# give user the permission to minikube profile directory  
```
sudo chown -R $USER $HOME/.minikube; chmod -R u+wrx $HOME/.minikube  
```

# create minikube cluster  
```
minikube start --driver=docker  
```

# see minikube details  
```
minikube status  
```

# see kubernetes details  
```
kubectl version  
```

# see kubernetes cluster details  
```
kuberctl get nodes  
kubectl get pod  
kubectl get service  
```

# create and see deployment  
```
kubectl create deployment nginx-depl --image=nginx  # rest all is default  
kubectl get deployment  
kubectl get replicaset  # no need to manage  
kubectl get pod  # no need to manage  
```

# edit and see deployment  
```
kubectl edit deployment nginx-depl  # edit opened conf for image version :1.16  
kubectl get pod  # old one terminates and new one starts  
kubectl replicaset # old one has 0 pods and new one created with 1 pod  
```

# debug pod  
```
kubectl logs {podname}  
kubectl describe pod {podname}  
kubectl exec -it {podname} -- bin/bash  
exit  
```

# delete and see deployment  
```
kubectl delete deployment nginx-depl  
kubectl get replicaset  
kubectl get pod  
```

# create deployment conf file  
```
touch nginx-deployment.yaml  
```
```
apiVersion: apps/v1  
kind: Deployment  
metadata:  
    name: nginx-deployment  
    labels:  
        app: nginx  
spec:  
    replicas: 1  
    selector:  
        matchLabels:  
            app: nginx  
    template:  
        metadata:  
            labels:  
                app: nginx  
        spec:  
           containers:  
           - name: nginx  
             image: nginx:1.16  
             ports:  
             - containerPort: 8080  
```  
  
# create deployment from conf file and see  
```
kubectl apply -f nginx-deployment.yaml  
kubectl get deployment  
kubectl get replicaset  
kubectl get pod  
```

# edit deployment from conf file and see (similarly for services, volumes etc)  
```
vi nginx-deployment.yaml - make 2 containers  
kubectl apply -f nginx-deployment.yaml  
kubectl get deployment  # shows 2 of 2  
kubectl get replicaset # shows one more container count  
kubectl get pod # one more created  
```

# understand conf file   
(auto generated status by kubernetes because it compares desired and actual state and updates state continuously for self healing status comes from etcd)  
(validate yaml)  
(good to store with app code or separate git repo for conf files)  
  
- api version of component  
```
apiVersion: apps/v1  
```

- declare what we are creating:  
```
kind: Deployment  
```

- metadata of component like deployment/service  
```
metadata:  
    name: xx  
```

- specification of component  
```
spec:  
    replicas: 2  
spec:  
    template:  # conf within conf for pod  
        metadata:  
        spec:  
            containers:  
            - name: nginx  
              image: nginx:1.16  
              ports:  
              - containerPort: 8080  
```

- labels are for connection - specific to component  
```
main metadata:  
labels:  
    app: nginx  # for service to connect with  
main spec:  
    selector:  
        matchLabels:  
            app: nginx  
template metadata:  
    labels:  
        app: nginx  
```

# create service conf file  
```
apiVersion: v1  
kind: Service  
metadata:  
    name: nginx-service  
spec:  
    selector:  
        app: nginx  
    ports:  
        - protocol: TCP  
          port: 80  # for other service to access this  
          targetPort: 8080  # to connect to pod  
```

# create deployment and service from conf and see 
```
kubectl apply -f nginx-deployment.yaml  
kubectl apply -f nginx-service.yaml  
kubectl get pod -o wide  
kubectl get service  
kubectl describe service nginx-service  
kubectl get deployment nginx-deployment -o yaml > nginx-deployment-result.yaml  
```

# delete deployment via conf file  
```
kubectl delete -f nginx-deployment.yaml  
kubectl delete -f nginx-service.yaml  
```

# create and see complete application  setup  
(mongo-express - pod - deployment - internal service - deployment.yaml env var for connecting to db configmap and secret)  
(mongo-db - pod - deployment - external service - configMap(url) - secret(user,pwd))  

```
apiVersion: v1  
kind: Secret  
metadata:  
    name: mongodb-secret  
type: Opaque  # others are for TLS certs etc  
data:  
    mongo-root-username: bXl1c2Vy  # taken from echo -n 'myuser'|base64  
    mongo-root-password: cGFzc3dvcmQ=  # taken from echo -n 'password'|base64  
```  
```
kubectl apply -f mongo-secret.yaml  
kubectl get secret  
```
```
apiVersion: apps/v1  
kind: Deployment  
metadata:  
    name: mongodb-deployment  
    labels:  
        app: mongodb  
spec:  
    replicas: 1  
    selector:  
        matchLabels:  
            app: mongodb  
    template:  
        metadata:  
            labels:  
                app: mongodb  
        spec:  
            containers:  
            - name: mongodb  
              image: mongo  
              ports:  
              - containerPort: 27017  
              env:  
              - name: MONGO_INITDB_ROOT_USERNAME  # referred from docker hub  
                valueFrom:  
                    secretKeyRef:  
                        name: mongodb-secret  
                        key: mongo-root-username  
              - name: MONGO_INITDB_ROOT_PASSWORD  # referred from docker hub  
]                valueFrom:  
                    secretKeyRef:  
                        name: mongodb-secret  
                        key: mongo-root-password  
---  
apiVersion: v1  
kind: Service  
metadata:  
    name: mongodb-service  
spec:  
    selector:  
      app: mongodb  
    ports:  
      - protocol: TCP  
        port: 27017  
        targetPort: 27017  
```  
```
kubectl apply -f mongo-deployment.yaml  
kubectl get all  
kubectl get service  
kubectl get pod -o wide  
kubectl get all|grep mongodb  
```
```
apiVersion: v1  
kind: ConfigMap  
metadata:  
    name: mongodb-configmap  
data:  
    database_url: mongodb-service  
```
```
kubectl apply -f mongo-configmap.yaml  
```
```
apiVersion: apps/v1  
kind: Deployment  
metadata:  
    name: mongo-express  
    labels:  
        app: mongo-express  
spec:  
    replicas: 1  
    selector:  
        matchLabels:  
            app: mongo-express  
    template:  
        metadata:  
            labels:  
                app: mongo-express  
        spec:  
            containers:  
            - name: mongo-express  
              image: mongo-express  
              ports:  
              - containerPort: 8081  
              env:  
              - name: ME_CONFIG_MONGODB_ADMINUSERNAME  # get from dockerhub  
                valueFrom:  
                    secretKeyRef:  
                        name: mongodb-secret  
                        key: mongo-root-username  
              - name: ME_CONFIG_MONGODB_ADMINPASSWORD  # get from dockerhub  
                valueFrom:  
                    secretKeyRef:  
                        name: mongodb-secret  
                        key: mongo-root-password  
              - name: ME_CONFIG_MONGODB_SERVER  # get from dockerhub  
                valueFrom:  
                    configMapKeyRef:  
                        name: mongodb-configmap  
                        key: database_url  
---  
apiVersion: v1  
kind: Service  
metadata:  
    name: mongo-express-service  
spec:  
    selector:  
        app: mongo-express  
    type: LoadBalancer  
    ports:  
        - protocol: TCP  
          port: 8081  
          targetPort: 8081  
          nodePort: 30000 # between 30000 and 32767  
```  
```
kubectl apply -f mongo-express.yaml  
minikube service mongo-express-service  # get http url and open on browser  
```

# about existing namespaces  
for organizing resources inside a cluster  
```
kubectl get namespaces  
```
- kube-system (master resources)  
- kube-public (public kubectl cluster-info)  
- kube-node-lease (about node's availability)  
- default (our resource go here if we don't have namespace)  
- our own  
eg: db, monitoring, logging, for diff teams with same named resources, stage/dev specific resources and some common resources in cluster, diff versions of prod and some common resources in cluster, limit resources and access etc  
each namespace should have its own configMap and secret for accessing common resource  
service can be accessed from other namespaces as `servicename.namespacename`  
some components are not namespaced - volumes, nodes  
  
# create and see namespace  
- way 1  
```
kubectl create namespace my-namespace  
```
- way 2  
```
apiVersion: v1  
kind: ConfigMap  
metadata:  
    name: mysql-configmap  
data:  
    db_url: mysql-service.database  
```
```  
kubectl apply -f {configfile} --namespace=my-namespace  
```
- way 3  
```
apiVersion: v1  
kind: ConfigMap  
metadata:  
    name: mysql-configmap  
    namespace: my-namespace  
data:  
    db_url: mysql-service.database  
``` 
```
kubectl apply -f {configfile}  
```

# see namespaces and resources  
```
kubectl get namespaces  

kubectl api-resources --namespaced=false  

kubectl api-resources --namespaced=true  

kubectl get configmap
# or
kubectl get configmap -n default  

kubectl getconfigmap -n my-namespace  
```

# change default namespace to ours if we don't switch often:  
https://github.com/ahmetb/kubectx#installation  
```
kubens  # active one is highlighted  
kubens my-namespace  
kubens  
```

# ingress  
open to outer world with internal service instead of external  
domain name instead of ip and port  
https instead of http  
browser->ingress->internalservice->pod  
```  
apiVersion: networking.k8s.io/v1beta1  
kind: Ingress  
metadata:  
    name: myapp-ingress  
spec:  
    rules:  
    - host: myapp.com  # must be valid and must be mapped to ip address of entrypoint node or if some server outside cluster is entrypoint, use that  
      http:  # for connecting to internal service  
        paths:  
        - backend:  
            serviceName: myapp-internal-service  
            servicePort: 8080  
```  
```  
apiVersion: v1  
kind: Service  
metadata:  
    name: myapp-internal-service  
spec:  
    selector:  
        app: myapp  
    ports:  
        - protocol: TCP  
          port: 8081  
          targetPort: 8081  
```  
default type is clusterIP  
  
# ingress controller  
pod or set of pods in our node to do evaluation and processing of ingress rules  
entrypoint in cluster  
does redirections based on rules  
K8s nginx ingress controller  
if on cloud -> browser - cloud lb - ingress controller  
if not on cloud -> configure entrypoint yourself inside or outside cluster eg: external proxy server (s/w or h/w) - public IP address with open port  
proxy server - ingress controller - ingress - service - pod  
  
# install and see ingress controller in minikube  
minikube addons enables ingress - starts nginx ingress controller  
```
kubectl get pod -n kube-system  
```

# install and see kubernetes dashboard  
https://itsfoss.com/could-not-get-lock-error/  
```
sudo apt-get update  
sudo apt-get install wget curl mlocate  
wget https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended.yaml  
kubectl create -f recommended.yaml  
kubectl get all -n kubernetes-dashboard  
```

# create ingress service for kubernetes dashboard  
```  
apiVersion: networking.k8s.io/v1beta1  
kind: Ingress  
metadata:  
    name: dashboard-ingress  
    namespace: kubernetes-dashboard  
spec:  
    rules:  
    - host: dashboard.com  # not registered  
      http:  
        paths:  
        - backend:  
            serviceName: kubernetes-dashboard  
            servicePort: 80  
```
```
kubectl apply -f dashboard-ingress.yaml  
kubectl get ingress -n kubernetes-dashboard  
kubectl get ingress -n kubernetes-dashboard --watch  
vi /etc/hosts  
{ingress service ip} dashboard.com  # local  
dashboard.com on browser  
```

# ingress default backend  
```
kubectl describe ingress dashboard-ingress -n kubernetes-dashboard  
```
can be used for error messages  
```  
apiVersion: v1  
kind: Service  
metadata:  
    name: default-http-backend  
spec:  
    selector:  
        app: default-response-app  
    ports:  
    - protocol: TCP  
      port: 80  
      targetPort: 8080  
```  
  
# ingress - multiple paths for same host  
```  
apiVersion: networking.k8s.io./v1beta1  
kind: Ingress  
metadata:  
    name: simple-fanout-example  
    annotations:  
        nginx.ingress.kubernetes.io/rewrite-target: /  
spec:  
    rules:  
    - host: myapp.com  
      http:  
        paths:  
        - path: /analytics  
          backend:  
            serviceName: analytics-service  
            servicePort: 3000  
        - path: /shopping  
          backend:  
            serviceName: shopping-service  
            servicePort: 8080  
```  
  
# ingress - multiple domains  
```  
apiVersion: networking.k8s.io/v1beta1  
kind: Ingress  
metadata:  
    name: name-virtual-host-ingress  
spec:  
    rules:  
    - host: analytics.myapp.com  
      http:  
        paths:  
            backend:  
                serviceName: analytics-service  
                servicePort: 3000  
     - host: shopping.myapp.com  
       http:  
        paths:  
            backend:  
                serviceName: shopping-service  
                servicePort: 8080  
```  
  
# ingress for https requests with tls cert secret  
```  
apiVersion: v1  
kind: Secret  
metadata:  
    name: myapp-secret-tls  
    namespace: default  # same namespace as ingress  
data:  
    tls.crt: {base64encoded cert}  # keys need to be exactly same  
    tls.key: {base64encoded key}  
type: kubernetes.io/tls  
```  
```  
apiVersion: networking.k8s.io/v1beta1  
kind: Ingress  
metadata:  
    name: tls-example-ingress  
spec:  
    tls:  
    - hosts:  
      - myapp.com  
      - secretName: myapp-secret-tls  
    rules:  
    - host: myaapp.com  
      http:  
        paths:  
        - path: /  
          backend:  
            serviceName: myapp-internal-service  
            servicePort: 8080  
```  
  
# Helm as k8s package manager  
package manager for kubernetes like apt, yum etc  
package collection of kubernetes yaml files and distribute them in public and private repositories  
adding elastic stack for logging would mean services, configmap, secrets, statefulset, k8s users etc  
helmchart: bundle of yaml files for specific purpose like elastic stack into helm repository - push or pull  
eg: db, elasticsearch, mongodb, monitoring(promotheus) etc  
- Install Helm: https://helm.sh/docs/intro/install/  
- install helm chart
```
helm install {chartname}  
```
- search helm chart
```
helm search {keyword} # or https://hub.helm.sh / https://github.com/helm/charts  
```
- can have private registries  
useful for deploying on multiple envs  
  
# Helm as templating engine  
to avoid writing repeat structure of deployment and service just for the sake of few changes in each microservice  
common blueprint and dynamic value placeholders i.e. template  
```  
apiVersion: v1  
kind: Pod  
metadata:  
    name: {{ .Values.name }}  
spec:  
    containers:  
    - name: {{ .Values.container.name }}  
     image: {{ .Values.container.image }}  
     port: {{ .Values.container.port }}  
```  
```  
name: my-app  
container:  
    name: my-app-container  
    image: my-app-image  
    port: 9001  
```  
or --set flag  
  
# helm chart structure  
```
mychart/  
    chart.yaml  # meta info about chart - name, version, dependencies etc  
    values.yaml  # default values for templates  
    charts/  # chart dependencies  
    templates/  # template files  
```
```
helm install {chartname} - templates filled with values  
other files - readme, license etc  
helm install --values=my-values.yaml {chartname}  # custom values - only diff, modify/new - merged - new .Values object  
or  
helm install --set xx=yy  
```

# k8s volumes  
- persistent volume  
- persistent volume storage  
- storage class  
eg: when db pod dies  
storage must be available to all nodes so that wherever db pod restarts, it can startup from storage  
storage should survive even if cluster crashes  
eg: for app which writes to files - persistent volume - like ram or cpu - via yaml  
it's an interface to actual storage like physical storage, aws block storage etc  
refer syntax from official docs  
nfs:  
```  
apiVersion: v1  
kind: PersistentVolume  
metadata:  
    name: pv-name  
spec:  
    capacity:  
        storage: 5Gi  
    volumeMode: FileSystem  
    accessModes:  
        - ReadWriteOnce  
    persistentVolumeReclaimPolicy: Recycle  
    storageClassName: slow  
    mountOptions:  
        - hard  
        - nfsvers=4.0  
    nfs:  
        path: {dirpathonnfsserver}  
        server: {nfsserveripaddress}  
```  
google cloud:  
```  
apiVersion: v1  
kind: PersistentVolume  
metadata:  
    name: test-volume  
spec:  
    capacity:  
        storage: 400Gi  
    accessModes:  
        - ReadWriteOnce  
    gcePersistentDisk:  
        pdName: my-data-disk  
        fsType: ext4  
```  
local:  
```  
apiVersion: v1  
kind: PersistemtVolume  
metadata:  
    name: example-pv  
spec:  
    capacity:  
        storage: 100Gi  
    volumeMode: Filesystem  
    accessModes:  
        - ReadWriteOnce  
    persistentVolumeReclaimPolicy: Delete  
    storageClassName: local-storage  
    local:  
        path: /mnt/disks/ssd1  
    modeAffinity:  
        required:  
            nodeSelectorTerms:  
            - matchExpressions:  
                - key: kubernetes.io/hostname  
                  operator: In  
                  values:  
                  - example-node  
```  
non namespaced  
local and remote  
local volume types are tied to node which is not nice and they also do not survive on cluster crash  
hence use remote storage  
storage needs to exist before pod as pod is dependent on it  
k8s admin role maintains cluster and ensures it has enough resources - makes and configures storage and make persistent volumes from these storage backends  
k8s user role deploys apps in cluster direct or via ci pipeline - app yaml  
app has to claim volume using PersistentVolumeClaim - created with yaml - matches criteria with available volumes  
```  
apiVersion: v1  
kind: PersistentVolumeClaim  
metadata:  
    name: pvc-name  
spec:  
    storageClassName: manual  
    volumeMode: Filesystem  
    accessModes:  
        - ReadWriteOnce  
    resources:  
        requests:  
            storage: 10Gi  
```  
use claim in pod  
```  
apiVersion: v1  
kind: Pod  
metadata:  
    name: mypod  
spec:  
    containers:  
        - name: myfrontennd  
          image: nginx  
          volumeMounts:  
          - mountPath: "/var/www/html"  
            name: mypd  
    volumes:  
        - name: mypd  
          persistentVolumeClaim:  
            claimName pvc-name  
```
configMap and secret are also local volumes but not use pv and pvc - they are directly managed by k8s - but can be done if needed  
```
apiVersion: v1  
kind: Pod  
metadata:  
    name: mypod  
spec:  
    containers:  
        - name: busybox-container  
          image: busybox  
          volumeMounts:  
            - name: config-dir  
              mountPath: /etc/config  
    volumes:  
        - name: config-dir  
          configMap:  
            name: bb-configmap  
```
```
apiVersion: v1  
kind: Pod  
metadata:  
    name: xx  
spec:  
    containers:  
        - name: xx  
          image: xx  
          volumeMounts:  
            - name: es-secret-dir  
              mountPath: /var/lib/secret  
    volumes:  
        - name: es-secret-dir  
          secret:  
            secretName: es-secret  
```
  
# Storage Class  
creates volumes dynamically when persistentvolumeclaim claims it  
created via yaml  
requested via pvc  
```  
apiVersion: v1  
kind: storageClass  
metadata:  
    name: storage-class-name  
provisioner: kubernetes.io/aws-ebs  
parameters:  
    type: io1  
    iopsPerGB: "10"  
    isType: ext4  
```
```
apiVersion: v1  
kind: PersistentVolumeClaim  
metadata:  
    name: mypvc  
spec:  
    accessModes:  
    - ReadWriteOnce  
    resources:  
        requests:  
            storage: 100Gi  
    storageClassName: storage-class-name  
```  
  
# StatefulSet  
for stateful applications eg: db or app that stores data  
deployed using StatefulSet instead of Deployment  
can have multiple pods or replicas  
cannot be randomly deleted/replicated as they have own identity on top of common blueprint  
so when pod dies new pod should have same sticky identity  
master pod has read write, slaves have only read, for consistency  
each pod has diff physical storage - each has own replica of storage  
data sync between master and slaves  
if cluster crashes db data will be gone, hence use persistentstorage  
use remotestorage because it should be available from all nodes, wherever the died pod is recreated  
stateful set pods have fixed ordered names unlike deployment ones, which have random hashes ahead of deployment name eg: statefulstatename:0, 1 etc - 0 is master  
next pod is created only when previous one is running  
new pod takes state from previous one and then syncs  
deletion is in reverse order, waits for each deletion  
each pod in statefulstate has its own dns name - podnamewithordinal.servicename - so that name and dns name remains same on dying and recreating - this is called sticky identity  
need to take care of below things on own:  
- syncing data  
- make remote storage available  
- backup  
bcoz containers should mostly be for stateless apps  
  
# Services  
- clusterIP  
default type  
service has ip and port  
each node has ip range - that's how pods gets ip  
when service is created, endpoint is also created - kubectl get endpoints to track which pods are endpoints of the service, so when pod dies new ip is tracked  
use port names in config for multiple ports in service  
- Headless  
for client to talk to a pod without service - eg: to write to master pod specifically in statefulset  
for pods to communicate with each other - eg: slaves to sync with master, for new slave to sync with previous  
set clusterIP None so that individual POD IPs are received instead of service IP in spec  
client can do dns lookup and use pod IPs  
- NodePort  
give type NodePort in spec  
static service port for 2 worker nodes in cluster  
for external request  
not secure - hence lb  
- LoadBalancer  
external lb used - nodeport and clusterip created on its own  
type: LoadBalancer  
and also has nodePort (for LB only, not outside)  
  
not covered:  
volume and storageclass configs in detail  
syncing data between db pods  
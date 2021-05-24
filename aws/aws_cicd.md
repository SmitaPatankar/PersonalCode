# AWS - ROOT
- Create root account on aws  
  (accountxx - passwordxx)  
- Set MFA for root account on aws
- Give billing access to IAM users in root account via ForceMFA policy on aws
(https://gitlab.com/LondonAppDev/recipe-app-api-devops-course-material/snippets/1944735)
- Create Admins group with AdministratorAccess and ForceMFA policy on AWS
- Create MyAdmin user in admins group with program and console access and auto generated password that is to be reset on AWS

# AWS - IAM - ADMIN
- Login with MyAdmin user and reset password on AWS
(passwordxx)  
- set MFA for MyAdmin user
- relogin with MyAdmin user and recreate access key
  (accesskeyxx, secretkeyxx)  
- create monthly recurring budget for IAM user for n dollars with threshold of n% with email on aws
- create s3 bucket for tfstate with bucket versioning on s3 on aws
- create dynamodb table with LockID as pk on aws
- create ecr repo with scan and push on aws
- create policy for user to push to ecr repo on aws
(https://gitlab.com/LondonAppDev/recipe-app-api-devops-course-material/snippets/1944784)
- create user with the above policy with program access on aws
(accesskeyxx, secretkeyxx)
- create policy for all our operations
(https://gitlab.com/LondonAppDev/recipe-app-api-devops-course-material/snippets/1944972)
- create user with the above policy with program access on aws
(accesskeyxx, secretkeyxx)
- import EC2 keypair from windows for ssh

# AWS VAULT
- Install aws-vault on windows
- save credentials in aws vault on windows
```
aws-vault add MyAdmin-
# enter access key
# enter secret key
vi ~/.aws/config
# enter region=us-east-1
# enter mfa_serial=<<mfadevicearn>>
```
- create session with temp credentials on windows
```
aws-vault exec MyAdmin --duration=12h -- cmd.exe
# enter mfa token
```

# IDE
- Install IDE with docker and terraform plugin on windows

# DOCKER
- Install docker on windows
- Test docker image on windows
```
docker build -t .
```
- Test docker container on windows
```
docker-compose up
docker compose -f xx run --rm <<command>>
```

# GIT
- Install git on windows

# GITLAB
- Create account on gitlab
(emailxx - passwordxx)
- Create ssh keys on windows and set them on gitlab
- set protected and masked variables on gitlab
```
AWS_ACCESS_KEY_ID - <<AWS_ACCESS_KEY_ID>>
AWS_SECRET_ACCESS_KEY - <<AWS_SECRET_ACCESS_KEY>>
ECR_REPO - <<URI>>
```

# Bastion
- ssh with ec2-user
- create superuser
```
$(aws ecr get-login --no-include-email --region us-east-1)
docker run -it -e DB_HOST=xx -e DB_NAME=recipe -e DB_USER=recipeapp -e DB_PASS=changeme123 xximagexx:latest sh -c python manage.py wait_for_db && python manage.py createsuperuser
# enter username and password for super user
```
- check on browser - publicip:8000/admin - login with creds

# AWS DNS
- register domain on route53
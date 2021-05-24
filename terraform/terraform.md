# Installation

## Windows
Download terraform and add its binary path to Path env variable.
Install terraform plugin on IDE.

## Linux
Download terraform via wget wget and unzip and copy it to /usr/local/bin i.e. to one dir from echo $PATH.

# Notes

- Terraform uses parallelism for creating resources.
- Indent by 2 levels.
- tf file has desired state and state file has current state.
- .terraform.lock.hcl prevents from changing version in tf file.
- Classify files as provider.tf, variables.tf, iam.tf, ec2.tf etc.
- Better to use AMI containing scripts than provisioners.
- Terraform registry has modules made by community that are verified/not verified by hashicorp.
- State file has passwords in plaintext.
- Save credentials in AWS CLI.
- Terraform cloud has UI, repo, plan - cost - apply, tf var - env var, settings, sentinel policy, encryption of state files.
- Workspaces have diff env vars and state files.

# Commands

## init
```
terraform init
terraform init --upgrade
terraform init -backend-config=backend.hcl
```

## fmt
```
terraform fmt
```

## validate
```
terraform validate
```

## plan
```
terraform plan
terraform plan -refresh=false
terraform plan -target=ec2
terraform plan -out=/tmp/myplan
```

## graph and dot
```
terraform graph > graph.dot
cat graph.dot|dot -Tsvg > graph.svg
```

## taint
```
terraform taint aws_instance.myec2
```

## export for logging
```
export TF_LOG = TRACE/DEBUG/INFO/WARN/ERROR
export TF_LOG_PATH=/tmp/mylog.log
```

## export env var
```
export TF_VAR_instancetype="t2.micro"
```

## workspace
```
terraform workspace new myworkspace
terraform workspace show
terraform workspace list
terraform workspace select myotherworkspace
```

## apply
```
terraform apply
terraform apply -auto-approve
terraform apply /tmp/myplan
terraform apply -var="instancetype=t2.micro"
terraform apply -var-file="custom.tfvars"
```

## output
```
terraform output
terraform output iam_names
```

## destroy
```
terraform destroy
terraform destroy -target aws_instance.myec2
```

## force-unlock
```
terraform force-unlock lock_id [dir]
```

## console
```
terraform console
```

## state
```
terraform state list
terraform state mv aws_instance.oldname aws_instance.newname
terraform state pull
terraform state push
terraform state rm aws_instance.xx
terraform state show aws_instance.xx
```

## import
```
terraform import aws_instance.my_ec2 idfromaws  # needs tf file as of now
```

# Syntax

## comments
```
# comment
```
```
// comment
```
```
/*
comment
comment
*/
```

## terraform
```
terraform {
  required_version = "> 0.12.0"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"  # 3.0, >=3.0, <=3.0, >=3.0,<=3.1
    }
  }
}
```

## provider
```
provider "aws"{
  region = "us-east-1"
  access_key = "xx"
  secret_key = "xx"
}
```

## resource
```
resource "aws_eip" "lb" {
  vpc = true
}
```

## output
```
output "eip" {
  value = aws_eip.lb.public_ip  # aws_eip.lb
  # sensitive = "true"
}
```

## variables
```
# variables.tf

variable "usernumber" {
  type = number
  default = 1
}

# terraform.tfvars / custom.tfvars

usernumber = 5

# ec2.tf

resource "iam_user" "lb" {
  name = var.usernumber
  path = "/system/"
}
```

## data source
```
data "aws_ami" "app_ami" {
  owners      = ["amazon"]
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

resource "aws_instance" "instance-1" {
  ami           = data.aws_ami.app_ami.id
  instance_type = "t2.micro"
}
```

## local provisioner

```
resource "aws_instance" "my-ec2"{
    ami = "xxx"
    instance_type = "t2.micro"
    provisioner "local-exec"{
        when = destroy
        command = "echo 'destroy time provisioner'"
        # on_failure=continue  # fail
    }
}
```

## remote provisioner
```
resource "aws_instance" "my-ec2" {
  ami = "xxx"
  instance_type = "t2.micro"
  key_name = "terraform"
  provisioner "remote-exec"{
    inline = [
      "sudo amazon-linux-extras install -y nginx1.12"
      "sudo systemctl start nginx"
    ]
  connection {
    type = "ssh"
    host = self.public_ip
    user = "ec2-user"
    private_key = "${file("./terraform.pem")}}"
  }
}
```

## resource attributes
```
resource "aws_security_group" "allow_tls" {
  name = "my-security-group"
  ingress {
    from_port = 443
    protocol = "tcp"
    to_port = 443
    cidr_blocks = ["${aws_eip.lb.public_ip}/32"]
  }
```

## count and count.index and splat expression
```
resource "iam_user" "lb" {
  count = 3
  name = var.elb_names[count.index]
}

output "arns"{
    value = aws_iam_user.lb[*].arn
}
```

## locals
```
locals{
    common_tags = {
        Owner = "DevOps Team"
        service = "backend"
    }
}

resource "aws_instance" "my-ec2" {
  ami = "xxx"
  instance_type = "t2.micro"
  tags = local.common_tags
}
```

## functions

### lookup and element
```
resource "aws_instance" "app-dev"{
    ami = lookup(var.ami, var.region)
    count = 2
    tags = {
        Name = element(var.tags, count.index)
    }
}
```

### file
```
resource "aws_key_pair" "loginkey" {
    key_name = "login-key"
    public_key = file("${path.module}/id_rsa.pub")
}
```

### formatdate and timestamp
```
locals{
    time = formatdate("DD MM YYYY hh:mm ZZZ", timestamp())
}

output "timestamp"{
    value = local.time
}
```

## dynamic block
```
resource "aws_security_group" "dynamicsg" {
    name = "dynamic-sg"
    description = "ingress for vault"
    dynamic "ingress" {
        for_each = var.ingress_ports
        iterator = port  # other wise dynamic block name will get used
        content {
            from_port = port.value
            to_port = port.value
            protocol = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
        }
    }
}
```

## our modules

```
# modules/ec2/ec2.tf

resource "aws_instance" "myweb"{
    ami = "xx"
    instance_type = var.instance_type
    security_groups = ["default"]
    key_name = "remotepractical"
}

# projects/myproject/myresource.tf

module "myec2"{
    source="../../modules/ec2"
    instance_type = "t2.large"
}

# projects/myproject/variables.tf

variable "instance_type"{
    default = "t2.micro"
}
```

## community modules
```
module "ec2-instance"{
    source = "terraform-aws-modules/ec2-instance/aws"
    version = "2.13.0"
    # insert required variables
    name = "my-cluster"
    ami = "xx"
    instance_type = "xx"
    subnet_id = "xx"
    instance_count = 1
    tags = {
        Terraform = "true"
        Environment = "dev"
    }
}
```

## workspace

```
# my-workspace.tf

resource "aws_instance" "myec2"{
    ami = "xx"
    instance_type = lookup(var.instance_type,terraform.workspace)
}

# variables.tf

variable "instance_type"{
    type = "map"
    default = {
        default = "t2.nano"
        dev = "t2.micro"
        prod = "t2.large"
    }
}
```

## remote backend
```
# create table in dynamodb with LockID as primary key

# backend.tf

terraform{
    backend "s3"{
        bucket = "xx"
        key = "filename"
        region = "xx"
        access_key="xx"
        secret_key="xx"
        dynamodb_table = "xx"
    }
}
```

## providers for diff regions and profiles
```
provider "aws"{
    region = "xx"
    alias = "mumbai"
}
resource "aws_eip" "one"{
    vpc="true"
    provider="aws.mumbai"
    profile = "account02"  # from awscli
}
```

## assume role
```
provider "aws"{
    region = "us-west-1"
    assume_role {
        role_arn = "xx"
        session_name = "xx"
    }
}
```

## explicit dependencies

```
resource "aws_instance" "xx"{
    instance_type = "t2.micro"
    depends_on = [aws_s3_bucket.example]
}
```

## conditions
```
resource "aws_instance" "xx"{
    instance_type = "t2.micro"
    count = var.istest == true ? 1: 0
}
```
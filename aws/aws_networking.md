# VPC

- region
- multiple AZs

- vpc with private CIDR
- local router for vpc
- main route table for vpc - destination=vpc cidr, target=local
- IGW attached to vpc

- public subnets for vpc in multiple AZs with smaller CIDR
- public subnet specific route table - destination=vpc cidr, target=local, destination=0.0.0.0/0, target=igwid

- ELB in public subnets
- NAT in public subnet

- private subnets for vpc in multiple AZs with smaller CIDR
- private subnet specific route table - destination=vpc cidr, target=local, destination=0.0.0.0/0, target=natid

- EC2 in private subnets
- db in other private subnets

- NACL is like FW for subnet
- sg is like FW for instance

- vpc endpoint gateway service for accessing s3 and dynamodb in same region
- vpc endpoint interface for accessing other services in same region (traffic routed through ENI in subnet)

- vpc private link to use SAAS by other company on AWS via vpc interface endpoint

# VPCs

- vpc peering between vpcs using AWS n/w

- transit gateway is better i.e. like hub

# VPC and on prem

- virtual private gateway on AWS
- corresponding router on prem i.e. customer gate way
- site to site vpn between the two where traffic goes via internet
- not reliable

- direct connect locations are already connected to AWS regions
- connect customer gateway to it

- we can also use transit gateway on aws side

- client vpn endpoint on AWS
- remote client can connect to it

# by user

- route 53 -> lb -> IGW
- cdn (edge locations are connected to aws using backbone n/w)

# levels

- IAM, route53, billing is on global level
- s3, cdn, dynamodb, sns, sqs, api gateway, lambda are on region level
- elb is on vpc level
- ec2 and rds is on AZ level

# CIDR

- classless inter domain routing
- IPv4 - 32 bit - 8.8.8.8 - 0-255.0-255.0-255.0-255 - 0.0.0.0 - 255.255.255.255
- 10.10.0.0/16 - 16 bits for n/w and rest changing for host - 2^16 i.e. 65536
- 10.10.0.0/24 - 8 bits for subnet i.e. 256 addresses
- 10.10.1.0/24 - same as above
- 5 IPs from subnet reserved by amazon
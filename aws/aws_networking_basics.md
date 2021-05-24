# structure (within vpc)    
```  
internet  
aws  
    vpc  
        cidr range  
        internet gateway to connect to internet  
        az for resilience  
            public subnet  
                ip address  
                    private ipv4 range - 10.0.0.0/8, 172.16.0./12, 192.168.0.0/16  
                    private ipv6 range - use dual stack for the same  
                    public ip addresses  
                routers - to talk to internet, to talk to other addresses  
                    route tables  
                        destination=private ip range of vpc, target=local  
                        destination=0.0.0.0/0, target=igw_id  
                nat gateway - for outbound access from private subnet to internet gateway  
                    public ip address  
                flow logs  
            private subnet  
                ip address  
                    private ipv4 range - 10.0.0.0/8, 172.16.0./12, 192.168.0.0/16  
                    private ipv6 range - use dual stack for the same  
                routers - to talk to other addresses  
                    route tables  
                        destination=private ip range of vpc, target=local  
                        destination=0.0.0.0/0, target=nat_gw_id  
                flow logs  
        security groups - distributed firewall - stateful - allow  
            public  
                rules  
                    type=http protocol=tcp port=80 source=0.0.0.0/0 0::/0  
                instances  
                    flow logs  
            private  
                rules  
                    type=customtcprule protocol=tcp port=2345 source=publicsg_id  
                instances  
                    flow logs  
        NACLs for security - stateless - at subnet level - granular  
        flow logs to s3 or cloudwatch  
        DNS - enable on vpc - dns resolution and hostnames  
```  
  
# vpc peering  
vpc peering - one to one - private - across accounts and regions - dont override cidr ranges - route table entries get added to vpc  
destination=othervpc, target=peerconnection  
  
# transit gateway  
transit gateway - attach vpcs - rule gets added to route table of vpc - private - cross account - not cross region as yet  
destination=biggeriprange for all vpcs, target=tgw_id  
has own routing table with attachment info  

# vpn  
aws site to site vpn - via internet - between on prem and vpc  
customer gateway on prem - virtual private gateway on vpc - 2 vpn tunnels for one connection for HA in 2 AZs  
update route table in vpc to use onprem range  
can connect to transit gateway  

# aws direct connect  
aws direct connect - dedicated physical connectivity in aws - between onprem and vpc  
aws direct connection locations have routers  
physical connectivity from onprem to direct connect location  
private virtual interface(vlan) from onprem to directconnect to vpc gateway  
public virtual interface from onprem to direct connect to aws managed services outside vpc  
aws direct connect gateway - for virtual connection from onprem to multiple vpcs - can connect to transit gateway  
vpc routetable - destination=onpremrange, target=tgw_id  
 
# route53 resolver
route53 resolver for dns resolution from onprem to aws and viceversa  
  
# vpc sharing  
vpc in owner account  
subnets can be shared with other participant accounts - can create sec groups etc - but can't change subnets, nacls etc  
can save ipv4 addresses  
saves peering  
separates duties  
bill for creator of resources  
  
# gateway endpoint  
access s3 and dynamodb from vpc  
update routetable  
destination=s3bucket, target=vpce-id  
  
# interface vpc endpoints  
for vpc to other aws services eg: aws services api  
no routing  
looks like service is in vpc  
ec2 uses private ip to connect to service  
can overwrite public domain name of service  
  
# vpc private link  
to share our services in one vpc to other vpc  
our service behind NLB i.e. endpoint service  
other vpc can create endpoint representing our service  
consumer connects to service on one port  
  
# global accelerator  
between users and app for optimized experience  
tcp/udp app  
# lb  
listener(s) port and protocol  
target group(s) for targets i.e. ec2/ip address/container  
autoscaling on the target groups  
  
# alb  
layer 7  
app  
http/https  
path/host based  
redirects  
fixed response  
slow start for newly added target  
ipv6  
tls management  
waf  
authentication - amazon,google etc  
server name indication  
tags to lb and target groups  
policy for lb, target groups, target  
atleast 2 AZs  
cloudwatch - latency, access  
hc  

# nlb  
layer 4  
n/w  
tcp/udp  
high throughput  
low latency  
flow based  
static ip on each az  
preserve source ip  
app and n/hc  
cloudwatch - flow  

# classic  
layer 4/7  
less features  
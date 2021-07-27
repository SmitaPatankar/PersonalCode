# Topology
- how machines are connected by cables and connectors

# Firewalls
- block unwanted traffic via ACL

# Network Components

## router
- network gateway
- connects networks
- routes packets to internal computers or sends them out to external computers

## switch
- connects devices to form networks

## hub
- like switch but doesnt know where to send data so sends everywhere

## Modem
- converts data from one form to another

## NIC
- For connecting computer to network

# MAC address
- hexadecimal printed on NIC

# OSI model
- application - data in readable form at user end
- presentation - compress/decompress and encrypt/decrypt
- session layer - create connection between apps
- transport - ensure packets are received by retrying if needed
- network - fragment/reassemble data and find destination
- data link - encode/decode data and send to physical layer
- physical - connect with cables etc

# IP address
- identify computer on network
- network address and host address
- IPv4(32 bit numeric), IPv6(128bit hexadecimal)

## IPv4
- 32 bit - 4 sets of 8 bits
- 8 bits form a number from 0 to 255
```
 1  0  0   0 0 0 0 0 |  0   0  0  0 0 0 1 0 |  0   0  0  1 0 0 1 1 |  0  0   1  0 0 1 0 0
128 64 32 16 8 4 2 1 | 128 64 32 16 8 4 2 1 | 128 64 32 16 8 4 2 1 | 128 64 32 16 8 4 2 1
        128          .           2          .           19         .         36
```

## IPv4 subnet mask
- first part for network and rest for host
  - class A - 255.0.0.0
  - Class B - 255.x255xx.0.0
  - class C - 255.0.0.0

## IPv6
- 128 bit - 8 sets of 16 bits
- 4 bits form one character from 0 to 9 and A to D
```
0010|0111|1101|1011 * 0010|0111|1101|1011 * 0010|0111|1101|1011 * 0010|0111|1101|1011 * 4 more
8421|8421|8421|8421 * 8421|8421|8421|8421 * 8421|8421|8421|8421 * 8421|8421|8421|8421 * 4 more
  2    6    D    B  :   2    6    D    B  :   2    6    D    B  :   2    6    D    B  * 4 more
```

## public IP
- on internet

## private IP
internal to network
- class A - 10.0.0.0 to 10.255.255.255
- class B - 172.16.0.0 to 172.31.255.255
- class C - 192.168.0.0 to 192.168.255.255

# subnet?
- small part of network
- for management
- network eg: 255.255.0.0
- subnet 2^n - 2 eg: borrow 3 bits from host network part to get atleast 3 subnets i.e. 6 subnets eg: 255.255.224.0

# IP addressing methods

## Dynamic IP
- get IP, subnet mask, default gateway and dns server from DHCP server
- better  
- lease - renews - can change - reservation can be done for imp devices for mac to avoid change
- router relays/broadcasts request if DHCP server is not on n/w  

## static IP
- manually assign IP
- no DHCP
- cannot change

## self assigned IP
- when DHCP is down  
- 169.254.0.0 - automatic private IP
- changes later when DHCP is up

# TCP/IP Protocol Suite

## TCP
- connection oriented (session)
  - syn ->
  - <-syn/ack
  - ack ->
- resends if failed

## UDP
- connection less/session less
- does not guarantee delivery

## FTP
- upload and download to/from file transfer
- connection oriented using TCP

## TFTP
- Trivial file transfer
- within same n/w
- no security
- connection less / udp

## SFTP
- secure FTP
- encrypted using SSH

## SMTP
- simple mail transfer
- based on TCP i.e. connection oriented

## POP3
- download email from mail server
- removed from mail server unless suggested otherwise
- eg usage: outlook

## IMAP4
- download email from mail server and also keep copy on server
- syncs emails from server to computer
- eg usage: outlook

## HTTP
- view web pages on internet
- clear text

## HTTPS
- secure/encrypted
- for sensitive information

## Telnet
- send commands remotely
- fast
- not secure
- plain text
- within local n/w

## SSH
- secure shell like tunnel

## ARP
- address resolution
- IP to MAC
- ARP cache at source server else broadcast msg with IP and matching computer will respond with MAC

## RARP
- MAC to IP

## NTP
- network time as per master clock

## SCP
- secure copy protocol with shell

## SNMP
- simple n/w mgmt
- collect data from n/w devices like routers, printers, servers

# Ports
- accept data
- TCP, UDP
- logical
- unique number from 0 to 65535
- HTTP = 80, HTTPS=443, SSH=22,DNS=53, Telnet=23, SMTP=25 etc

# DNS
- name to ip

# WINS
- windows internet name service
- computer name to IP on same n/w

# NAT
- n/w address translation
- translate IP to another IP eg: private to public on router and viceversa

# PAT
- port address translation
- translate IP based on port

# SNAT
- static nat
- link public and private permanently

# Proxy
- proxy server caches information for speed and bandwidth and security

# RDP
- for connecting to windows server remotely

# CSMA/CD
- carrier sense multiple access with collision detection
- send data during wire's idle time to avoid collission
- wait in case of collission

# CSMA/CA
- carrier sense multiple access with collision avoidance
- send small packet first to see if wire is idle

# broadcast
- single to multiple
- eg: wireless signal

# unicast
- single destination

# multicast
- multiple destinations

# routing protocols

## loopback interface
- virtual interface on router with IP
- for testing and admin

## routing table
- path of packet to destination
```
interface(sender), destination(gateway), next hop, subnet mask, best route(metric)
```

## distance vector protocol
as per hops to routers
eg: RIP - routing information protocol to other routers
eg: BGP - based on paths and policies

## link state protocol
independently map best path
eg: OSPF - open shortest path first - topology map
eg: ISIS - intermediate system to intermediate system - within domains

## hybrid protocol
eg: EIGRP - combo - for cisco routers

## SIP
session initiation
eg usage: VOIP, IM, conference

## RTP
real time
audio video
based on UDP
based on RTCP for quality
unicast/broadcast

# WAN technologies
data sent in packets

## packet switching/connection less
diff routes
assemble
eg: internet

## circuit switching
same route
eg: telephone lines

## ISDN
integrated services digital network
standard for telephone lines

## T1 carrier level
internet

## T3 carriel level
high speed internet

## E1 line
europe

## E3 line
european

## OCx 
optical carrier

# Internet access technologies

## DSL
digital subscriber line
access broad band data over the internet

### ADSL
asymmetric - download fast than upload

### SDL
symmetric

### VDSL
very high bit
copper wire - short distance
can use fiber optic cable for long distance

### cable
for broadband

### POTS/PSTN
plain old / public switched telephone service
for internet

### satellite
rarely used

### mobile hotspot
wireless

### WIMAX
super wireless

### metro ethernet
metropolitan area ethernet conenctivity

# types of networks

## PAN
personal area
eg: bluetooth

## LAN
same bldg - ethernet

## MAN
metropolitan area - few buildings or city - fiber optic

## WAN
wide area
country, continent or globe
eg: internet

## SCADA/ICS
monitor powerplants etc

## GSM and CDMA
mobiles
voice to digit and vice versa

## 4G
fast

# remote access protocols and services

## RAS
remote access service

## SLIP

# cc
## IAAS
our app, data, os, runtime, middleware

## PAAS
our app only
azure

## saas
everything from them
run app
google apps

## NAS
central stoage
feels like shared drive

## SAN
high speed
feels like hard drive
expandable
backup

# ipsec
network layer security for data transfer
sender and receiver should share public key
transport mode
tunnel mode

# tcp ip

app - http, dns, dhcp, ftp
transport - tcp, udp
internet - ipv4, ipv6, icmpv4, icmpv6 - routing protocols, nat
network access layer - ethernet etc, ppp, frame relay

data - segment - packet - frame - bits
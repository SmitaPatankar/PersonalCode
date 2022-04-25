# network basics
- connects machines 
- eg: phone -> watch i.e. personal area network
- eg: tablet -> wireless access point -> internet via wifi network
- eg: desktop -> hub -> switch -> router -> internet
- converged digital network for voice, data etc

# network components

## client
- device used by end user to access internet
- eg: laptop, phone, tv, server

## server
- provides resources to network
- eg: email server, file server, web server, print server, chat server
- dedicated h/w or s/w that makes it act accordingly 

## hub
- old
- connect devices like clients and servers 
- issue - signal to one port and then re-broadcasted to all ports

## wireless access point
- wireless hub
- for wireless devices to connect to wired network

## switch
- smarter version of hub 
- connects clients and servers 
- receives on one port and knows which port to send to exactly 
- secure and efficient

## router
- connects diff networks 
- make forwarding decisions based on IP address

## media
- connect 2 devices or connect device to switch port 
- eg: copper cable - cheap but cant go far
- eg: fiber optic cable - can go far but cost is more
- eg: radio waves - for wifi

## WAN link
- connection to outer world
- physically connects 2 geographically dispersed networks
- internet is big series of WAN links
- eg: lease line
- eg: DSL line
- eg: cable line
- eg: fiber optic line
- eg: cellular line
- eg: microwave
- it is router back into our network via our router
- connect internal n/w to external
- eg: connect home office to internet

# Network Models
how data is moved around network

## client server model
- server provides access to printers, scanners, files etc
- easy/centralized administration, management, backup and scalability
- cost for dedicated h/w and dedicated os
- server stays on always

## peer to peer model
- peers like laptops, desktops etc share resources like files, printers etc directly
- low cost, no specialized h/w, no specialized OS
- administration, management, backup and scalability is difficult due to diff places
- peer is not on always

# Network Geography

## PAN
- personal area network
- wired/wireless
- <= 10 ft i.e. couple of metres
- eg: bluetooth
- eg: USB

## LAN
- local area network
- wired/wireless
- 300 ft or 100 metres
- cat 5 cabling = 100 metres
- fiber optic = more
- for small offices or home
- ethernet - IEEE 802.3 standard
- wifi - IEEE 802.11 standard

# CAN
- campus area network
- few buildings in IT park, college campus
- multiple LANs form CAN

# MAN
- metropolitan area network
- across city
- 25 miles
- multiple CANs form MAN

# WAN
- wide area network
- connects leased lines, VPNs etc
- state/country/world
- internet
- not necessarily public
- LANS from diff countries make WAN
- 3000-4000 miles

# Network topology
- physical - cabling
- logical - data flow via network

## Wired network topology - physical/logical

### Bus
- single cable in line in entire area
- machine connects to it via t connector
- old
- collisions are possible when multiple machines talk together

### Ring
- single cable in circle
- collisions are possible when multiple machines talk together
- clockwise or anticlockwise

### Token Ring
- electronic tag passed from computer to computer as they were about to talk to take turns to avoid collision
- if cable was cut, network is down i.e. no redundancy
- Hence, FDDI ring i.e fiber distribution data interface
- 2 rings in clock and anticlock for backup if one is cut
- new

### star
- all machines talk to central point eg: switch using fiber/copper/wireless
- if cable is cut or power is down, network is down i.e. single point of failure
- cheap

### hub and spoke
- connect multiple sites
- like connecting stars together
- similar to connecting flights
- not fully redundant is one hub fails
- better than single star

### full mesh
- fully redundant
- everything to everything
- optimal routing i.e. one jump to other machine
- expensive
- less common physically

### partial mesh
- hybrid of full mesh and hub and spoke
- optimal routing between some sites that are in demand
- more hubs than hub and spoke
- if something fails, alternate route is available

## wireless network topology - logical

### infrastructure mode
- wifi connecting to outside world via cable/fiber modem
- devices connect to wireless access point like start topology wirelessly
- security controls and benefits

### adhoc mode
- like peer to peer
- eg: between laptops

### wireless mesh
- interconnections of diff types of nodes, devices and radios like routers, geteways, clients, servers, radio, tunnels
- eg: combination of bluetooth, wifi, microwave, cellular, satellite
- redundant and reliable
- eg: after disaster
- microwave goes 30-40 miles
- satellite goes 1000s of miles
- wifi goes about 100 feet

# internet of things
- eg: refrigerator with wireless connection
- eg: smart tv
- eg: servers
- eg: desktop
- eg: car
- eg: bluetooth keys

# internet of things technology
- 802.11 - wifi
- bluetooth
- rfid - radio frequency identification
eg: hotel room key with chip that uses electromagnetic field
- nfc - near field communication - 2 devices within 4cm 
eg: google pay
- ir - infrared - light beams - old
eg: tv remote
- z-wave - short range, low latency, low power, low data rate than wifi - low speed - home automation
eg: sound, lights in home
- ANT+ - collection and transfer of sensory data i.e. know what is on or off i.e. for things having sensors - know temperature, brigthness
eg: tier pressure of car

# OSI model/stack
- open systems interconnection model
- ISO 7498
- old
- all networks
- 7 layers (Please Do Not Throw Sausage Pizza Away)(Do Some People Fear Birthdays)
  1. Physical - bits - hub
  2. Data link - frame
  3. Network - packet - router
  4. Transport - segment
  5. Session - data
  6. Presentation - data
  7. Application - data

## Physical Layer
- binary bits(0s and 1s) are transferred across network
- media - represents bits differently - transition modulation used for switching between 0 and 1 mode
  - ethernet network
  - fiber optic cables - light - light off for 0 and light on for 1
  - copper cables - cat5/cat6 - 0 voltage for 0 bit, +or-5voltage for 1 bit - RJ45 connector
  - radio frequency for wifi, bluetooth
- standards for connectors
  - TIA/EIA-568A
  - TIA/EIA-568B
- cables
  - cross over cable - flips transmission and receiving bits at the end of the cable - one end will have A std and one B
  - straight through cable/patch cable - B std on both sides
- topology
- communication
  - async - eg: email, voicemail - start bit to start transmission - stop it to stop transmission
  - sync - eg: phone call - like clock i.e. transmit and receive every second
- bandwidth
  - broadband - divides bandwidth into separate channels like tv channels
  - baseband - all frequency used all time - eg: telephone - one call at a time - uses reference clock for asyn communication 
    eg: wired ethernet network - all frequency from cable used - gives more bandwidth that broadband area
- get more out of baseband
  - TDM - time division multiplexing - each session will take turns using time slots
  - StatTDM - statistical time division multiplexing - time slots allocated on need basis
  - FDM - frequency division multiplexing - split cable into channels - each person gets small portion of frequency
- examples (repeat whatever is given - in and out)
  - cables
  - radio frequency
  - hubs
  - access points
  - media converters

## Data Link Layer
- package bits from physical layer and put them into frames and transmit them throughout network
- while identifying unique network devices using mac address
- MAC
  - media access control access 
  - identify device physically and operate it logically
  - 48 bit address on NIC - Network Interface Card
  - eg: D2:51:F1:3A:34:65 - 1 letter = 4 bits - first 24 bits = manufacturer - next 24 bits = actual machine
  - see whose turn it is to talk
- LLC - logical link control - connection services and recipients acknowledge receipt or issue  
last bit odd/even and sum of all bits also same means correct else issue
- communication synchronization modes
  - isochronous - common reference clock + time slots for transmission i.e. like synchronous + time division multiplexing
  - synchronous - devices use same clock + beginning and end frames and special characters to denote when we'll start and end - drawback have to work as per clock times
  - asynchronous - each device has own clock and start and stop bits
- devices
  - NIC
  - bridge
  - switch (logic - which phys port is attached to which device based on mac address)

## Network Layer
- forwarding traffic i.e. routing using logical addresses
- IP address - v4 or v6 or both - logical address
- networking layer switching = routing
- routing protocol - IP - others also exist
- eg: 172.16.254.1
- ways to transfer data
  - packet switching - common - like letter - switch from place to place till final destination - if failed, resends on other route
  - circuit switching - same dedicated link for a session like phone call
  - message switching - data divided into messages - like email - like packet switching but can store and forward
- routers have routing tables for packets to move forward based on IP address of destination - static/dynamic route
- routing protocols - RIP, OSPF, EIGRP etc - to select path - like map
- in dynamic routing - routers continously talk to each other and know best routes
- connection services - augment data link layer connections for more reliability
  - flow control - eg: speed of sender as per receiver
  - packet reordering - order packets at receiver in correct order and put together for data
- ICMP - internet control message protocol - send msgs and operational info to IP destination
  - eg: ping - check if received and in how long
  - eg: tracert - gives info of every router on the way - uses series of pings from each router
- devices
  - routers
  - multilayer switches (switch and router combined)

## Transport Layer
- segment and datagram data type
- protocols
  - TCP
    - transmission control protocol
    - connection oriented i.e. reliable way to transport segments across network
    - resend segment if no ack received
    - client - syn : server - ack : client - ack i.e. 3 way handshake
    - windowing
    - segment sequencing
    - eg: banking, website, ecommerce
  - UDP
    - user datagram protocol 
    - connection less protocol
    - datagram data type
    - unreliable
    - sender won't know of drops
    - eg: audio/video - few seconds part drop doesn't matter
    - no overhead of handshake and checks
    - no windowing
    - no segment sequencing
- reliability features
  - windowing
    - adjust amount of data in each segment
    - retransmission means too much data
    - no retransmission means less data
    - eg: 20 mins remaining, 5 mins remaining, 10 mins remaining
  - buffering
    - routers store segments if bandwidth isn't available and clears out later
    - segments drop when buffer runs out of memory
- devices
  - TCP
  - UDP
  - WAN accelerators - add compression to IP packets and send segments through WAN accelerators to our n/w faster
  - Load balancer
  - firewall - eg: block port 80 for TCP

## Session layer
- separate conversation to avoid intermingling of data
- tasks
  - set up
    - check user credentials and assign number to session
  - maintain 
    - transfer data back and forth 
    - re-establish connection if broken 
    - acknowledge receipt
  - tear down
    - both parties agree to disconnect or one party disconnects
- protocols
  - H.323
    - setup, maintain and teardown voice and video connections
    - operators on RTP - real time protocol
    - eg: video call
  - NetBIOS
    - share files over n/w

## presentation layer
- tasks
  - format data
    - make compatible for diff devices
    - examples
      - scripting language - HTML, PHP, JS, CSS
      - standard text - ASCII, UNICODE
      - Pictures - GIF, JPG, PNG
      - Movies - mp4, mpeg, mov
      - encrypt data
  - encrypt data
    - scramble
    - examples
      - TLS
      - SSL

## application layer
- application services - unites components from multiple n/w applications
- examples
  - file transfer protocol - FTP, FTPS, SFTP
  - n/w transfer/mgmt
  - email protocols like POP3, IMAP, SMTP
  - remote access - telnet, ssh, SNMP
  - client server processes
  - web browsing - http/https
  - dns
- service advertisement  - advertise provided services
- examples
  - new printer joined n/w

# wireshark packet analyzer - pcap files
- example packet for TCP (SYN)
  - layer 2 - data link layer - frame - mac address - ethernet encapsulation
  - layer 3 - network layer - IPv4
  - layer 4 - transport layer - TCP
- example packet for TCP (SYN ACK) - same as above
- example packet for HTTP - layer 7 - browser, server, url, content
- example packet for telnet - layer 7 - user and server interactions like creds, commands, ping

# encapsulation and decapsulation
- encapsulation
  - put headers and trailers around data
  - layer 7 to 1
- decapsulation
  - remove headers and trailers from data
  - layer 1 to 7
- PDU - protocol data unit used to transmit data - as per layers
  - L7 - application - data - with header metadata for application like HTTP
  - L6 - presentation - data - above + header for presentation/encryption
  - L5 - session - data - above + header for session
  - L4 - transport - segment for tcp/datagram for udp - above + tcp header with 10 fields i.e. 20 bytes or udp header with 4 fields i.e. 8 bytes
  - L3 - network - packet - above + IP header with many fields
  - L2 - data link - frame - above + ethernet header with few fields + payload with minimum 42 bytes for vlan and 46 bytes without vlan
    payload has MTU default 1500 bytes else use jumbo frame
  - L1 - physical - bits - 1s and 0s
- specific headers
  - tcp header
    - source port
    - destination port
    - sequence number
    - ack number
    - offset
    - reserved
    - window size
    - checksum
    - urgent pointer
    - mtcp (optional)
    - tcp flags
      - syn - from client for 3 way handshake
      - syn ack - from server for 3 way handshake
      - ack - from server for 3 way handshake
      - fin - tear down connection - after last packet is sent by host
      - rst - reset when client/server receives unexpected package
      - psh - used by sender to indicate high priority data
      - urg - tell recipient to process immediately and ignore anything else in FIFO
  - udp header
    - source port
    - destination port
    - length
    - checksum (optional)
  - IP header
    - version
    - length
    - type of service
    - total length
    - identifier
    - flags
    - fragmented offset
    - TTL
    - protocol
    - header checksum
    - source ip
    - destination ip
    - options and padding
  - ethernet header
    - source mac address
    - destination mac address
    - EtherType (protocol)
    - VLAN Tag (optional) - IEEE802.1Q or IEEE802.1AD 
- next device tasks eg: switch
  - put bits back together
  - read ethernet header and send to switch port if mac is of that else send to default gateway i.e. router
  - router reads ip header and sends to device if on own network else reencapsulate and send to default gateway till host is found
  - host decapsulates till L7 header

# TCP/IP model or TCP/IP Stack or DoD model(dept of defence)
- reference model
- alternative to OSI model
- 4 layers
- layers
  - application  - application 
  - presentation - application
  - session      - application
  - transport    - transport
  - network      - internet
  - data link    - network interface
  - physical     - network interface

## network interface layer
- transmit bits across n/w
- decide network medium - twisted pair copper cable, coaxial cable, fiber cable, wireless, tcp over ethernet/token ring

## internet layer
- package data into IP datagram
- source dest ip
- transfer data across hosts
- routing
- externally on remote networks
- internet to intranet
- internet vs external
- examples - IP, ICMP, ARP, Reverse ARP

## Transport layer
- level of service and status of connection used by TCP, UDP, RTP
- protocols
  - TCP - connection
  - UDP - connection less
  - RTP - real time (voice and video)

# Application layer
- how program connects with transport layer and conduct session mgmt
- user interacts with n/w via some program
- examples - HTTP, Telnet, FTP, SSH, SNMP, DNS, SMTP, SSL/TLS

# data transfer over networks
- ip
  - where to go
- port
  - for particular app - logical opening on system or app i.e. listening and waiting for traffic
  - 0 to 65535 ports on a machine
  - well known/reserved ports - 0 to 1023
    - FTP - 21
    - SMTP - 25
    - HTTP - 80
  - ephemeral ports for short time - 1024 to 65535
    - client request goes from random to 80 on server
    - server response comes from 80 to that random on client
- IP flags - for packet fragmentation etc
- protocol - TCP/UDP

# protocol, port and usage
protocol | full form | port | purpose
--- | --- | --- | ---
FTP | file transfer protocol | 20, 21 | between client and server on n/w - clear data - insecure
SSH | secure shell | 22 | remotely take control of other computer via command shell - cryptographic - safe for use over internet
SFTP | secure ftp | 22 | tunnel ftp through ssh
Telnet | - | 23 | remote access via command prompt - insecure for username, pwd, data
SMTP | simple mail transfer protocol | 25 | emails
DNS | domain name system | 53 | hierarchical decentralized name system for computers etc connected to private network and internet - ip to domain name and vice versa
DHCP | dynamic host control protocol | 67, 68 | automatically assign IP address and network configurations eg: ip, subnet mask, default gateway, dns server
TFTP | trivial FTP | 69 | file transfer in both directions of client server - no auth/directory vision - stripped down version of FTP - send/request conf files from router/switch - boot OS from network file server
HTTP | hyper text transfer protocol | 80 | data communication for www
POP3 | post office protocol | 110 | local email client to retrieve emails from mail server over TCP/IP connection - incoming email - store and forward mode - old
NTP | network time protocol | 123 | sync date and time across network devices
NetBIOS |n/w based i/o system | 139 | apps on separate computers communicate over windows local network to share files, printers
IMAP | Internet mail application protocol | 143 | email clients can receive msgs from email server over TCP/IP connection + view/edit mails even when they are on server - new - eg: read, unread status as email server keeps track - syncs all devices
SNMP | simple n/w mgmt protocol | 161, 162 | collect info about all managed devices on IP n/w eg: router, switches, voip phones - can modify device info - monitor uptime, downtime, etc
LDAP | Light weight directory access protocol | 389 | access and maintain distributed directory information services - like Active Directory in windows - AD is proprietary version of LDAP - used to say search email contacts in addressbook - users and groups also saved
HTTPS | HTTP - secure | 443 | HTTP over encrypted tunnel using SSL/TLS i.e. secure socket layer / transport layer security(new and more secure)
SMB | server msg block protocol | 445 | provides system with shares access to files, printers etc between devices on windows n/w - operates often with NetBIOS(auth)
Syslog | system logging | 514 | send sys logs to centralized server i.e. syslog server for monitoring and review by analysts
SMTP TLS | SMTP transport layer security | 587 | encrypted SMTP
LDAPS | secure LDAP | 636 | secure LDAP
IMAP over SSL | secure IMAP | 993 | secure IMAP - over encrypted SSL tunnel - receive emails
POP3 over SSL | secure POP3 | 995 | secure POP3 - over encrypted SSL tunnel
SQL protocol | structured query language protocol | 1433 | client communication with db for microsoft SQL server db engine
SQLnet protocol | SQL net | 1521 | client to oracle db
MySQL | MySQL | 3306 | client to MySQL i.e. opensource db
RDP | remote desktop protocol | 3389 | proprietary protocol by microsoft - control computers remotely using GUI - inside network or over internet
SIP | session initiation protocol | 5060, 5061 | signalling and controlling media communication sessions for different apps - eg: VoIP, video/audio calls, insta msging - eg: skype,facetime etc

# finding open ports
- nmap tool - network mapper - for troubleshooting
- `nmap -sS -O <<ip>> | more`  # sS = syn scan , O = os
- zenmap for UI - profile i.e. quick scan, intense scan - creates nmap command - shows topology, app version etc
- use scanb.org for practice

# IP protocol types

## TCP
- transmission control protocol
- layer 4 - transport layer
- used on top of IP for reliable transmission
- 3 way handshake
- windowing - continuously negotiate how much data should be sent and received
- receiver sends ack
- connection oriented
- sequence can be made correct
- missing packets can be resent

## UDP
- user datagram protocol
- connection less
- on top of IP
- lightweight
- corrupt packets are detected by client using checksum
- no connection/sequencing
- cant detect missing/unordered packet
- used for audio/video streaming
- no reliability
- fast and simple
- no accuracy

## ICMP
- internet control message protocol
- network layer
- communicate network connectivity issues back to sender
- eg: ping
- error reporting
- send ICMP datagram from client/server/network device
- send redirect msgs, diagnostic msgs etc
- for troubleshooting
- for attacks

# GRE
- generic routing and encapsulation protocol
- tunneling protocol by cisco
- encapsulate network layer protocols inside virtual point to point or point to multipoint link over IP network
- tunnel over public network
- encapsulation decapsulation from one side of tunnel to other
- check MTU considering encapsulation bytes also to not exceed general MTU size of 1500 bytes by devices
- no encryption by default

# IPSec
- Internet protocol security protocol
- network or packet processing layer
- protect data flow between peers
- TCP protocol
- authenticate and encrypt IP packets
- features
  - data confidentiality
  - data integrity
  - origin authentication
  - anti-replay
- tunnel over public WAN
- encrypted tunnel
- used in VPN using 2 underlying protocols
  - AH - authentication header - integrity and authentication - normal ip header + data payload is hashed = new AH header append to packet - AH header goes from our router to destination router - destination receives, hashes, checks packet against this header - rejetced packets are resent due to TCP
  - ESP - encapsulation security payload - encryption and integrity - ESP header after IP header - routed with IP devices - backwards compatible with older routers not designed for IPSec

# bandwidth
- theoretical measurement of how much data can be transmitted from source to destination 

# throughput
- actual measure

# Media
- material to transmit data over network
- interconnect nodes on computer n/w
  - copper - cables
  - fiber optic - cables
  - wireless - radiowaves

## copper media
Types:
- coaxial - old
  - center wire + insulator (conductor), metal shield, plastic
  - examples:
    - RG-6 - connected cable service to home 
    - RG-59 - inside home - carry composite video between 2 nearby devices, connect outlet to cable modem - for cable tv/satellite tv
  - connectors:
    - F-Type - common - cable tv, cable modems - screwed
    - BNC - push and turn to lock
- twinaxial
  - 2 conductors
  - for short range and high speed - upto 10 Gbps speed
- serial - not common
    - series of copper wires inside plastic jacket
    - RS232 signaling method
    - connectors:
      - DB9 - 9 pins at end - d shaped
      - DB25 - 25 pins at end - d shaped
- twisted pair - popular
  - 100m/300feet approx 
  - examples:
    - network cable to laptop
    - 8 wires in sheath and twisted in 4 pairs
  - twist for less interference from electromagnetic waves
  - types:
    - utp - unshielded twisted pair - plastic shield - common - easy to bend etc
    - stp - shielded - metal foil wrap before plastic
  - connectors: (registered jack standardized n/w interface)
    - RJ45 - common - plastic - A pin - for ethernet based networks - 8 pin - cat5 uses only 4
    - RJ11 - 6 pin - conf uses only 2 - for phone to landline jack - 1 for ring , 1 for signal - for DSL modem or VoIP services
  - categories:
    - CAT3 - ethernet - 10BASE-T - 10Mbps - 100m
    - CAT5 - fast ethernet - 100BASE-TX - 100Mbps - 100m
    - CAT5e - Gigabit ethernt  -1000BASET - 1000Mbps i.e. 1Gbps - 100m
    - CAT6 - 1000BASE-T / 10GBASE-T - 1000Mbps i.e. 1Gbps / 10Gbps - 100m/55m
    - CAT6a - 10GBASE-T - 10Gbps - 10Gbps - 100m
    - CAT7 - 10GBASE-T - 10Gbps - 100m - RJ45/terra connector - hence speed achieved faster - older than above
    - CAT8 - 40GBASE-T - 40Gbps - 30m
  - ahead of 100m - signal needs to be repeated using switch/router/some repeating device
  - length of cable also needed from ceiling, floor etc

## straight through cable/patch cable
- same pinpoints on both ends
- 568A
- 568B - preferred in buildings - orange blue green brown with whites on left
- connects DTE to DCE or vice versa
- DTE = data terminal equipment i.e. laptop, desktop, servers, routers
- DCE = data communications equipment i.e. switch, modem, hub, bridge

## cross over cable
- connect DTE to DTE or DCE to DCE
- swaps send and receive pins on other end
- 568A and B on each side
- switch to switch also required cross over cable earlier
- pins 1 2 3 and 6 from 568B are crossed over on other end
- orange and green pairs swap places
- 568A - GBOB - green blue orange brown
- 568B - OBGB - orange blue green brown

## MDIX
- medium dependent interface crossover
- simulate use of cross over cable electronically
- used in modern networks along with straight through cables for switches

## plenum cable
shielding on utp or stp cable for retarding fire from insulation
# Q&A

## How to get the process that utilizes highest memory?  
```  
ps aux --sort=-%mem | tail -1  
# a - all users  
# u - show users  
# x - show processes without terminal processes also  
```  

## If one person opens file in editor and other person deletes the file from separate terminal, what will happen to the first person's process?  
- File from first person's process will get saved as a new file.  
  
# If some process on one terminal is using a file and other person deletes the file from separate terminal, what will happen to the first process?  
- If the file is open by process, file won't get deleted from the system completely, only it's link will get deleted.  
- If the process goes to open file newly, error will be thrown.  
    
## When we access a URL on browser what happens further in detail like how does the dns work, where is the dns entry searched exactly on linux?  
```
curl -v https://google.com
dns lookup
determine port
offer ALPN i.e. tell that you support HTTP1, HTTP2
prepares local dirs to write certs that server will send
tcp connection established - syn, ack, syn ack
tls handshake - client hello, server hello, server encrypted extensions, server cert, server cert verify, client change cipher, client tls handshake 
ALPN protocol determined as http2
get request, protocol, host, accept header
get response
```
```
for client to identify server name, we can add mapping to /etc/hosts i.e. name resolution
this is difficult
hence dns server(nameserver) mapping put in /etc/resolv.conf
/etc/hosts can still be used for testing
/etc/hosts is looked first
order can be changed
can have multiple name servers in resolv.conf
that's difficult
hence forward mapping can be added to first dns server
ROOT - .
TLD - .com, .net, .edu, .org
domain name - google
sub domain - www, maps, drive, apps
organization dns server(caches for few secs/mins) - root dns - .com dns - google dns
organization dns can have company names
to refer web.mycompany.com as web internally, put search mapping in /etc/resolv.conf - search mycompany.com prod.mycompany.com
dns server entry
A record for ipv4
AAAA record for IPv6
CNAME for alias
nslookup for name resolution
does not consider hosts file like ping
dig shows more details
```

## What is hardlink and softlink?  
- Hardlink points to disk location of original file name.    
Hence hardlink exists even if original file is deleted.    
. and .. are hardlinks.  
It can be used when same file is needed in different directory structures.  
It can be created on same file system only.  
- Soft link links to the original file name.  
It is useless if original file is deleted.  
It can be used across filesystems.  
It can be used to rename commands.  
  
## If we delete a file and there is no backup and hard link and softlink, can it be recovered?  
- Files point to inode and inode points to location on disk.  
- When file gets deleted, data still exists on disk unless it's replaced i.e. only the slot is marked as free.  
- It can or cannot be recovered by some difficult process.  
  
## How can we make a file not deletable by root also?  
```
chattr +i filename  
# chattr -i filename - to revert  
```

## How exactly does traceroute work?  
- Packet has source, destination and TTL info eg: 30 by default so that it does not hop forever in case of an incorrect loop.
- Packet goes via various routers and each time TTL is reduced by 1.  
- 3 Packets are sent and received back.  
- Round trip time is shown.  
- Packet is dropped and message is sent to sender when TTL becomes 0.  
- Shows all hops.
- Some routers show * but pass packet further. This means that they were not configured to send information back but are working fine.  
    
## What is load average?  
```
uptime
top
```
- Shows number of jobs in run queue waiting for cpu utilization averaged over 1 min, 5 mins and 15 mins.  
- eg: 1.0(for 1 core or 4.0 for 4 cores) means 100% i.e. jobs running one by one without any idle time.  
- eg: 1.3(for 1 core) means jobs are waiting for queue to clear.    
  
## If we are not able to connect to a particular port on localhost, what all can we troubleshoot?  
```
netstat --listen
``` 
  
## If all permissions and space is available but still we are not able to create a file, what could be the reason?  
todo  
  
## If a server is running slowly, what all can we troubleshoot? 
```
top # cpu idle time
vmstat 1 # no. of waiting processes for cpu  
vmstat 1 # free, cache, swap memory    
vmstat 1 # cpi utilization, idle, no. of waiting processes for cpu    
mpstat -P ALL 1 # cpu stats by core  
iostat -x 1 # disk utilization  
sar -n DEV 1 # network i/o utilization  
pidstat 1 # app cpu utilization  
strace -tp `pgrep <<appname>>` 2>&1|head -100 # system calls  
perf record -F 99 -a -g --sleep 10  # profile cpu usage  
```
  
## How to use awk?  
todo   
  
## How does boot process work?  
- BIOS - basic input output system
  - perform integrity checks
  - searches boot loader program in disk drive, sd card reader, cd/dvd rom, hard drive
  - executes the boot loader program
- MBR - master boot record
  - located in first sector of bootable disk i.e. /dev/sda or /dev/hda generally
  - less than 512 bytes in size
    - primary boot loader information
    - partition table info
    - mbr validation check
  - contains info about grub
- GRUB - grand unified boot loader
  - choose which kernel image to execute if we have many - else default selected from grub conf (/boot/grub/grub.conf)
  - has knowledge of file system
  - loads and executes kernel and initial ram disk images (temporary file system until kernel is booted and root file system is mounted)
- Kernel
  - mounts root file system as specified in grub conf
  - executes init program located in sbin folder
- init
  - first program being executed
  - process id 1
  - looks at /etc/inittab file to decide run level
- runlevel
  - decides which initial programs will be loaded at startup - single user, multiuser, reboot etc
  - executes programs as per current run level
  - directories are like /etc/rc.d/rc0.d/
  - programs are executed in appropriate directory
  - s - start
  - k - kill
  - sequence numbers for how to start and kill  
  
## If we delete a file and the system space is still not freed up, what could be the reason?  
- There may be a hardlink.  
- File may be open in some process.  
  
## How to check since when the system is up?  
```
uptime  
```

# process management commands

```
# start program
ctrl+z  # suspend program
bg  # move to background
fg  # move to foreground

kill <<pid>>

nice -n <<value>> <<pid>>  # set priority # -20 to 19 # default is 0
renice -n <<value>> <<pid>>  # change priority

df -h  # check free disk space  # -h for readability

free -m  # see free ram in mb
free -g  # see free ram in gb
```

# networking commands

## ifconfig
- interface config

## ping
- packet internet groper
- shows round return time to server
- uses icmp - internet control message protocol

## netstat
- shows open sockets, routing tables etc
- which ports server is listening on

## dig
- domain information groper

## nslookup  
- for dns information for ip address  
(resolver(isp) - root server - tld server - authoritative name server(s))  

# route
- shows routing table

## arp
- mac address to ip address and vice versa

## hostname
- get hostname

## curl and wget
- download files from internet

## tcpdump
- shows traffic passing through network

## ssh
- secure login
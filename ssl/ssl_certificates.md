# Purpose
- for data transferred from client to server

# Symmetric Encryption
- same key is used for encryption and decryption at client and server respectively
- not secure

# TLS - Public Key Encryption
- client initiates 
- server sends public key 
- client has symmetric key and encrypts it via public key and sends
- server decrypts using private key
- client encrypts data with symmetric key and sends
- client doesn't know if the public key is of server or sniffer 
- not secure

# Certificates
- server talks to certificate authority and it makes cert for public key and signs it
- CA has pub and private key
- signs with private key
- main cert linked to intermediate cert for cert authority for public key
- linked to root cert
- client to server starts
- server sends certs
- client verifies with cert authority by using public key of cert authority and encrypting public key of server and see if some content is received
- until root - root is self-signed
- root is on every machine - untrusted root if root goes down
- can install root
from cryptography.fernet import Fernet
data = b"{\"a\": \"b\"}"

key = Fernet.generate_key()
fnet = Fernet(key)

encrypted_data = fnet.encrypt(data)
print(encrypted_data)

decrypted_data = fnet.decrypt(encrypted_data)
print(decrypted_data)

# b'gAAAAABey_ZvnhRcWfvu4sdTdQRbXEqvcckXKyOZ9BRs8UDSyMMpXHAehV1hTVaSC89kx6i500H-WFmClsk_T9XeaXp3WX-sew=='
# b'{"a": "b"}'

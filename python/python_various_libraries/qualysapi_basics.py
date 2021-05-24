from qualysapi import connect
conn = connect(username="username",password="password",hostname="hostname")
params = {"action": "list", "vm_processed_after": "yyyy-mm-dd", "truncation_limit": 0, "details": "All", "output_format": "CSV_NO_METADATA", "status": "New,Active,Re-Opened"}
response = conn.request("xx.com/api/n.0/fo/xx/xx/", params)
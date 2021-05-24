import ldap3
LDAP_PAGED_RESULT_OID_STRING = "1.2.840.113556.1.4.319"
server = ldap3.Server("hostname", get_info=ldap3.ALL, mode=ldap3.IP_V4_PREFERRED, use_ssl=True)
with ldap3.Connection(server, authentication=ldap3.NTLM, auto_bind=True, password="password", read_only=True, receive_timeout=10, user="user") as ldap_connection:
    search_parameters = {"search_base": "base_dn", "search_filter": "(&(objectCategory=Group)(objectClass=group)(distinguishedName=xx))", "attributes": ["member"], "paged_size": 1000}
    while True:
        ldap_connection.search(**search_parameters)
        for entry in ldap_connection.entries:
            val = getattr(getattr(entry, "member"), "value", None)
        cookie = ldap_connection.result["controls"][LDAP_PAGED_RESULT_OID_STRING]["value"]["cookie"]
        if cookie:
            search_parameters["paged_cookie"] = cookie
        else:
            break

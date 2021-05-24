import grp

for g in grp.getgrall():
    print("group: {}".format(g.gr_name))
    for mem in g.gr_mem:
        print("member: {}".format(mem))
        exit()

# ...
# group: adm
# member: syslog

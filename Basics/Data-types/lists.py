server1 = "10.0.0.2"
server2 = "10.0.0.3"
servers = ["10.0.0.4", True, 123, 12345.69, 3.14]
print(type(servers), servers, server1, server2)
server1 = servers[0]
print("server1 ip address:", server1)
#slicing
simple_slice= servers[0:1]
print(simple_slice)
simple_slice= servers[0:4]
print(simple_slice)
simple_slice= servers[0:5:2]
print(simple_slice)
simple_slice= servers[-1:-3:-1]
print(simple_slice)
print(len(simple_slice))
print("Before modify:", servers)
servers[-3]=1234
print("After modify:", servers)
# print(dir(list))
"""
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
servers.append(False)
print(servers)

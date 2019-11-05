import pywbem

server_uri = 'http://ttm4128.item.ntnu.no:5988/root/cimv2'

conn = pywbem.WBEMConnection(server_uri)

# server = pywbem.WBEMServer(conn)

classNames = conn.EnumerateClassNames(DeepInheritance=True)
print(classNames)

import socket

def findServiceName():
    protocolname = 'tcp'
    for port in [80,25]:
        print("Port: %s =>service name : %s" %(port,socket.getservbyport(port,protocolname)))

    print("Port: %s =>service name : %s" % (53, socket.getservbyport(53, 'udp')))
    print("Port: %s =>service name : %s" % (53, socket.getservbyport(53, 'tcp')))

if __name__ == '__main__':
    findServiceName()
import socket
from binascii import hexlify

def convertIPv4Address():
    for IPAddr in ['127.0.0.1','192.168.0.1']:
        packedIPAddr=socket.inet_aton(IPAddr)
        unpackedIPAddr=socket.inet_ntoa(packedIPAddr)
        print("IP address : %s =>Packed : %s,Unpacked : %s" %(IPAddr,hexlify(packedIPAddr),unpackedIPAddr))

if __name__== '__main__':
    convertIPv4Address()

'''
将字符串形式的IP地址转换成打包后32位二进制形式
hexlify()将打包后的数据以十六进制的形式表示
'''
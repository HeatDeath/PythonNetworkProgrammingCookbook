import socket

def getRemoteMachineInfo():
    remoteHost='cn.bing.com'
    try:
        print("IP address is %s " %socket.gethostbyname(remoteHost))
    except socket.error as err_msg:
        print("%s:%s" %(remoteHost,err_msg))
    #如果执行函数gethostbyname（）的过程中出现了错误，这个错误将有try-except块处理


if __name__ == '__main__':
    getRemoteMachineInfo()
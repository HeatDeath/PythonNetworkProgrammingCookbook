import  socket

def printMachineInfo():
    hostName=socket.gethostname()   #该函数没有参数，返回所在主机或本地主机的名字
    print("Host name is  %s " %hostName)

    print("------------------------------")

    IpAddress=socket.gethostbyname(hostName)        #该函数接受一个参数hostname，返回对应的IP地址
    print("IP address is %s " %IpAddress)

if __name__  ==  '__main__':
    printMachineInfo()


# 端口检测器
import optparse
from socket import *
from threading import Thread
# 定义扫描函数
def connScan(tgtHost,tgtPort):
    try:
        # 尝试启动socket实例
        connSkt = socket(AF_INET,SOCK_STREAM)
        # 连接
        connSkt.connect((tgtHost,tgtPort)) 
        # 并打印tcp主机开放的端口号
        print("[+] %d/tcp open" % tgtPort)
        connSkt.close()
    except:
        #当tcp连接发生异常时则提示端口为关闭状态
        print("[-] %d/tcp closed"%tgtPort)
def portScan(tgtHost,tgtPorts):
    try:
        # 使用socket下的gethostbyname()方法获取目标主机域名的IP
        tgpIP = gethostbyname(tgtHost)
    except:
        # 解析失败时则返回未知域名
        print("[-] Cannot resolve '%s':Unknown Target Host"%tgtHost)
    try:
        # 通过gethostbyaddr反取主机名
        tgtName = gethostbyaddr(tgpIP)
        print("\n[+] Scan Results for: "+tgtName[0])
    except:
        print("\n[+] Scan Result for : "+tgpIP)
    # 设置默认超时重连1
    setdefaulttimeout(1)
    # 启用线程扫描
    for tgtPort in tgtPorts:
        print("Scanning port ： "+tgtPort)
        task = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        task.start()
def main():
    # 启动一个opt解析器实例
    parser = optparse.OptionParser("usage %prog -H <target host> -p <target port>")
    # 添加属性参数-H 主机名和-p 端口
    parser.add_option("-H", dest="target_host", type=str, help="specify target host")
    parser.add_option("-p", dest="target_port", type=int, help="specify target port[s] separated by comma")

    (options, args) = parser.parse_args()

    tgtHost = options.target_host
    tgtPorts = str(options.target_port).split(",")
    # 当tgtHost和tgtPort不为空时，返回解析器的占用情况
    if (tgtHost == None) | (tgtPorts[0] == None):
        print("[-] You must specify a target host and port[s]")
        exit(0)
    else:
        portScan(tgtHost,tgtPorts)
if __name__ == "__main__":
    main()
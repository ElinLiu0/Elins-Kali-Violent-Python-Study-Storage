# 端口检测器
import optparse
from socket import *
# 定义扫描函数
def connScan(tgtHost,tgtPort):
    try:
        # 尝试启动socket实例
        connSkt = socket(AF_INET,SOCK_STREAM)
        # 连接
        connSkt.connect((tgtHost,tgtPort)) 
        # 并打印tcp主机开放的端口号
        print("[+]%d/tcp open" % tgtPort)
        connSkt.close()
    except:
        #当tcp连接发生异常时则提示端口为关闭状态
        print("[-]%d/tcp closed"%tgtPort)
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
    for tgtPort in tgtPorts:
        print("Scanning port ： "+tgtPort)
        connScan(tgtHost,int(tgtPort))

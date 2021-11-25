# 使用optparse库来实现端口扫描
import optparse
# 启动一个opt解析器实例
parser = optparse.OptionParser("usage %prog -H <target host> -p <target port>")
# 添加属性参数-H 主机名和-p 端口
parser.add_option("-H", dest="target_host", type=str, help="specify target host")
parser.add_option("-p", dest="target_port", type=int, help="specify target port")

(options, args) = parser.parse_args()

tgtHost = options.target_host
tgtPort = options.target_port
# 当tgtHost和tgtPort不为空时，返回解析器的占用情况
if (tgtHost == None) | (tgtPort == None):
    print(parser.usage)
    exit(0)

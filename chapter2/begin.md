在开始本章节之前，你需要准备ftp服务。

教程来源：https://www.fujieace.com/kali-linux/vsftpd.html


一、什么是vsftpd？
vsftpd 是一个 UNIX 类操作系统上运行的服务器的名字，它可以运行在诸如 Linux, BSD, Solaris, HP-UX 以及 IRIX 上面。它支持很多其他的 FTP 服务器不支持的特征。

 

二、安装vsftpd
root@kali:~# apt-get update
root@kali:~# apt-get install vsftpd
 

三、配置vsftpd
root@kali:~# vim /etc/vsftpd.conf
 

一般vsftpd.conf配置选项设置如下：

# listen=YES
listen_ipv6=YES
# listen 和 listen_ipv6 开一个就行；两个都开，vsftpd就报错了

# 匿名用户访问
anonymous_enable=NO

# 本地用户访问
local_enable=YES
write_enable=YES
local_umask=022
anon_mkdir_write_enable=NO
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_file=/var/log/vsftpd.log

chroot_local_user=YES
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd.chroot_list

secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd

rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
各个选项具体含义参见默认的vsftpd.conf文件里面注释，主要重点讲下以下这几个参数含义：

chroot_local_user=YES

chroot_list_enable=YES

chroot_list_file=/etc/vsftpd.chroot_list

chroot_local_user设为YES的情况下，如果chroot_list_enable设为YES， 那么chroot_list_file里面列出的用户有权限访问用户主目录之外的目录。

一般情况下直接如不允许所有用户访问用户主目录之外的目录，直接chroot_local_user=NO即可！

 

四、增加用户组和用户
root@kali:~# groupadd ftpuser
root@kali:~# useradd -g ftpuser remote1
root@kali:~# mkdir -p /home/remote1
root@kali:~# passwd remote1
输入新的 UNIX 密码：
重新输入新的 UNIX 密码：
passwd：已成功更新密码
 

五、chroot权限控制
如果用户被允许访问主目录之外的目录(chroot=true)，则该用户通过ftp连接服务器可以访问其他用户或者用户组不开放的文件和目录之外的服务器上的大部分文件和目录；

所以，一般不允许用户访问主目录之外的目录(chroot=false)，此时ftp连接的时候往往会报错；此时需要更改用户主目录权限：

root@kali:~# chmod a-w /home/remote1
更改后用户ftp登录后无法在用户根目录下创建子目录和写文件；所以需要创建子目录，然后将文件写入到子目录中。

 

六、启动vsftpd服务
root@kali:/home# service vsftpd restart
root@kali:/home# service vsftpd status
service vsftpd status active (running) 

 

七、查看vsftpd端口监听状态，看vsftpd是否真正的成功？
root@kali:/home# netstat -nap | grep vsftpd
netstat -nap | grep vsftpd

 

八、用FTP客户端连接上ftp
ftp客户端可以使用FileZilla、WinSCP、xftp等软件，大家就自行去网上下载吧！

 

由于我是本地搭建，我就直接以“ftp://username:password@hostname:port”这种方式去连接FTP吧！

经过替换，我的正确FTP连接地址是“ftp://remote1:remote1@192.168.40.132:21”，最后成功效果如下图，显示是空的是因为我的“/home/remote1”目录是空的。

vsftpd连接FTP成功

 

总结：看此教程后，在最后一个步骤上可能你会遇到到“500 OOPS: could not read chroot() list file:/etc/vsftpd.chroot_list”错误这种情况，这个非常的简单不用担心。
#/bin/bash
#以nginx源码包在/root/lnmp_soft/下为例　解压到当前
tar -xf /root/lnmp_soft/nginx-1.12.2.tar.gz -C /root/lnmp_soft/
#进入源码包
cd /root/lnmp_soft/nginx-1.12.2
#创建无权限用户防止客户登录服务器有直接修改配置的权限
useradd -s /sbin/nologin nginx
#安装编译软件还有依赖包
yum -y install gcc openssl-devel pcre-devel

#运行脚本配置nginx配置（有需要的服务可以开启相对应的模块）
#配置nginx的所有者所属组是nginx　开启网站数据加密的模块　网页状态信息模块
./configure --user=nginx --group=nginx --with-http_ssl_module --with-http_stub_status_module

#编译
make && make install

#创建nginx快捷方式
ln -s /usr/local/nginx/sbin/nginx /sbin
#启动服务
nginx
#查看nginx版本
nginx -V
#查看端口默认80
netstat -ntulp

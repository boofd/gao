#/bin/bash
#以nginx源码包在/root/lnmp_soft/下为例　解压到当前
tar -xf /root/lnmp_soft/nginx-1.15.8.tar.gz -C /root/lnmp_soft/
#进入源码包
cd /root/lnmp_soft/nginx-1.15.8
#第一次安装nginx需要安装编译软件依赖包此次升级不需要安装直接运行脚本配置nginx
./configure --with-http_ssl_module --with-http_stub_status_module
#编译
make
#将原先的nginx启动程序修改名字
mv /usr/local/nginx/sbin/nginx /usr/local/nginx/sbin/nginx.back
#将新版nginx的启动程序复制到nginx目录下
cp /root/lnmp_soft/nginx-1.15.8/objs/nginx /usr/local/nginx/sbin/
#创建nginx快捷方式
ln -s /usr/local/nginx/sbin/nginx /sbin
#需要先停止服务　在启动服务
nginx -s stop
nginx
#查看nginx版本
nginx -V

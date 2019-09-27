#!/bin/bash
for i in 44
do
scp /home/student/桌面/redis-cluster-4.3.0.tgz root@192.168.4.$i:/root
ssh root@192.168.4.$i 'tar -xf redis-cluster-4.3.0.tgz;
yum -y install php-devel gcc;
cd redis-4.3.0;
phpize;
./configure --with-php-config=/usr/bin/php-config;
make && make install;
sed -i 's#; extension_dir = "./"#extension_dir = "/usr/lib64/php/modules/"#' /etc/php.ini;
sed -i 's#; extension_dir = "ext"#extension = "redis.so"#' /etc/php.ini;
systemctl restart php-fpm'
done

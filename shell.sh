1.使用while循环,统计1+2+3+..100的总和
#!/bin/bash
x=0
a=0
while [$x -le 100]
do
let x++
a=$[a+x]
done
echo $a

2. 编写脚本,使用for循环对2000以内的整数判断,是177倍数显示
#!/bin/bash
for i in `seq 2000'
do
x=$[i%177]
if [$x -eq 0];then
echo '$i是0的倍数'
fi

3.使用循环打印5*5的星星 
for i in {1..5}
do
for i in {1..5}
do
echo -n '*'
done
echo
done

4.编写脚本,通过三个read命令读取用户输入的三个任意数字,脚本对输入的三个数字求和输出

read -p '请输入数字' a
read -p '请输入数字' b
read -p '请输入数字' c
d=$[a+b+c]
echo $d

5.判断当前系统启动的进行数量,如果进程数量超过100个,则发送邮件给root报警
#!/bin/bash
a=`ps -aux | wc -l`
if [$a -gt 100];then
echo "有人入侵" | mail -s test root
fi

6.编写脚本,测试当前用户对/etc/passwd/文件是否具有读写执行权限
[-r /etc/passwd] && echo "当前用户有写权限" || echo "当前用户无写权限"
[-w /etc/passwd] && echo "当前用户有读权限" || echo "当前用户无读权限"
[-x /etc/passwd] && echo "当前用户有执行权限" || echo "当前用户无执行权限"

7.查看服务器状态信息的脚本
uptime | awk -F :'{print $5}'	#查看硬件状态信息
ifconfig eth0 | awk '/rx p/{print $5}'	#网卡流量接受字节
ifconfig eth0 | awk '/tx p/{print $5}' 	#网卡发送字节
free -m | awk '/Mem/{print $4}'		#查看运行内存
df -h | awk '/sda1/{print $4}'		#查看剩余可用空间
user=`cat /etc/passwd | wc -l`
echo "当前有$user人"			#查看服务器当前用户人数
a=`who | wc -l` 				
echo "当前有$a人登录服务器		#查看当前登录服务器的人数
b=`ps -aux | wc -l`
echo "当前进城数量为$b"			#查看当前进程数量


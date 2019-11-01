#!/home/student/nsd1906/bin/python
python3 =m venv ~/nsd1906 	#创建虚拟环境
source ~/nsd1906/bin/activate	#激活虚拟环境
python --version		#查看python版本
which python			#查看python命令
Pycharm是专门编写python程序的IDE
python的语法结构
python完全靠锁紧表达代码逻辑,缩进四个空格
注释采用#,续行采用\,与shell一样
同一行如果书写多条语句,可以用;分隔,与shell一致,但是可读性差,不推荐
# print ('hello wordl')	#字符串必须用引号引起来,单双引号无区别
print('hello world')
print('hello world')
print('hello wordl')
print('hello world')
print('hello world')
print('hello world')
print('hello world')
if 3 > 0:   print('yes')    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if 3 > 0:
    print('yes')
    print('no')
if  3>0:
    print('yes')
    print('no')
# if 3 > 0:
#     print('yes')
#     print('no')
# print ('hao' + '123')	#字符串拼接用+
print('hao'+'123')
print('hao'+'123')
print('hao'+'1123')
print('hao'+'123')
print('hao'+'123')
print('hao'+"123")
print('hao'+"123")
print('hao'+'123')
print('hao'+'123')
print('hao'+"123")
# print('hello word')
# print('hao', 123)	#打印多项,用逗号分隔,输出各项间默认都是空格
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
print('hao',123)
# print('hao', 123, sep='*****')	#设置输出的各项间以***作为分隔符
print('hao',123,sep='**')
print('hao',123,sep='**')
print('hao',123,sep='**')
print('hao',123,sep='**')
print('hao',123,sep='***')
print('hao',123,sep='***')
print('hao',123,sep='**')
print('hao',123,sep='**')
print('hao',123,sep='**')
print('hao',123,sep='**')
# user=input('username:')	#input读入的一定是字符串
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
user=input('')
# n=input('number')
n=input('')
n=input('')
n-input('')
n=input('')
n=input('')
n=input('')
n=input('')
n=input('')
n=input('')
n=input('')
# print(int(n) +5)	#int将字符串形式的数字转成真正的数字
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
print(int(n)+5)
# u=input()
# print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(n)+int(u))
print(int(u)+int(n))
# u=input('username')
# print (str(u), 'hellow ')	#str将对象转成字符串
print (str(u),'hello')
print (str(u),'hello')
print(str(u),'hello')
print(str(n),'hello')
print(str(n),'hello')
print(str(n),'hello')
print(str(n),'hello')
print(str(n),'hello')
print(ste(n),'hello')
print(str(n),'hello')
# print(u,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
print(n,'hello')
# print('欢迎%s' %u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%u)
print('欢迎%s'%s)
print('欢迎%s'%u)
# print('hello'+u)

变量
1.可以变化的量是变量,如a=10,以后还可以改变它,a=100
2.与变量相反的是字面量,如字符串'hello',数字100,都是字面量
3.写程序时,入股总是用字面量,就是硬编码
合法变量名的要求
1.首字符必须是字母或者下划线
2.其他字符可以是数字,字母,下划线
3.区分大小写
推荐的名称的写法
1.变量名全部用小写,尽量有意义,pythonstring
2.简短.pystr
3.多个单词间用下划先分隔,py_str
4.变量用名词,如phone;函数名用谓词(动词+名词),update_phone
5.类名采用驼峰的形式,MyClass
变量赋值自右向左,将=右边表达式的计算结果赋值给左边的变量
变量在使用之前必须赋值
a=10
a=a+5
a+=5
a+=10
b=10
b+=5
a-=10
b-=10
print(a+b)
5/3 1.6666666666666666667
5 //3 #只保留商 1
5%3 #求余,模运算
divmod(5,3) #5除以3,返回商和余数(1,2)
a,b=divmod(5,3) #将商和余数分别赋值给a和b
2 ** 3 #2的三次方
比较运算符
3==3
10>5>1 #python支持连续比较
20>10<30	#相当于是20>10 and 10<30
逻辑运算符,最终结果为true或false
10 > 50 and 2<5	false
10 > 5 and 2<5	true
2 * (3**2) 18
(not 10 > 50) or 2 < 5#涉及到可读性差的代码,应该加()
not 10 > 3 	#not是取反,真变假,假变真
数据类型概述
type (1.3)	#有小数点为浮点数
type(10)	#没有小数点为整数
true +1 	#2 true的值是1
flase + 1 	#1 flase的值是0
python默认使用10进制表示数字
如果以0o开头表示8进制数	#0o11 9
oct(10) 0o12	#将10进制数转为8进制数
0x11	17	#16进制以0x开头
hex(20)	0x14	#10进制转16进制
0b11	bin(7)	#2进制以0b开头
字符串:引号一起来的部分,单双引号没有任何区别
三引号就是三个连续的单引号或者双引号
words='hello\nweda\ngree'
print(words)
hello
weda
gree	print将\n转义为回车
三引号可以保存用户的输入格式
wds ='''hello
...welcaome
...gree'''
print(wds)
hello
welcaome
gree
wds 'hello\nwelcaome\ngree'
py=python
len (py)	#计算长度
py[0]		#去除下标为0的字符
py[6]		#下标超出范围将会报错
py[-1]		#下标为复数,表示自右向左
py[2:4]		#th 取切片,起始下标包含,结束下标不包含
py[2:6]		#thon	切片,不会出现下标越界的错误
py[2:]		#结束不写,表示取到结尾
py[:2]		#开头不写,表示从头取
py[:]		#从开头取到结尾
py[::2]		#切片默认步长为1,改为2
py[1::2]	#yhn
py[::-1]	#步长值为负,表示从右往左取
'abc'+'123'	#字符串拼接
py='good'	#python good
'*' * 30	#*号重复30遍
py * 5		#变量值重复五遍
't' in py	#t在字符串中吗
'th'in py	#th在字符串中吗
'to' in py 	#to在字符串中吗?不连续的字符为false

列表,与字符串类似,都是序列对象
alist=[1,2,3,'tom','he']	len alist 5
alist[0]	1
alist[3::]	['tom','he']
alist+[10,20]	[1,2,3,'tom','he',10,20]
alist*2 	[1,2,3,'tom','he',1,2,3,'tom','he']
alist.append('bob')	向列表尾部追加一个字符串

元组,可以认为它是不可变的列表
atup=(1,2,3,'bob','tom')
len(atup)	5
atup[3:]	('bob','tom')
atup[0]=10	#元组不可变,所以不能把他的元素重新赋值

字典:采用的key:val的形式
adic:{'name':'gao','year':10}
len(adic)	2
adic[0]		#字典是无序,所以没有下标
'tom'in adic	#tom是字典的key吗
adic['name']	#通过key找到val

数据类型的特点
按存储模型分类
标量:数据中不能包含其他类型数据。数字、字符串
容器:可以包含其他类型数据。列表、元组、字典
按更新模型分类
不可变:数字、字符串、元组
可变:列表、字典
按访问模型分类
直接:数字
顺序:字符串、列表、元组
映射:字典
55/3
5//3
5%3
divmod(5,3)
a,b=divmod(5,3)

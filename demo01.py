# 一，python常用方法
# 1.print()方法：用于进行打印输出    格式：print()        语法格式： print() #括号内跟具体要打印的信息
print('hello world')
print(1+1)
print(1+2)

# 2.type()方法：用于查看数据类型     格式：type(obj)
print(type("abc"))
print(type(222))

# 二. python常用变量
# 1，定义变量
#  格式 ： var_name = value    （var_name 变量名）  （value，变量值）
a = 10          #将数字10赋值给a
b = 6           #将数字6赋值给b
c = 'hello world'       #将数字'hello world'赋值给c
# 定义变量的其他方式
d,e,h = 8,0,'cat'            #将8,0,'cat'分别赋值给的d，e，h
g = a+b
# 2. 使用变量
print(a)
print(b)
print(c)
print(d)
print(g)
# 3，变量命名规范
# 1. 定义变量时，= 的左右应各保留一个空格
# 2. 如果变量是由两个或多个单词组成时： （每个单词都使用小写字母） （单词与单词之间使用_连接，如：qq_number,my_name）
# 3. 命名变量 ： 不能已数字开头     不能和关键字重名

# 三， python算数运算符
# 算数运算符
a,b= 8,4
print(a,b)
print(a+b)     #a+b 求和
print(a-b)     #a-b 求差
print(a*b)     #a*b 相乘
print(a/b)     #a/b 相除，返回的是浮点数
print(a//b)    #a//b 相除  整数 返回的数是整数
print(a%b)     #a%b 取余
print(a**b)    #a**b 次方

# 比较运算符
print(a>b)       #a 大于 b
print(a>=b)      #a 大于等于 b
print(a<b)       #a 小于 b
print(a<=b)      #a 小于等于 b
print(a ==b)     #a 等于 b
print(a!=b)      #a 不等于 b
print(a is b)    #两个对象引用相同
print(a is not b)   #两个对象引用不相同
# ‘==,!= 对比的是两个变量的值        is, is not 对比的是两个变量的内存地址

# 赋值运算符
a,b = 4,2
a+=b       #加赋值  a+=b   >>>>=  a = a+b
print(a)   # 所以a 现在等于6          所以a=6
a-=b       #减赋值  a—=b   >>>>=  a = a-b
print(a)   # 所以a 现在等于 a=6-2     所以a=4
a*=b       #乘赋值  a*=b   >>>>=  a = a*b
print(a)   # 所以a 现在等于 a=4*2     所以a=8
a/=b       #除赋值  a/=b   >>>>=  a = a/b
print(a)   #所以a 现在等于 a=8/2      所以a=4
a%=b       #取余数赋值  a%=b   >>>>=  a = a%b
print(a)   #所以a 现在等于 a=4%2      所以a=0
a**=b      #幂赋值  a**=b   >>>>=  a = a**b
print(a)   #所以a 现在等于 a=0**2    所以a=0
a//=b      #取整数赋值  a//=b   >>>>=  a = a//b
print(a)   #所以a 现在等于 a=0//2    所以a=0

#逻辑运算符
# 1. a and b  ==> 两个条件都满足 ，返回真 ，否则返回假
a,b = 4,6
print(a,b)
print(a > 3 and b < 10 )   #a大于3 ， b小于10  所以输出值为正确 true
print(a > 3 and b > 6 )    #a大于3   b大于6是错误的条件  所以输出值为 false

# 2. a or b ==> 两个条件满足其一返回真，否则返回假
print(a > 3 or b >10)     #a大于3 是正确的条件  b大于10 为错误的条件  所以or 满足其中一个条件 输出值为 true
print(a < 2 or b >10)     #a小于2   b大于10 都是错误的条件  所以输出值为 false

# 3. not a  ==> 条件为真 ，加上not变成假 ，反之变成真 。
print(not a > 2)   a大于2 条件是真的 加上 not 就为假 所以输出值为假 False
print(not a < 2)   a小于2 条件是假的 加上 not 就为真 所以输出值为真 True

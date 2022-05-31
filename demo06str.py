
#格式化字符串str  使用符号 %s
my_str = "my nmae is %s" % ("张四")   #可以随意改变变量值
print(my_str)

#格式化整数 使用 %d
my_str1 = "张三今年 %d岁" % (56)
print(my_str1)

#格式化浮点数  使用 %f
my_str2 = "苹果一斤%f元" % (5)
print(my_str2)

#辅助指令：m,n
my_str3 = "苹果一斤%6.2f元" % (5.66798)
print(my_str3)

#显示左对齐: —
my_str4 = "苹果一斤%-6.2f元" % (5.667)
print(my_str4)

#在数字前面显示加号(+)
my_str5 = "苹果一斤%+6.2f元" % (5.667)
print(my_str5)

#在数字前面显示加号(+) 并且左对齐 -
my_str6 = "苹果一斤%+-6.2f元" % (5.667)
print(my_str6)

#在数字前加 空格
my_str6 = "苹果一斤% 8.2f元" % (5.667)
print(my_str6)

#在数字前加 空格 把空格换成 0
my_str7 = "苹果一斤%08.2f元" % (5.667)
print(my_str7)



# 二。使用format()方法进行字符串格式化
# "{}".format("字符串)
my_str8 = "张三 今年 {}岁".format(25)   #可以随便改值
print(my_str8)

my_str9 = "今天星期{},张三今年{}岁".format('四','25')   #可以随便改值
print(my_str9)

my_str10 = "我是位置参数{0} {1}".format('hello','python')  #0代表着值的第一个数'hello'，1代表值的第二个数'python'
print(my_str10)                                          #2代表值的第三个数

#format的关键字参数: "{x}{y}".format(x='hello',y='world')
my_str11 = "今天星期{x},张三今年{y}岁".format(y='四',x='25')   #可以随便改值
print(my_str11)

#位置参数和关键字参数可以结合起来使用，: “{0}{x}”.format('hello',x='world')
my_str12 = "今天星期{0},张三今年{x}岁".format('四',x='25')   #x不管在那个位置 都会去找x的值   0代表着第值的第1位
print(my_str12)


print('=============================================')

#字符串方法演示

#1.字符串分割：join(seq
astr = 'hello'
bstr = astr.join('world')
print(bstr)

a = '+'
b =a.join('1234')
print(b)

#2.分割字符串 ：split(str="") 其中str代表分隔符
cstr ="hello world php"
dstr =cstr.split(" ")
print(dstr)

cstr1 ="hello+world+php 3"
dstr1 =cstr1.split("+")
print(dstr1)

cstr2 ="helloworlfphpove"
dstr2 =cstr2.split("o")
print(dstr2)

#查找字符串: find(substr) 如果找到了返回的是最小索引，没有找到返回——1
estr = 'helloworld'        #开头的是0，1，2...
print(estr.find('l'))
print(estr.find('d'))
print(estr.find('c'))


#查找xxx结尾的字符串： endswith('xxx')
fstr = "小说.txt"
if fstr.endswith('.txt'):
    print("它是一个txt文档")


#替换字符串 ： replace(old_value,new_value)
gstr = "张三 李四 七七"
hstr=gstr.replace('张三','九九')
print(hstr)

#返回字符串的长度
gstr1 = '张三 李四 七七'
print(len(gstr1))

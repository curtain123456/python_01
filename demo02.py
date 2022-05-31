
# 一 ， 条件语句
"""
1.格式：
if 条件语句:
    执行代码块
"""
#例：
a = 10
if a >13:
    print("a是大于13的数")
else:
    print("a是小于13的数")
"""
2.多条件判断方式
if 条件判断1:
代码1
elif 条件判断2:
代码2
elif 条件判断3：
代码3
else:
代码4
"""
#例：
score = 75
if score > 90:
    print("优秀")
elif score > 80:
    print("良好")
elif score > 60:
    print("及格")
else:
    print("不及格")

if score > 75 and score <90 :
    print("良")
 #3. 各数据类型的返回值
if 1:
    print("hello world")
a = 0
if a:
    print("整数0返回的是True")
else:
    print("整数0返回的是False")

if "":
    print(空字符串返回的是False)
if "aaa":
    print("hello2")   # 字符串，对于空字符串为返回False，其它值返回True

if None:
    print("None返回为Fale")
if 2:
    print("非None值为True")
# 列表|元组|字典，对于空列表，空元组，空字典都是返回False，非空值返回True.

"""
is 和 in
is ： 判断两个对象的引用地址是否相等
in :  判断一个元素是否在另外一个元素中 。
"""
a = 257
b = 257
print(a is b)

#语法格式：
#obj in obj

a = '我是一个字符串'
b = '我是'
if b in a:
    print('在字符串内')
else:
    print('不在字符串内')

a_str = "hello"
b_str = "helloworld"
print(a_str in b_str)


print('==========================')




kk = input('输入一行字符')
zm=0
kg=0
sz=0
qt=0
for x in kk:
    if kk.isdigit():
        sz+=1
    elif kk.isalpha():
        zm+=1
    elif kk.isspace():
        kg+=1
    else:
       qt+=1
print('数字:',sz)
print('字母:',zm)
print('空格:',kg)
print('其他:',qt)





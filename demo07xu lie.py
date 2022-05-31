

#序列的通用操作

#1.所有— 列表,序列,字符串
# 创建列表  从左往右取 最左边从0开始   0是第一个值‘red’ 1是第二个值”小李“
lst = ['red','小李','无','七七']
print(lst[1])
# 从右往左取 最右边从1开始
lst = ['red','小李','无','七七']
print(lst[-3])

#创建元组
tp= ('red','小李','无','七七')
print(tp[1])
print(tp[-3])

#创建字符串
kk = 'hello'
print(kk[1])
print(kk[-4])


#二，切片 sep[start:end:step]  start代表开始位置，默认从0开始，
 #end代表结束位置，如果不填写，代表列表的长度。
# step代表的是步长，默认是1
v =[1,2,3,4,5,6,7]
print('获取第2-5个元素:',v[1:5:1])
print('获取偶数的值:',v[1:7:2])
print('获取奇数的元素:',v[::2])  #print('获取奇数的元素:',v[0:7:2])
print("获取第3个及后面的元素:",v[2:])  #print(v[2:7:1])
print('获取第2个及后面的元素且步长为2:',v[1::2])  #省略的是end
print("获取第3个及前面的元素:",v[:3:])  #省略了 start和step

#元组切片
x =(1,2,3,4,5,6,7)
print('获取第2-5个元素:',x[1:5:1])
print('获取第偶数元素:',x[1:7:2])

#字符串切片
l ='hellopl'
print('获取第2-5个元素:',l[1:5:1])
print('获取第偶数元素:',l[1:7:2])

#列表中有十个元素，取出来奇数个数的元素、
#print('某定义'[::2])


#三 。 序列的相加和相乘: +,*
alst = [1,2]
blst = [2,4]
clst = alst + blst
print(clst)

astr = 'hello'
bstr ='world'
cstr =astr + bstr
print(cstr)

dlst =alst *2   #2个数值变成4个
print(dlst)

print('=' * 30)

#4,检查元素 in ,针对的是列表 ，元组 ，字符串
lst5 = ['red','green','blue','black','gold','orange']
print('red' in lst5)
print(1 in lst5)


#序列中的方法 list()  将序列转换成列表
klst = list()
print(klst)

cstr = 'abcd'
kstr = list(cstr)
print(kstr)

#序列中的方法 dstr()  将序列转换成字符串
h = ['a','b','c']
u = str(h)
print(u)
print(type(u))
for x in u:
    print(x)

#enumernte  循环序列中的索引和值
lst7 = ['red','green','blue','black','gold','orange']
for y,x in enumerate(lst7):
    print(y,'===',x)


print('='* 40)
#5.列表推导式
# 格式 ：[ expB for x in iterable expA ]
# expB ：对x的运算，如加，减，乘，除以及条件判断等
#  for x in iterable  循环序列
#  expA  条件筛选或再次循环
#  [表达式 循环体 表达式 ] 执行的顺序： 先执行循环体，其次执行后面的表达式1，最后执行表达式2

# 生成一个1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)

lst1 = [x for x in range(1,11)]
print(lst1)

# 生成一个1-10的列表 要求只打印奇数
lst2 = [x for x in range(1,11) if x %2 != 0]
print(lst2)

# 生成一个1-10的列表 生成的奇数的值再加上10
lst3 = [x+10 for x in range(1,11) if x %2 != 0]
print(lst3)
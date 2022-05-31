"""
一 ， for 循环
格式：
for 循环变量 in 序列
    代码块
"""
#实例：循环某个字符串中的每个字符
v = '123456'
for x in v:
    print(x)

# while 循环
"""
while 条件语句(condition)：
代码块(statements)……

"""
# 实例：打印1~5的所有数字
a = 1
while a<=5:
    print(a)
    a+=1  #a=a+1

# 练习：计算1~100内所有数的和
sum = 0
a = 1
while a<=100:
    sum+=a
    a+=1
print(sum)

# range函数
"""
range(start,end,step)
start : 开始索引，默认是从0开始 ，可以忽略
end : 代表结束 ，必选项
step : 步长 ，默认就是1
"""
# 需求1 ： 打印1-10的数

# for 循环变量 in 序列
for x in range(0,10,1):
    print(x)
# 需求2：  开始位置为1，循环到10
for x in range(1,10,1):
    print(x)
#需求 3： 开始位置1 ，循环到10 ，步长为2
for x in range(1,10,2):
    print(x)

# break语句断开循环
# 需求 ： 循环1-10，当遇到7退出循环
for x in range(1,10,1):
    print(x)
    if x == 7:
        break

# continue语句进行跳出本次循环
# 需求 ： 循环1-10，当遇到7跳过该次循环
for x in range(1,10,1):
    if  x == 7:
     continue
    print(x)

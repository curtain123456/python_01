# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a,b,c,d = 4,5,2,1
print(a+b-c*d)
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for v in range(1,101,1):
    if v % 3 == 0:
     sum+=v
print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
for v in range(1,11,2):
    print(v)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum = 0
sum1 = 0
for x in range(1,101):
    if x% 2 == 0:
        sum += x
    else:
        sum1 += x
print(sum-sum1)

# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1,101):
    sum+=x
print(sum)

# 6. 判断一个数n能同时被3和5整除
n = input('请输入一个整数')
if int(n) % 3 == 0 and int(n) % 5 == 0:
    print("被3和5整除")
else:
    print("不能被3和5整除")
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
v = input('请输入一个整数')
if 1 < int(v) <= 100:
    print('hello')
else:
    print('world')

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
list = []
x = input('请输入一个整数:')
y = input('请输入一个整数:')
z = input('请输入一个整数:')
list.append(x)
list.append(y)
list.append(z)
print(list)
print(list.sort())
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示， 60分以下的用C表示。备注：需要使用input()方法
score = int(input('请输入你的分数'))
if score >= 90:
    print('A')
elif score >= 60 and score <= 89:
    print('B')
else:
    print('C')

# 10. 将一个列表的数据复制到另一个列表中。
k1 = [1,2,3]
k2 = [4,5,6]
k1.extend(k2)
print(k1)

# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='')
    print()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
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
print('数字',sz)
print('字母',zm)
print('空格',kg)
print('其他',qt)

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制

#14. 题目：打印出如下图案（菱形）:
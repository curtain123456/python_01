# 一,函数
# 所谓的函数，就是具有特定功能的代码块。
"""
def 函数名字(参数列表)：
    代码块
"""
#函数相加
def add(x,y):     #参数列表
    z =x+y
    return z
#调用函数
print(add(4,5))
print(add(4,5.5))
print(add('hello','world'))

def add(x,y):
      return x + y       ##直接返回参与运算后的结果


#位置参数
def aad1(x,y):      # 定义了两个形参，调用该方法时必须传入两个参数值，传多或传少都会报错
    z = x+ y
    return z
print(add(5,6))        # 正确
print(add('red','blue'))   #正确
# print(add(5,6，7))    #报错
# print(add(5))    #报错


# 关键字参数 ：  #当关键字参数和位置参数混合使用时，
# 位置参数必须在前，关键字参数在后，否则会报错。
def student_lesson(grade,subject):
    z='{}年纪上{}课'.format(grade,subject)
    return z
print(student_lesson(3,'英语'))  #位置参数
print(student_lesson(grade=3,subject='语文'))  #关键字参数
print(student_lesson(subject='数学',grade=4))    #关键字参数可以调换位置
print(student_lesson(3,subject='生物'))     #关键字参数和位置参数混合使用。


#默认参数 ： 其中某个参数会有默认值  如果设置默认参数，需将在位置参数后 。

def study_language(name,language='python'):     #language默认值为'python'
   info = ("{}要学习{}语言".format(name,language))
   return info
print(study_language('七七','java'))  # 调用函数时，给language传递值java
print(study_language('六六',language='mysql'))
print(study_language('九九'))  # 调用函数时，给language不传递任何值

#可变化参数: 参数的个数是可以进行变化的，它有两种形式 列表形式和字典形式
# 分别是用来接收列表形式的可变参数，调用函数时跟位置参数一样
# 用来接收字典形式的可变参数 。调用函数时跟为关键字参数一样。
# 可变参数和位置参数，关键字参数最大的不同就是传递参数的数量不受限制 。
"""
语法格式：
def fun_name(a,b,*args):
   pass
"""


#定义列表形式    列表，元组可变参数
def add(x,y,*args):
   # print(args)
    z = x+y +sum(args)
    return z

print(add(4,5))  #x=4 y =5
print(add(4,5,6,8,7))      #传递多个参数   args = 6,8,7

#使用列表的方法进行调用
print(add(4,5,*[6,7,8]))  #传入列表，注意，列表前需要加*
print(add(4,5,*(6,7,8)))  #传入元组，注意，元组前需要加*

# 2.可变化参数 ----   字典可变参数
def k(**kwargs):
    print(kwargs)

print(k(a='hello',b=1,c=2))

dt_date ={'x':1,'y':2,'z':3}
print(k(**dt_date))


def show_info(**kwargs):
    print(kwargs)

print(show_info())      #可变参数也可以不传入任何参数
print(show_info(key1="python"))     #传入一个参数
print(show_info(key1="python",key2='java'))     #传入多个参数
print(show_info(**{'key1':'python','key2':'java'}))   #传入列表，注意，列表前需要加*



##  同样的位置参数和可变参数结合起来使用。也可以将可变参数列表和字典形式结合起来使用 。
def fun_name(*args,**kwargs):
    print(fun_name(''))   #此函数可以接收任何长度，任何位置，任何关键字的参数





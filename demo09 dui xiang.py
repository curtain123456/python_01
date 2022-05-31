
#面向对象：
"""
1.先定义一个类
2.在类里面申明属性（数据）和方法（函数）
3.定义一个具体的对象 叫初始化对象   对象是一个实实在在的对象。  ===>初始化对象 ： 对象名 = 类名
4.使用对象调用方法或者属性： 对象名.属性 || 对像名.方法
"""

##需求 设计一个电梯
# ===使用函数去实现

# 打开电梯
def start():
    print('函数-打开电梯')
# 关闭电梯
def oppn():
    print('函数-关闭电梯')
# 运行电梯
def run():
    print('函数-运行电梯')

start()
oppn()
run()

# 面向对象
# 1.定义一个电梯的类  class 类名()
class Elevator():
    # 2.在类的里申明车的属性(数据)和方法(函数)
    button = "开/关"
    floor = 15
    peple_nums = 13

    #打开电梯
    def start(self):
        print("面向对象-打开电梯")
    #关闭电梯
    def stop(self):
        print("面向对象-关闭电梯")

     #运行电梯
    def run(self):
        print('面向对象-运行电梯')
# 3.定义一个具体的对象 ，叫初始化对象 ，对象是一个实实在在的对象。
e = Elevator()
# 4.使用对象调用方法或者属性 : 对象名.属性 || 对象名.方法
e.stop()
e.stop()
e.run()






# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Students():
    name = ''
    grade = ''

    def study(self):
        print("{}年级的学生{}在上课".format(self.grade,self.name))

s1 = Students()
s1.name = '七七'
s1.grade =  '4'
print(s1.study())

s2 = Students()
s2.name = '六六'
s2.grade = '5'
print(s2.study())

# 使用构造方法来完成需求
"""
语法格式：
def __init__(self,...):
代码块
"""
class Students():
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def study(self):
        print('学生{},{}年级'.format(self.name,self.grade))

s3 = Students('张三',8)
s3.study()


# 2.4变量
"""
1. 在类中的变量主要包括类变量，实例变量和局部变量
"""
"""
1.类变量：
2.所有类的实例化对象都同时共享类变量，属于类的公共资源数据。
3.类方法的调用方式有 2 种，既可以使用类名直接调用，也可以使用类的实例化对象调用。
"""
#例：
class stu():
    name = ''
    grade = ''

#通过实例调用
k = stu()
k.name = '孙悟空'
k.grade = '6'
print(k.name)
print(k.grade)

#通过类名调用
stu.name = '八戒'
print(stu.name)

"""
实例变量:
1.实例变量指的是在任意类方法内部，以“self.变量名”的方式定义的变量，
2.其特点是只作用于调用方法的对象。
3.实例变量只能通过对象名访问，无法通过类名访问。
"""
class vv():
    def __init__(self,name,grade):
       self.name= name
       self.grade = grade

x = vv('阿珂',6)
print(x.name)
print(x.grade)


"""
局部变量：
1.局部变量直接在方法内定义的变量且以“变量名=值”的方式进行定义
2.局部变量的使用范围也仅限于所定义的方法内
"""
class g():
    def std(self,name):
        val = 'hello'
        print('{} {}'.format(val,name))

o = g()
o.std("唐僧")
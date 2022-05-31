"""
一，封装
1.不希望某部数据或功能被外界去使用和访问，
可以通过在变量或方法前个单下划线(_)或双下划线(__)
"""

class Students():
    name = '七七'
    __score = '78'    #如果是以_下划线开头的方法和属性，则是无法导入的。
                      #如果是以__下划线开头的方法和数学，则是无法直接调用的

    def __set_score(self,score):
        self.__score = score

    def get_score(self):
        return self.__score


print(Students.name)
#print(Students.__score)
s = Students()
#s.__set_score()
s.get_score()


"""
二,继承
1.必选具有父子关系  有父类和子类
2.在子类中可以直接调用父类的属性(数据)和方法(功能)
"""

#父类-人类
class People():
    def eat(self,ids):
       print("{}吃饭".format(ids))
#子类-学生类
class Students(People):
     def study(self):
        print("学习")
#子类-老师类
class Teacher(People):
    def teach(self):
        print("教书")

s = Students()
s.eat("学生")
t = Students()
t.eat("老师")


"""
三，类的多肽
1.
"""
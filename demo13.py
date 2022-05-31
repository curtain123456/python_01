# os 模块
import os

print(os.listdir())  #返回当前路径下的所有文件和文件夹

print(os.getcwd())   #返回当前的工作目录

#print(os.path.exists('C:\Users\小冰\PycharmProjects\python_01’))  #判断当前路径是否存在




#datetime 模块
import datetime

#当前时间
print(datetime.datetime.now())






"""
5.1try ... except语句
#语法格式：
try:
  正常代码块
except Exception as e:
  处理异常的代码块

"""

def div(x,y):
    try:
        z = x / y
        return z
    except exception as e:
        print("除法不能出现被0除的情况")

print(div(3,4))
print(div(3,0))
print(div(6,6))



"""
5.2try...except...finally语句
#语法格式：
try:
  正常代码块
except Exception as e:
  处理异常的代码块
finally
 必须要执行的码块
"""

f = None
try:
    f = open("aac.txt",'r')
    contents = f.readline()
    for x in contents:
          print(x)
except Exception as e:
    print(e)
finally:
  if f:
       f.close()
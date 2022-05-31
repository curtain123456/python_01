
""""
#导入其他包下的莫块
from work.work2 import x

from ../demo03 import work.work3
"""


#main : __main__

def div(x,y):
    try:
        z = x / y
        return z
    except exception as e:
        print("除法不能出现被0除的情况")
print(div(3,4))


if __name__ == '__main__':
    print(div(3,4))
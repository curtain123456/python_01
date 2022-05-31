"""
一, python 序列
列表 list
# 语法：
变量名 = []
#说明：定义列表需要使用[],[]内可以存放任何的数据类型
"""
list = ['red'] #定义空列表
list2 = [6,8,9,'one','two']
print(list)
print(list2)

# 循环列表 ：
# for x in blst:
#     print("列表中的值:",x)

for x in list2:
    print("列表中的值:",x)

# 1.列表的方法
cat = [1,2,3,6,6,'blue']
# 向列表中添加元素 : list.append(obj) ,列表的元素
cat.append(9)
print("使用append添加元素后的列表:",cat)

# 向列表中追加一个其它列表内的元素 : list.extend(seq)
cat.extend(list)
print("追加list后的结果:",cat)

# 列表翻转 ： list.reverse()
cat.reverse()
print("翻转后的结果:",cat)

# 统计在列表中出现的次数 ：list.count(obj)
print(cat.count(6))

# 从列表中找出某个元素的位置: list.index(obj)
print(cat.index(2))

# 向列表中的某个位置插入元素 ： list.insert(index,obj)
cat.insert(3,'black')
print(cat)


# 3. 元组
# 语法：
#变量名 = ()
#说明：定义列表需要使用(),()内可以存放任何的数据类型

tp1 = ()
tp2 = (4,5,6)
print(tp1)
print(tp2)

#语法：
#for 元素 in 元组:
#代码块
#说明：通过for循环，会将元组中的元素依次遍历，然后给到元素

for v in tp2:
    print(v)

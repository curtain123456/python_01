# 一，字典
# 1. 字典的定义 ： 变量名 = {key1:value1 , key2:value2}
#  语法格式： d = {key1:value1,key2:value2}
# 创建字典
a1 = {}
a2 = {'one':1,'two':2,'three':3}
a3 = {'five':5,'six':6}
print(a1)
print(a2)

# 2. 字典的获取 : a['键名']
print("获取字典a2中键名为one的值:",a2['one'])
# print("获取字典a2中键名为for的值:",a2['for'])     # 键名不存在会报错

# 字典的获取 ：a.get(键名)  另一种格式
# 获取字典a2中键名为two的值
print("获取字典a2中键名为two的值:",a2.get('two'))
#print("获取字典dct2中键名为d的值:",dct2.get('d'))  键名不存在会报错

# 3. 更新字典的某个值 ：dict['键名'] = 新值
a2 ['for'] = 4
print(a2)

# 二，字典中常见方法
# 4. 更新字典里的值到另外一个字典 ：dict.update(dict1)
a2.update(a3)
print("更新后的字典显示:",a2)

# 5. 判断字典中是否存在某个键名 : '键名' in dict
print('one' in a2)
print('six' in a2)

# 6.获取字典中所有的键名 ： dict.keys()
print('获取a2字典中所有的键名',a2.keys())
for v in a2.keys():   #循环
    print(v)

# 7.获取字典中所有的值 ：dict.values()
print('获取a2字典中所有的值',a2.values())
for x in a2.values():
    print(x)

# 8.获取字典中所有的键值对 ：dict.items()
print('获取字典中所有的键值对',a2.items())
for s,y in a2.items():
    print(s,y)
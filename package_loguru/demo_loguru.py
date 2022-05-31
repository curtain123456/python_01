
#loguru 模块

"""
功能：
1.可以格式化日志
2.着色（不同的颜色）
3.生成到文件
4.显示不同的日志级别
5.只使用一个对象（非常方便）


日志级别
debug : 调试日志
info ：普通日志
warning ：警告日志
success ：成功日志
error ：错误日志
"""
"""
logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")
"""

#1. 下载安装： pip install loguru

#2. 导包
from loguru import logger

# 3. 打印一条日志：hello world
logger.info('hello world')
logger.info('这是一条info普通日志')
logger.debug('这是一条debug调试日志')
logger.warning('这是一条warning警告日志')
logger.success('这是一条success成功日志')
logger.error('这是一条error错误日志')


#3.输出文件
"""
add()方法，用于将日志写到本地文件中         file_name 代表的是输出日志文件名
 format ：设置格式化                     format 代表的是输出的格式    
level ：设置级别                        time 时间 | level  级别 | module 模块名 | line 行数 | message 消息

"""
logger.add('a.log',format='{time} | {level} | {module} | {line} | {message}',level='DEBUG')
logger.info('这是一条info普通日志')
logger.debug('这是一条debug调试日志')
logger.warning('这是一条warning警告日志')
logger.success('这是一条success成功日志')
logger.error('这是一条error错误日志')

#  4. 字符串格式化
#  Loguru倾向于使用更加优雅和强大的 {} 进行格式化，日志记录功能实际上等效于 str.format() 。
# 进行传入参数的格式化
logger.info('我的名字叫{张三},今天星期{6}')
# -*- coding=utf-8 -*-

from sys import argv
#导入时间包
import time

script,filename = argv

#要想往文件写内容，必须打开文件的时候定义成可写的
txt = open(filename,'w')

#清空文档
txt.truncate()
#定义要输入的句子和换行符号
line1 = "The first."
line2 = "The second."
line3 = "The third."
n = "\n"
#往文档里面写内容
txt.write(line1)
txt.write(n)
txt.write(line2)
txt.write(n)
txt.write(line3)
txt.write(n)
txt.write("The end")

#重新打开文档
txt = open(filename)

#读取文档内容，并打印出来
print txt.read()
#等待5秒钟
time.sleep(5)

#关闭文档
txt.close

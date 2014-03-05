# -*- coding=utf-8 -*-

from sys import argv

script,filename = argv
#打开的文件赋值给一个对象变量，这个对象变量代表着一个打开的文件。用open方法
text = open(filename)

print "Here is your file %s:" %filename

#输出这个文件的内容，用这个对象的read方法
print text.read()

print "Type the filename again:"

#重新输入一个文件名

file_again = raw_input(">>>>>")

#打开重新输入的文件，赋值给一个对象变量
txt_again = open(file_again)

#读取这个重新打开的文件，用这个对象的read方法

print txt_again.read()


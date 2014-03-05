#-*- coding=utf-8 -*-

#定义方法，注意定义完成后一定要用：号，另外函数内的实现都要进行缩进。

from sys import argv

script,input_file = argv #运行的时候输入两个参数，这两个参数分别被赋值给script和input_file两个变量

def print_all(f):
	print f.read()   #定义一个方法，这个方法可以输入一个文件对象，然后打印出这个文件对象的内容


def rewind(f):
	f.seek(0)  #定义一个方法，这个方法是回到文件对象的开始
	
def print_a_line(line_count,f):
	print line_count,f.readline()  #定义一个方法，这个方法是指定行号和文件对象，打印出输入的行号和读取文件对象的第一行，如果再调用一下readline（）就会读取第2行。

	
current_file = open(input_file) #通过输入参数打开一个文件，把这个文件对象赋值给current_file.

print_all(current_file) #打印出文件的内容

rewind(current_file)#磁头定位到文件的开始

current_line = 1
print_a_line(current_line,current_file) #打印行号1和第一行的内容，现在磁头移向下一行

current_line = current_line+1
print_a_line(current_line,current_file) #打印行号2和第二行的内容，现在磁头移向第三行

current_line = current_line+1
print_a_line(current_line,current_file) #打印行号2和第二行的内容，现在磁头移向第三行


	

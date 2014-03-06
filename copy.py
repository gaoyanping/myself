# -*- coding=utf-8 -*-

from sys import argv
import time
#from os.path import exists

script,filename_from,filename_to = argv

#打开文件，把文件的内容读出来，然后赋值给一个变量,关闭这个文件
from_txt = open(filename_from)
txt_out = from_txt.read()
print txt_out
from_txt.close

#打开另外一个文件，清空文件，然后把第一个文件读出来的内容写进这个打开的文件，赋值成一个新的对象，关闭这个文件
to_txt = open(filename_to,'w')
to_txt.truncate()
to_txt.write(txt_out)
to_txt.close

#打开新的filename_to,读出其中的内容，然后打印出来。不过目前这样做有问题，最后打印不出来这些内容,调用a.read()没有成功！！！
print "test--------------"
a = open(filename_to)
b = a.read()
print b
time.sleep(3)
a.close








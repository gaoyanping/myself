# -*- coding=utf-8 -*-

#引入参数包从sys类中
from sys import argv

#将参数变量包解开，依次将参数放到左边的每一个变量中
script,first,second,third = argv
#python 运行后面的都叫参数，所以运行python argument.py one two three，运行的时候要给每个参数变量赋值
print "The script is called:",script  #arument.py,注意：被运行的文件名字也算一个参数了
print "The first variable is:",first   #one
print "The second variable is:",second  #two
print "The third variable is:",third    #three






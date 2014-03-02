#-*- coding=utf-8 -*-
#关于row_input的作用

a = 50
b = 60
c = raw_input()
#rwa_input()默认的是字符
print "c is %s" %c
#将int型转换成字符型
print str(a)+str(b)+c

#可以将raw_input()转换成int型的
d = int(raw_input())
print a+b+d

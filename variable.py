#-*- coding=utf-8 -*-
#变量的定义和打印,以及输出变量的方式,和字符串的格式化

cars = 100.00
drivers = 50.00
bike = "bike"
w= "wo"
e= "is"
print "drivers can dirver %d cars." % (cars/drivers)
print "I have %s cars" %cars
print "T have %r drivers" %drivers
print "I have",cars,"cars",drivers,"drivers"
#对于%r，会打印出所有的字符,另外可以用到转义符号
print "I have %r" %bike
print 'I have \"%s\"' %bike

print w+e
#-*- coding=utf-8 -*-

#定义方法，注意定义完成后一定要用：号，另外函数内的实现都要进行缩进。
def print_two(*args):#表示有多个参数
	arg1,arg2 = args #用两个变量去接受输入的两个参数
	print "arg1:%s , arg2:%s" %(arg1,arg2)
	
	
def print_three(*args):#表示有多个参数
	arg1,arg2,arg3 = args #用三个变量去接受输入的两个参数
	print "arg1:%s,arg2:%s,arg3:%s" %(arg1,arg2,arg3)

def print_two_again(arg1,arg2):
	print "arg1:%s , arg2:%s" %(arg1,arg2)
	
def print_one(arg1):
	print "arg:%s" %arg1
	

#直接调用函数	
print_two("a","b")

print_two_again("c","d")

print_three("g","h","I")

print_one("e")


def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates #表示这个函数返回三个值
	
start_point = 10000

beans,jar,crate = secret_formula (start_point) #表示函数返回的三个值分别用beans，jar和crate去存
print secret_formula(start_point) 
print beans
print jar
print crate


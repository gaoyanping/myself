#-*- coding=utf-8 -*-

#关于for的使用方法

The_count = [1,2,3,4,5]
for number in The_count:  #遍历The_count中的所有元素
	print "The number is %s" %number
	
	
elements = []
for i in range(0,6):  #遍历range中的所有元素
	print "The i is %s" %i
	elements.append(i) #在列表的尾部追加元素，i就是在列表中所加的元素
	
#由于上个循环后，elements已经增加了从0到5的元素，所以现在elements = [0,1,2,3,4,5]	
for i in elements:
	print "The element is %s" %i
	
	

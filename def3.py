#-*- coding=utf-8 -*-
#from sys import argv
#script,word = argv

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ') #把输入的多个单词用''包起来，然后以，号分开。
	return words #返回值是分开的words


def sort_words(words):
	"""sort the words. """#作为注释
	return sorted(words)#把单词的字母排序后进行返回,以‘’分开
	
def print_first_word(words):
	"""print the first word after popping it off."""
	word = words.pop(0) #取出数组内的第一个单词
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word  #取出数组内的最后一个单词
	
def sort_sentence(sentence):
	"""Take in a full sentence and return the sorted words"""
	words = break_words(sentence) #把单词用‘’分开，然后都赋值给words
	return sort_words(words)#调用方法，把这些单词重新排序，然后返回排序后的值
	
def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)#把单词用‘’分开，然后都赋值给words
	print_first_word(words)#打印首字母
	print_last_word(words)#打印尾字母
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)#把句子的单词按字母排序
	print_first_word(words)#打印首字母
	print_last_word(words)#打印尾字母
	
sentence = "I love you"
words = break_words(sentence)
print words  #['I', 'love', 'you']

word = "love"
print sort_words(word)	#['e', 'l', 'o', 'v']

#这个方法的参数是一个数组，而不是一个句子和单词.只有数字有pop的方法
words = ['I','Love','You']
print print_first_word(words) #I

print print_last_word(words) #YOU

sentence = "YOU LOVE ME"
print sort_sentence(sentence)  # ['LOVE', 'ME', 'YOU']

sentence = "ME YOU TOO"
print print_first_and_last(sentence)  #ME TOO

sentence = "ME YOU TOO"
print print_first_and_last_sorted(sentence)  # ME YOU



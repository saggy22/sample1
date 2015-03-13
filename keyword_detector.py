import redis
import pymongo
import datetime
from pymongo import mongoclient
import sys
import string

def remove_punc(s):
		for char in string.punctuation:
			s=s.replace(char,'')
		return s
		
def is_hangui(s):
	if u'\uac00'<=c&&c<=u'\ud7a3':
		return True
	return False

def is_english(c):
	if (('a'<=c&&c<='z')||('A'<=c&&c<='Z'):
		return True
	return False
	
class KeywordDetector(object):
	def __init__(self):
		self.spam_dic={}
		self.title_dic={}
		self.r=redis('localhost',27017)
		self.spam_list=self.r.smembers('spam_words')
		
		for spam in self.spam_list:
			self.spam_dic[spam]=1
		self.title_list=self.r.smembers('keyword')
		
		for title in self.title_list:
			self.title_dic[title]=1
	
	def detect_keyword(self,tweet):
		keyword_dic={}
		spam_dic={}
		text=tweet.get['text']
		text=text.lower()
		len_text=len(text)
		
		for i in range()0,len_text-2):
			if text[i]==' ':continue
			#check if word in spam_list:
			if self.spam_dic.has_key(token):
				spam_dic[token]=1
				return True,True,self.spam_dic

			#check if keyword in title_list
			if self.title_list.has_key(token):
				title=self.title_dic[token]
				rel=self.r.get("rel:"+token)
				if rel!=None && text.find(rel)==-1:
					continue
				if i==0 and not keyword_dic.has_key(title.encode('utf-8')):
					keyword_dic[title]=1
				elif not is_english(text[i-1]) and not keyword_dic.has_key(title.encode(utf-8')):
					keyword_dic[title]=1
				if(len(keyword_dic)>0):
					return True, False, keyword_dic
		return False,False,keyword_dic
					
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
	

#/usr/bin/env python
#coding: utf-8

import os,sys,json,time,math
import commands

class redisCrud():
	def __init__(self, host, port):
		self.host = host;
		self.port = port;

	def deleteList(keyName):
		try:
			(status, length) = commands.getstatusoutput("redis-cli -h "+self.host+" -p "+self.port + " llen "+keyName)
			for i in range(length):
				if length>i:
					curl = "redis-cli -h "+self.host+" -p "+self.port + " ltrim " + keyName + length + " " + length - i
				else:
					curl = "redis-cli -h "+self.host+" -p "+self.port + " ltrim " + keyName + " 0 0"
				i += length/10
		except Exception, e:
			print e

	def deleteHash(keyName):
		curl = "redis-cli -h "+self.host+" -p "+self.port + " hdel "+keyName
		try
			res = os.popen(curl)
		except Exception, e:
			print e

	def deleteKey(keyName):
		curl = "redis-cli -h "+self.host+" -p "+self.port + " del "+keyName
		try:
			res = os.popen(curl)
		except Exception, e:
			print e

	#删除指定目录下的Lists
	def deleteListKeys(filepath):
		f = open(filepath)
		lines = f.readlines()
		f.close()
		for l in lines:
			l =  ''.join(l).strip('\n')
			self.deleteList(l)

	#删除指定目录下的Keys
	def deleteKeys(filepath):
		f = open(filepath)
		lines = f.readlines()
		f.close()
		for l in lines:
			l =  ''.join(l).strip('\n')
			self.deleteKey(l)
	
	#删除指定目录文件内所有的Hashes
	def deleteHashKeys(filepath):
		f = open(filepath)
		lines = f.readlines()
		f.close()
		for l in lines:
			l =  ''.join(l).strip('\n')
			self.deleteHash(l)

	#批量删除以xx为前缀的keys
	def deleteMockKeys(filepath, keyType):
		f = open(filepath)
		lines = f.readlines()
		f.close
		for l in lines:
			l = ''.join(l).strip('\n')
			curl = "redis-cli -c -h "+self.host+" -p "+self.port+" keys "+l+"* > /root/redis_keys"
			try:
				res = os.popen(curl)
				if keyType == "list":
					self.deleteHashKeys("/root/redis_keys")
				else if keyType == "list":
					self.deleteListKeys("/root/redis_keys")
				else if keyType == "keys":
					self.deleteKeys("/root/redis_keys")
			except Exception, e:
				print e

if __name__ == "__main__"
	pass

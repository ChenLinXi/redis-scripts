import os,sys,json,time
#import redis

def getKeys():
	try:
		res = os.popen('redis-cli -h 172.16.146.152 -p 6038 scan 0 count 42420')
		return res
	except Exception, e:
		pass

def getKeyInfo(res):
	i = 0
	#r = redis.Redis(host='172.16.146.152',port=6038,db=0)
	for l in res.readlines():
		curl = 'redis-cli -h 172.16.146.152 -p 6038 debug object '+ l.strip()
		try:
			f = file("/root/status","a+")
			ret = os.popen(curl)
			res = ret.read().split(" ")
			res = res[4].split(":")[1]
			l =  ''.join(l).strip('\n')
			f.write(l+ ':' +res+'\n')
			f.close()
		except Exception, e:
			pass

	print "finished"

if __name__ == "__main__":
	res = getKeys()
	getKeyInfo(res)
	

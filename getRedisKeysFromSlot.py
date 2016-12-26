import os,sys,json,time

def getKeys():
	res = os.popen('redis-cli -h xxxx -p xxxx CLUSTER GETKEYSINSLOT slot-number slot-range')
	return res

def getSeriLen(keysline):
	i = 0
	for l in keysline.readlines():
		curl = 'redis-cli -h xxxx -p xxxx debug object '+ str(l)
		try:
			f = file("/root/status","a+")
			ret = os.popen(curl)
                        res = ret.read().split(" ")
                        res = res[4].split(":")[1]
			l =  ''.join(l).strip('\n')
			f.write(l+ ' : ' +res+'\n')
			f.close()
		except Exception, e:
			print e
	print "Finished"

if __name__ == "__main__":
	res = getKeys()
	#print res
	getSeriLen(res)

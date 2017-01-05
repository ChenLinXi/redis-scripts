import os,sys,json,time
import subprocess
import Queue
import threading

global resQueue

resQueue = Queue.Queue(0)

def getKeysInfo(scanid, cmd):
	try:
		path = cmd +"scan " + scanid + " count 100 > /root/a.log"
		res = subprocess.Popen(path, shell=True)
		log = open("/root/a.log")
		lines = log.readlines()
		log.close()
		for l in lines[1::]:	
			l = ''.join(l).strip('\n')
			f = file("/root/statusxxxx","a+")
			curl = cmd + "debug object "+l
			ret = os.popen(curl)
			res = ret.read().split(" ")
			res = res[4].split(":")[1]
			f.write(l+":"+res+'\n')
			f.close()
	except Exception,e:
		print e
	res = ''.join(lines[0]).strip('\n')
	if res == '0':
		return 
	else:
		return getKeysInfo(res, cmd)

if __name__ == "__main__":
	scanid = '0'
	cmd = "redis-cli -h xxxx -p xx "	
	res = getKeysInfo(scanid, cmd)
	print 'success'	


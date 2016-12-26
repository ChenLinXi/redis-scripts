import os,sys
import json

def getInfo():
	res = os.popen('docker ps')
	RES = []
	for l in res.readlines():
		l = l.split()
		RES.append(l[len(l)-1])
	return RES

def getPort(res):
	RES = []
	i = 0
	for i in range(len(res)):
		RES.append(res[i][len(res[i])-4:len(res[i])])
		i+=1
	return RES	

def getStatus(res):
	i = 0
	j = 0
	RES = []
	for i in range(len(res)):
		if i == 0:
			pass
		elif i == len(res) - 1:
			pass
		else:
			ret = 'redis-cli '+'-h XXX -p ' + str(res[i]) + ' info'
			#print ret
			result = os.popen(ret)
			RES.append(result)
	status = {}
	for j in range(len(RES)):
		for l in RES[j].readlines():
			if 'master_link_status' in l:
				status[res[j]] = l
	print len(status)
	status = json.dumps(status, indent=4).encode("utf-8")
	print status

	return 0	


if __name__ == "__main__":

	res = getInfo()
	res = json.dumps(res, indent=4).encode("utf-8")
	#print res
	ports = getPort(res)
	getStatus(ports)

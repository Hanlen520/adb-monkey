# encoding: utf-8

import  platform,subprocess,re,os
 
cmds=subprocess.call('adb connect 127.0.0.1:62001')
print(cmds)
# cmdss=subprocess.call('adb devices')
# '获取设备状态'
def huoqushebeizhuangtai():#获取设备状态
	cmd1='adb get-state'
	devices_status=os.popen(cmd1).read().split()[0]
	return devices_status
print(huoqushebeizhuangtai())
# print("连接成功")

#获取包名和activity
pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+") 
out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read() #window下使用findstr
list = pattern.findall(out)
component = list[0] #输出列表中的第一条字符串   #包名和activity
def name():
	ackagename=component.split("/")[0]    #获取当前应用的包名
	return ackagename
def activicy():
	packagenameactivicy=component.split("/")[1]    #获取当前设备的activity
	return packagenameactivicy
# fhandle = os.open(r"e:\aa.txt", "w")  
# os.write()
# fhandle.close()
print(component)
print(name())
print(activicy())

# -*- coding: utf-8 -*-
# @Author  : hanzilong
import  platform,subprocess,re,os
# os.popen(cmdd).read()
cmds=subprocess.call('adb connect 127.0.0.1:62001')
# print(cmds)
# cmdss=subprocess.call('adb devices')
# '获取设备状态'
def huoqushebeizhuangtai():#获取设备状态
	cmd1='adb get-state'
	devices_status=os.popen(cmd1).read().split()[0]
	return devices_status

print(huoqushebeizhuangtai())
print("连接成功")

component="com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.main.MainActivity"
packagename="com.ss.android.ugc.aweme"
# adb shell monkey -p com.jiochat.jiochatapp --throttle 100 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 1000000>d:\b.log
# '获取启动耗时'
def starttime_app(packagename,component):#启动耗时
	cmd='adb shell am start -W -n %s'%component
	me=os.popen(cmd).read().split('\n')[-7].split(':')#获取启动时间
	# cmd2='adb shell am force-stop %s'%packagename
	# os.system(cmd2)
	return me
print("应用启动时间：%s"% starttime_app(packagename,component))
#'获取cpu信息'
def caijicpu(packagename):#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
	cpu='adb shell top -n 1| findstr %s'% packagename
	re_cpu=os.popen(cpu).read().split()[2]
	return re_cpu
print("CPU占有率：%s"% caijicpu(packagename))
#'获取内存'
def getnencun(packagename):#Total 的实际使用过物理内存
	cpu = 'adb shell top -n 1| findstr %s' % packagename
	re_cpu=os.popen(cpu).read().split()[6]
	return re_cpu
print("使用内存：%s"% getnencun(packagename))

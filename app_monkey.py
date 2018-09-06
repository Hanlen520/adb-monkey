# encoding: utf-8

import os

component="com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.main.MainActivity"
packagename="com.ss.android.ugc.aweme"
# adb shell monkey -p com.jiochat.jiochatapp --throttle 100 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v 1000000>d:\b.log
s_num="1001111"   #伪随机数生成器的seed值，如果用相同的seed值再次运行monkey，将生成相同的事件序列
throttle="100"    #延时
pct_touch="10"    #调整触摸事件的百分比
pct_motion="80"    #调整motion（拖动）事件百分比
pct_trackball="10"  #调整滚动球事件百分比
pct_nav="0"        #调整基本的导航事件百分比（上下左右键）
pct_syskeys="0"      #调整系统事件百分比（系统按键）
pct_appswitch="0"    #调整Activity启动的百分比  （全部界面）
num="10000"             #测试总次数
logfilepath="F:\monkey.txt"
# '执行monkey测试'在日志中搜索“ANR ”（此处有空格）， 崩溃问题：在日志中搜索“Exception”，快速定位到关键事件信息
def adb_monkey(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath):
    cmden='adb shell monkey -p %s -s %s --throttle %s --pct-touch %s --pct-motion %s  --pct-trackball  %s  --pct-trackball %s  --pct-syskeys  %s  --pct-appswitch  %s   -v -v -v %s >%s'%(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath)
    os.popen(cmden)


#encoding:utf-8
import urllib2, sys
import json
import subprocess

try: citycode = sys.argv[1]
except: citycode = '120010' #地域120010
#resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

# 読み込んだJSONデータをディクショナリ型に変換
resp = json.loads(resp)

i  = 0
for forecast in resp['forecasts']:
   i = i + 1
   print '**************************'
   print forecast['dateLabel']+'('+forecast['date']+')'
   print forecast['telop']
   if i == 1:#今日の天気
       k = forecast['telop']
print '**************************'

cmd = "echo 0 > /dev/myled0"
subprocess.call( cmd, shell=True  )

if k.find(u'晴') != -1:#########################################################
    cmd = "echo 1 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.rfind(u'曇') != -1:
        cmd = "echo 2 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'雨') != -1:
        cmd = "echo 3 > /dev/myled0"
        subprocess.call( cmd, shell=True)
    elif k.rfind(u'雪') != -1:
        cmd = "echo 4 > /dev/myled0"
        subprocess.call( cmd, shell=True)
elif k.find(u'曇') != -1:########################################################
    cmd = "echo 2 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.rfind(u'晴') != -1:
        cmd = "echo 1 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'雨') != -1:
        cmd = "echo 3 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'雪') != -1:
        cmd = "echo 4 > /dev/myled0"
        subprocess.call(cmd,shell=True)
elif k.find(u'雨') != -1:#########################################################
    cmd = "echo 3 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.rfind(u'晴') != -1:
        cmd = "echo 1 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'曇') != -1:
        cmd = "echo 2 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'雪') != -1:
	cmd = "echo 4 > /dev/myled0"
        subprocess.call(cmd,shell=True)
elif k.find(u'雪') != -1:#########################################################
    cmd = "echo 4 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.rfind(u'晴') != -1:
        cmd = "echo 1 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'曇') != -1:
        cmd = "echo 2 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.rfind(u'雨') != -1:
        cmd = "echo 3 > /dev/myled0"
        subprocess.call(cmd,shell=True)
##################################################################################

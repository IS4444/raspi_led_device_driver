#encoding:utf-8
import urllib2, sys
import json
import subprocess

try: citycode = sys.argv[1]
except: citycode = '120010' #デフォルト地域120010
resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

# 読み込んだJSONデータをディクショナリ型に変換
resp = json.loads(resp)

i  = 0
for forecast in resp['forecasts']:
   i = i + 1
   if i == 1:
       k = forecast['telop']

cmd = "echo 0 > /dev/myled0"
subprocess.call( cmd, shell=True  )
cmd = "echo 2 > /dev/myled0"
subprocess.call( cmd, shell=True  )
cmd = "echo 4 > /dev/myled0"
subprocess.call( cmd, shell=True  )

#if k == '晴れのち曇り'.decode('utf-8'):
#    cmd = "echo 5 > /dev/myled0"
#elif k == '曇り'.decode('utf-8'):
#    cmd = "echo 3 > /dev/myled0"
#elif k == '雨'.decode('utf-8'):
#    cmd = "echo 1 > /dev/myled0"

if k.find(u'晴') != -1 or k.rfind(u'晴') != -1:
    cmd = "echo 5 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.find(u'雨') != -1 or k.rfind(u'雨') != -1:
        cmd = "echo 1 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.find(u'曇') != -1 or k.rfind(u'曇') != -1:
        cmd = "echo 3 > /dev/myled0"
        subprocess.call( cmd, shell=True)
elif k.find(u'雨') != -1 or k.rfind(u'雨') != -1:
    cmd = "echo 1 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.find(u'晴') != -1 or k.rfind(u'晴') != -1:
        cmd = "echo 5 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.find(u'曇') != -1 or k.rfind(u'曇') != -1:
        cmd = "echo 3 > /dev/myled0"
        subprocess.call(cmd,shell=True)
elif k.find(u'曇') != -1 or k.rfind(u'曇') != -1:
    cmd = "echo 3 > /dev/myled0"
    subprocess.call(cmd,shell=True)
    if k.find(u'雨') != -1:
        cmd = "echo 1 > /dev/myled0"
        subprocess.call(cmd,shell=True)
    elif k.find(u'晴') != -1:
        cmd = "echo 5 > /dev/myled0"
        subprocess.call(cmd,shell=True)

subprocess.call( cmd, shell=True)

#s = '晴れのち雪'
#index = s.find('晴れ')
#print index

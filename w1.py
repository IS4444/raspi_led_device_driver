#encoding:utf-8
import urllib2, sys
import json
import subprocess

try: citycode = sys.argv[1]
except: citycode = '020010' #デフォルト地域120010
resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

# 読み込んだJSONデータをディクショナリ型に変換
resp = json.loads(resp)
#print '**************************'
#print resp['title']
#print '**************************'
#print resp['description']['text']
i  = 0
for forecast in resp['forecasts']:
   i = i + 1
   print '**************************'
   print forecast['dateLabel']#+'('+forecast['date']+')'
   print forecast['telop'] 
   if i == 1:
       k = forecast['telop']
#print '**************************'
j = 0
while j<3:
    if j == 0:
        cmd = "echo 0 > /dev/myled0"
        subprocess.call( cmd, shell=True  )
    elif j == 1:
        cmd = "echo 2 > /dev/myled0"
        subprocess.call( cmd, shell=True  )
    elif j == 2:
        cmd = "echo 4 > /dev/myled0"
        subprocess.call( cmd, shell=True  )
    j = j +1

if k == '晴れ'.decode('utf-8'):
    cmd = "echo 5 > /dev/myled0"
elif k == '曇り'.decode('utf-8'):
    cmd = "echo 3 > /dev/myled0"
elif k == '雨'.decode('utf-8'):
    cmd = "echo 1 > /dev/myled0"

subprocess.call( cmd, shell=True)

# 天気情報取得用デバイスドライバ
・myled.cは講義内で使用したプログラムを改良し、LEDを4つ点灯させるものとなっている。w2.pyを利用することでその日の天気情報を取得することが出来る。
GPIO22 = 晴れ
GPIO23 = 曇り
GPIO24 = 雨
GPIO25 = 雪
(例)その日の天気が「晴れのち曇」の場合はGPIO22とGPIO23が点灯する。

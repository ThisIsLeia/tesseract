from re import L
import pytesseract
import time
from PIL import Image

cardict = {}
mypath = 'D:\\Course\\python\\'
while True:
    carplate = input('請輸入或掃描車牌(欲退出請輸入Q或q)')
    if carplate == 'Q' or carplate == 'q':
        print('Bye')
        break
    carplate = mypath + carplate
    keytext = pytesseract.image_to_string(Image.open(carplate))
    if keytext in cardict:
        excitTime = time.asctime()
        excitsecond = time.time()
        timecost = excitsecond - entrysecond
        hour = timecost // 3600
        min = timecost % 3600 // 60
        sec = timecost % 60
        if min != 0 or sec != 0:
            cul = hour + 1
        print('車牌:', keytext, '出場時間:', excitTime)
        print('花費時間 %d小時 %d分鐘 %d秒, 停車費: %d 元' % (hour, min, sec, cul*60))
        del cardict[keytext]
    else:
        entryTime = time.asctime()
        entrysecond = time.time()
        print('車牌:', keytext, '進場時間:', entryTime)
        cardict[keytext] = entrysecond


# 辨識繁體文字圖片

with Image.open('D:\\Course\\python\\chinese_traditional.jpeg') as obj:
    text = pytesseract.image_to_string(obj, lang='chi_tra')
    print(text)

with open('D:\\Course\\python\\chinese_traditional.txt', 'w') as fn:
    fn.write(text)

# 辨識簡體文字圖片
# 注意！簡體字的encoding要記得加, encoding='utf-8'

with Image.open('D:\\Course\\python\\chinese_simple.jpg') as obj:
    text = pytesseract.image_to_string(obj, lang='chi_sim')
    print(text)

with open('D:\\Course\\python\\chinese_simple.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)

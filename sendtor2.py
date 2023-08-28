#!/usr/bin/env python
# coding: utf-8
#zezo2023@zezo.com
import requests
import time
import random
itemid = 0
#logging.basicConfig(filename='/home/xman/Desktop/logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.info('Started program execution')

#   SOCKS proxy  Tor

def sendMsg(id,msg):

    sticker_urls = [
	'https://bit.ly/45t6soH',
	'https://bit.ly/3EgyTKI',
	'https://bit.ly/45t6soH',
	'https://bit.ly/3EgyTKI',
	'https://bit.ly/45t6soH'
    ]
	                    
          
    random_sticker_url = random.choice(sticker_urls)
    
    payload = {
        'profileId': id,
        'chatId': '',
        'messageText': msg,
        'messageImg': '',
        'listId': '20',
        'chatFromUserId': '',
        'chatToUserId': '',
        'stickerImgUrl': random_sticker_url,
        'stickerId': '0',
        'basedOnMessages': '',
        'lang': '',
        'accessToken': '55b390321f6996e1f1521d0fc6aa2aad',
        'accountId': '4751947'
    }

    files=[

    ]
    
    # رابط الطلب الPOST
    urlMsg = 'https://alarabspace.com/api/android/v1/method/msg.new.inc.php'

    # Header:
    headers = {
        'Cookie': 'PHPSESSID=2035a4511dfdb5d7819af894849b45fe; lang=en',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; SM-A226B Build/TP1A.220624.014)'
    }

    # إرسال الطلب POST مع البيانات
    response = requests.request("POST", urlMsg, headers=headers, data=payload, files=files)
    #print(response.text)

    if response.status_code == 200:
        response_data = response.json()  # تحويل النص إلى تنسيق JSON
        error = response_data.get('error')
        if(error != True):
            print('Send Succed.!')
        

def users(itemid):
    
    # متغيرات سحب المستخدمين
    data = {
        'accessToken': '55b390321f6996e1f1521d0fc6aa2aad',
        'accountId': '4751947',
        'gender' : '1',
        'query' : '',
        'online' : '0',
        'pro_mode' : '0',
        'itemId' : itemid,
        'loadingMore' : True,
        'viewMore' : True,
        'sex_orientation' : '0',
        'age_from' : '18',
        'age_to' : '105'
        
    }
    # رابط الطلب الPOST
    url = 'https://alarabspace.com/api/android/v1/method/app.search.inc.php'
         
    # إرسال الطلب POST مع البيانات
    response = requests.post(url, data=data)
    # الحصول على الاستجابة من الخادم
    if response.status_code == 200:
        response_data = response.json()  # تحويل النص إلى تنسيق JSON
        
        itemid = response_data.get('itemId', 'itemId Not Found')
        print("itemid:" ,itemid)
        #Get itemId ???? itemCount

        items = response_data.get('items', [])  # الحصول على قائمة العناصر
        items_count = len(items)  # الحصول على عدد العناصر داخل القائمة
        print("CountPeople:", items_count)
        
        #if items_count == 0:
               #exit(0)
		
        for item in items:
            Id = item.get('id' , 'ID Not Found.!')
            print("ID:" , Id)
            fullname = item.get('fullname', 'قيمة افتراضية إذا لم تكن موجودة')
            print("Fullname:", fullname)
            gender = item.get('sex', 'Gender Not Found.!')
            print("Gender: " , gender)
            sex_orientation = item.get('sex_orientation' , 'sex_orientation Not Found')
            print("Sex_Orientation" , sex_orientation)

            message = f"""
                   {fullname} مرحبًا،

اى بنت ترغب في مشاهدة افلام عربي جنسSيــة ومقاطع أجنبية مترجمة للعربي مدبلجة تنضم لمجموعة التليجرام السرية الموجودة في البايو او حساب انستغرام aflame666 ارسل لي نقطة فى انستغرام وارسلك كل المقاطع 
رومانسية وغيرها ومقاطع زنجي بدون شروط
https://t.me/+h1n4TMLxYOBjYWNk

                    """


            sendMsg(Id,message)

            time.sleep(5)

    else:
        print("حدث خطأ في الرد، الكود:", response.status_code)
        #logging.info('Finished program execution')
        exit(0)

# دالة للتحقق من الضغط على مفتاح خروج
while True:
    users(itemid)
   


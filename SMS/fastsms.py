import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=YOUR_QT_SMS_ID&language=english&route=qt&numbers=".urlencode('9845112790,9972885998')."&flash=1&variables=".urlencode('{#AA#}|{#CC#}')."&variables_values=".urlencode('123456787|asdaswdx').""
headers = {
    'authorization': "sfKE8k7cOjJegxUaF3tTq9RPDvQL50BZnY4mIXwziSrh6bduCWr1kKo5Nw6Lvz2Wh4isXaDyVxQOUuJ0",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
   # 'authorization': "sfKE8k7cOjJegxUaF3tTq9RPDvQL50BZnY4mIXwziSrh6bduCWr1kKo5Nw6Lvz2Wh4isXaDyVxQOUuJ0",
    

import requests

url =  "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=This is a test message&language=english&route=p&numbers=8520801066,8520801066&Oflash=1"
headers = {
    'authorization': "sfKE8k7cOjJegxUaF3tTq9RPDvQL50BZnY4mIXwziSrh6bduCWr1kKo5Nw6Lvz2Wh4isXaDyVxQOUuJ0"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
print(respone.status_code)
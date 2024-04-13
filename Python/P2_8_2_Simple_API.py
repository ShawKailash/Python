import requests
import time
while True:
    req = requests.get("https://courses.codingforeverybody.com")
    print(req.status_code)
    if req.status_code !=200:
        pass
    time.sleep(1)
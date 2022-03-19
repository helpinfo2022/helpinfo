import time
from datetime import datetime

from playsound import playsound
import requests





response = requests.get('https://www.newsru.co.il/')
first=response.text

while first:
    current_datetime = datetime.now()
    print("проверка", current_datetime)
    response2 = requests.get('https://www.newsru.co.il/')
    seecond=response2.text

    if first!=seecond :
        current_datetime2 = datetime.now()
        print("есть изменения", current_datetime2)
        playsound('1.mp3')
        first=seecond
    time.sleep(600)


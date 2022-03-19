

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.calcalistech.com/ctech/articles/0,7340,L-3929918,00.html')
# response = requests.post('https://api-server-name.com/methodname_post', data = {'key':'value'})

soup = BeautifulSoup(response.text, 'lxml')

list_urls = []
num=0
text=''
for i in soup.findAll('p'):
    # link = str(i.get('text'))
    list_urls.append(i)

    text=text+str(i)
    num+=1
    # if len(i)>5 :
    #     print(i)

# print(list_urls)
print(num)
print(len(text.split(" ")))
print(text)


poisk = ["investments", "want", "vasya"]
nashel = []
nenashel = []
for m in poisk:
    if m in text:
        nashel.append(m)
    else:
        nenashel.append(m)

print(nashel)
if nashel==poisk:
    print("100% nashel",nashel)
else:
    print("Ne nashel",nenashel)





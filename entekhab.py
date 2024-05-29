import requests
from bs4 import BeautifulSoup


req = requests.get(url=r'https://www.entekhab.ir/')
response = BeautifulSoup(req.text, 'html.parser')

news = dict()

for div1 in response.select('div.im-news-content.col-xs-36'):
    for div2 in div1.find('div').select('div h2.Htags a'):
        news[div2.text.strip().encode('utf-8').decode()] = div1.find('div', class_='im-news-sub').text
else:
    print(news)        

    

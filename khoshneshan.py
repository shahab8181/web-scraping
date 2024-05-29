from requests import api
from json import dumps
from fake_useragent import FakeUserAgent


user_agent = FakeUserAgent()
response = api.get(
    url=r'https://api.khoshneshan.com/api/loads',
    headers={'User-Agent': user_agent.random}
)

with open('khoshneshan-loads.json', 'wt', encoding='utf-8') as file:
    file.write(dumps(response.json(), indent=4))
    file.close()
    
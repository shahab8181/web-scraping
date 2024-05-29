import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent


url = r'https://www.mongard.ir/{}'
user_agent = FakeUserAgent()
email = ... # NOTE: your email address
password = ... #NOTE: your password

session = requests.Session()
request_1 = session.get(
    url=url.format('accounts/login/'), 
    headers={'User-Agent': user_agent.random},
)
login = BeautifulSoup(request_1.text, 'html.parser')

login_data = dict()

for inp in login.find('form', class_='sign_in_form').find_all('input', attrs={'type': 'hidden'}):
    login_data[inp.get('name')] = inp.get('value')
    
login_data.update({
    'email': email,
    'password': password
})

request_2 = session.post(
    url=url,
    data=login_data,
    headers={'User-Agent': user_agent.random}
)
request_3 = session.get(
    url=url.format('courses/'),
    headers={'User-Agent': user_agent.random}
)
courses = BeautifulSoup(request_3.text, 'html.parser')
pages = courses.find('div', class_='courses').find('div', class_='container').find('div', class_='row').find('div', class_='col-sm-12 col-md-12 col-lg-12 col-xl-12').find('nav', class_='custom-pagination mt-4 d-flex justify-content-center align-items-center').find('ul').find_all('li')


def get_digitis(string: str) -> str:
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
    else:
        if len(digits) == 0:
            return 'Free'
        return ''.join(digits)+'000'

data = []

for index, page in enumerate(pages):
    request_4 = session.get(
        url=url.format(f'courses/?page={index+1}'),
        headers={'User-Agent': user_agent.random}
    )
    content = BeautifulSoup(request_4.text, 'html.parser')
    courses = content.find('div', class_='courses').find('div', class_='container').find('div', class_='row').find('div', class_='col-sm-12 col-md-12 col-lg-12 col-xl-12').find('div', class_='row').select('div.col-sm-12.col-md-12.col-lg-6.col-xl-4.mb-4')
    for course in courses: 
        data.append(dict(
            title=course.find('div', class_='card').find('img').get('alt'),
            price=get_digitis(course.find('div', class_='card').find('div', class_='card-footer d-flex justify-content-between align-items-center').find_all('span')[-1].get_text(strip=True)),
            finish_recording_the_course=True if course.find('div', class_='card').find('div', class_='card-body').find('div', class_='card-details d-flex justify-content-between align-items-center').find('div', class_='custom-btn-course-status').find('i').get('class') == 'fa fa-check' else False,
            time=course.find('div', class_='card').find('div', class_='card-footer d-flex justify-content-between align-items-center').find('span').text.strip()
        ))
else:
        print(data)
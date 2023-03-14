from requests import Session
from bs4 import BeautifulSoup
# from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36'
}

work = Session()
work.get('https://quotes.toscrape.com/', headers=headers)  # cookie 0
response = work.get('https://quotes.toscrape.com/login', headers=headers)  # cookie 1

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')
"""
<input type="hidden" name="csrf_token" value="JVHTpesSD*">
"""

data = {'csrf_token': token, 'username': 'noname', 'password': 'password'}

result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)

# work get page/1
# circle to new page: page/2 page/3 etc

"""
count = 1
r = work.get(f'https://quotes.toscrape.com/page/{count}/', headers=headers, data=data)
s = BeautifulSoup(r.text, 'lxml')
result = s.find_all('span', class_='text')
authors = s.find_all('small', class_='author')
print(f'{result}, {authors}')

if len(result) != 0:
    count += 1
else:
    pass
"""

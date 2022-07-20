import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

# Convert to object
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('.score'))

# file = open('./sample.html', 'w')
# file.write(str(soup))
# file.close()
# # print(soup.body.contents)
# # print(soup.find_all('div'))
# # print(soup.title)
# # print('\n')
# # print(soup.find(id = '32126637'))
# # print(soup.select('.score'))

print(soup.select('.storylink'))
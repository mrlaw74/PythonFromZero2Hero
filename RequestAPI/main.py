import requests
url = 'https://api.pwnedpasswords.com/range/' + 'CBFD2'
res = requests.get(url)
print(res)
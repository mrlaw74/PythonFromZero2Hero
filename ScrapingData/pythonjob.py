import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

results = soup.find("section", class_ = "job_list")
# print(result)

job_elements = results.find_all("div", class_ = "job")
print(job_elements)
# print(len(job_elements))
for job_element in job_elements:
    python_jobs = results.find_all("h1", string=lambda text: "href" in text.lower())
    # title = job_element.find("i ", class_ = "i-globe")
    print(python_jobs)
    print()
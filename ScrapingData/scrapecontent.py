import requests
from bs4 import  BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# Find elements by ID
result = soup.find(id="ResultsContainer")
# print(result.prettify)

# Find elements by HTML Class Name
job_elements = result.find_all("div", class_ = "card-content")
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element)
#     print(company_element)
#     print(location_element)
#     print()

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
# print(job_elements)

# Find Elements by Class Name and Text Content

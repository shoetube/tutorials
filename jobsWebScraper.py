import requests
from bs4 import BeautifulSoup as bs

''' Web scraping tutorial from realpython.com'''
def tryIt(arg):
    try:
        exec(arg)
    except:
        pass

jobTitle = input("Enter job title: ")
jobTitle = jobTitle.strip()
list = jobTitle.split(' ')
jobTitle = '-'.join(list)

location = input("Enter location: ")
location = location.strip()
list = location.split(' ')
location = '-'.join(list)

url = f'https://www.monster.com/jobs/search/?q={jobTitle}&where={location}'
page = requests.get(url)
soup = bs(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:

    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')

    tryIt('print(title_elem.text.strip())')

    try:
        print(company_elem.text.strip())
    except:
        pass

    try:
        print(location_elem.text.strip())
    except:
        pass

    print()

print(url)
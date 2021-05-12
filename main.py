from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import lxml

# Instantiate an Options object
# and add the “ — headless” argument

opts = Options()
opts.add_argument(' — headless')
url= f'https://www.indeed.com/m/jobs?q=data+analyst&start=0'
PATH="/Applications/chromedriver"
driver=webdriver.Chrome(PATH)
driver.get(url)
# Put the page source into a variable and create a BS object from it
soup_file=driver.page_source
soup = BeautifulSoup(soup_file, 'lxml')


    # This will get the jobcards
jobcards= soup.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
for jobs in jobcards:
    title=jobs.find('a').text.strip( )
    company=jobs.find('span', class_='company').text.strip( )
    summary=jobs.find('div',class_='summary').text.strip( )
    print(title,company,summary)

#integrate into functions and download 



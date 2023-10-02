import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
from fake_headers import Headers

headers = Headers(browser="chrome", os='win', headers=True)

telephone, email, job_title, prefix, last_name, first_name, research_topics = [], [], [], [], [], [], []

url_base = 'https://www.dal.ca/faculty/computerscience/faculty-staff.html'
response_base = requests.get(url_base, headers=headers.generate())
soup_base = BeautifulSoup(response_base.text, 'html.parser')
hrefs = soup_base.find_all('a')

# For all the links related to the professors
links = []
for a in hrefs: 
    href = a.get('href')
    if type(href) == str: 
        if 'faculty-staff' in href:
            href = "https://www.dal.ca" + href 
            links.append(href)


# Pop the first two faculty pages on the header, it should be on 3
del links[:3]

for link in tqdm(links):
 
    response = requests.get(link, headers=headers.generate())
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        first_name.append(soup.find('span', itemprop='familyName').text)
    except:
        first_name.append('')
    try:
        last_name.append(soup.find('span', itemprop='givenName').text) 
    except:
        last_name.append('')
    try:
        prefix.append(soup.find('span', itemprop='honorificPrefix').text)
    except:
        prefix.append('')
    try:
        job_title.append(soup.find('h2', itemprop='jobTitle').text)
    except:
        job_title.append('')
    try:
        email.append(soup.find('span', itemprop='email').text)
    except:
        email.append('')
    try:
        telephone.append(soup.find('span', itemprop='telephone').text)
    except:
        telephone.append('')

    # Find research areas if exist.
    try:
        research_topics_heading = soup.find("b", string="Research Topics:")
        ul_element = research_topics_heading.next_sibling

        # Find the next UL after research  area heading
        if research_topics_heading:
            for ul_element in research_topics_heading.next_siblings:
                if ul_element.name == "ul":
                    break

        # If the UL tag is found, get all of the li tags
        if ul_element:
            li_elements = ul_element.find_all("li")

        # Create a list of the li text
        li_text = []
        for li_element in li_elements:
            li_text.append(li_element.text)
        research_topics.append(li_text)
    except:
        research_topics.append('')




chart = pd.DataFrame({
    'Title': job_title,
    'Name': first_name,
    'Last Name': last_name,
    'Email': email,
    'Prefix': prefix,
    'Research Topics': research_topics,
})

name = '{}.csv'.format(time.time())
chart.to_csv(name, index=False)
print("File Created: {}".format(name))
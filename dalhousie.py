import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
from fake_headers import Headers

class DalFacultyScraper:
    def __init__(self):
        self.headers = Headers(browser="chrome", os='win', headers=True)
        self.telephone, self.email, self.job_title, self.prefix, self.last_name, self.first_name, self.research_topics = [], [], [], [], [], [], []

    def scrape_faculty_data(self):
        url_base = 'https://www.dal.ca/faculty/computerscience/faculty-staff.html'
        response_base = requests.get(url_base, headers=self.headers.generate())
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
            response = requests.get(link, headers=self.headers.generate())
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                self.first_name.append(soup.find('span', itemprop='familyName').text)
            except:
                self.first_name.append('')
            try:
                self.last_name.append(soup.find('span', itemprop='givenName').text)
            except:
                self.last_name.append('')
            try:
                self.prefix.append(soup.find('span', itemprop='honorificPrefix').text)
            except:
                self.prefix.append('')
            try:
                self.job_title.append(soup.find('h2', itemprop='jobTitle').text)
            except:
                self.job_title.append('')
            try:
                self.email.append(soup.find('span', itemprop='email').text)
            except:
                self.email.append('')
            try:
                self.telephone.append(soup.find('span', itemprop='telephone').text)
            except:
                self.telephone.append('')

            # Find research areas if exist.
            try:
                research_topics_heading = soup.find("b", string="Research Topics:")
                ul_element = research_topics_heading.next_sibling

                # Find the next UL after the research area heading
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
                self.research_topics.append(li_text)
            except:
                self.research_topics.append('')

    def create_csv(self, file_name = time.time()):
        chart = pd.DataFrame({
            'Title': self.job_title,
            'Name': self.first_name,
            'Last Name': self.last_name,
            'Email': self.email,
            'Prefix': self.prefix,
            'Research Topics': self.research_topics,
        })

        name = '{}.csv'.format(file_name)
        chart.to_csv(name, index=False)
        print("File Created: {}".format(name))




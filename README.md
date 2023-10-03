# Dalhousie University Faculty Web Scraper

## Overview

This Python project is a web scraper designed to collect information about professors from Dalhousie University's Faculty of Computer Science. It extracts data such as email addresses, names, last names, prefixes, and research areas from the [Dalhousie University Faculty and Staff Page](https://www.dal.ca/faculty/computerscience/faculty-staff.html) and stores it in a structured format using the Pandas library.

## Features

- Scrapes professor data from the Dalhousie University Faculty and Staff Page.
- Extracts information including email addresses, names, last names, prefixes, and research areas.
- Stores the collected data in a structured format, making it easy to analyze.

## Prerequisites

Before running this scraper, ensure you have the following Python packages installed:

- Pandas
- Requests
- BeautifulSoup
- tqdm
- Fake-Headers

## Version 1 (Original):

- The original code is a script without a specific structure.
- It consists of a series of statements executed sequentially.
- It scrapes faculty data from Dalhousie University's Computer Science department website.
- Data extraction and saving are done without using classes or methods.


## Version 2 (Updated):
- The updated version introduces a class-based structure.
- It encapsulates related functionality into methods within a class called DalFacultyScraper.
- Data scraping and saving are organized within this class.
- The code is more modular, making it easier to understand and maintain.


You can install these packages using pip:

```bash
pip install pandas
```
```bash
pip install requests

```
```bash
pip install tqdm

```
```bash
pip install beautifulsoup4

```
```bash
pip install fake-headers

```

## Usage

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/dalhousie.git
```

Navigate to the project directory:
```bash
cd dalhousie
```

Run the scraper script:
```bash
python dalhousie.py
```

## Future Enhancements

In the future, I plan to extend the capabilities of this web scraper by integrating machine learning techniques to provide more advanced analysis and insights. Some of the planned enhancements include:

- **Professor Ranking**: Utilizing machine learning algorithms, I plan to implement a ranking system that will help identify and recognize the best professors based on specific criteria or skills. This can assist students and researchers in making informed choices when seeking academic guidance or collaboration.

- **Recommendation System**: By employing recommendation algorithms, I aspire to build a system that suggests professors to students or researchers based on their interests, skills, and academic goals.

These future enhancements will transform this web scraper into a powerful tool for both students and researchers, facilitating better engagement and collaboration within the academic community.


The scraped data will be saved in a CSV file.

## Legal Notice
Please note that web scraping should be performed responsibly and ethically. Before using this scraper, ensure that you are complying with the website's terms of service and legal regulations regarding web scraping. Do not send mass requests to servers or engage in any activity that may disrupt the normal operation of the website.

## Disclaimer
This project is for educational and research purposes only. The creators and contributors of this project are not responsible for any misuse or unlawful activities performed with this web scraper. Use it responsibly and respect the website's terms of use.


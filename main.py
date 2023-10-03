from dalhousie import DalFacultyScraper


if __name__ == "__main__":
    scraper = DalFacultyScraper()
    scraper.scrape_faculty_data()
    scraper.create_csv()
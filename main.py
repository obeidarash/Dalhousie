from dalhousie import DalFacultyScraper
import pandas as pd

if __name__ == "__main__":
    scraper = DalFacultyScraper()
    scraper.scrape_faculty_data()
    scraper.create_csv()
    # print(pd.read_csv(scraper.file_name))
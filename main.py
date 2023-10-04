from dalhousie import DalFacultyScraper
import pandas as pd
import os
import subprocess

if __name__ == "__main__":
    scraper = DalFacultyScraper()
    scraper.scrape_faculty_data()
    scraper.create_csv()

    file = scraper.file_name

    if os.path.exists(file):
        # subprocess.Popen(['start', file], shell=True)
        print(pd.read_csv(file).head())
    else:
        print(f"The file '{file}' does not exist.")

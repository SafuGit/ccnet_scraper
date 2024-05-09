# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from hider import Hider
import pandas as pd

# Class
class TownScraper:
    def __init__(self, towns, world):
        self.towns = towns
        self.world = world
        self.data = pd.DataFrame()

        self.options = Options()
        self.options.page_load_strategy = 'none'
        self.driver = webdriver.Edge(options=self.options)

        self.wait = WebDriverWait(driver=self.driver, timeout=20)
        self.hider = Hider()

    def scrape_towns(self):
        url = self.world
        print(f'Getting url... {url}')
        self.driver.get(url)
        self.start = str(input("start scraping? (Y/N): ")).lower()

        time.sleep(1)
        if self.start == 'y':
            for town_name, town_coords in self.towns.items():
                print(f'Scraping {town_name}...')
                print(town_coords)
                print(f'Hiding elements...')
                self.hider.hide(driver=self.driver)
                print(f'Finding element with coords... {town_coords}')
                print(f'Clicking element with coords... {town_coords}')
                self.driver.execute_script(f'''var element = document.querySelector('[{town_coords}]');
                                        if (element) {{
                                                element.click();
                                            }} else {{
                                                console.log('Element not found');
                                                print('Element not found');
                                            }}''')
                
                print(f'Getting page source')
                html = self.driver.page_source
                print(f'Parsing HTML')
                soup = BeautifulSoup(html, 'html.parser')
                
                print(f'Finding bank and upkeep amounts')
                bank_span = soup.find('span', string='💰 Bank')
                upkeep_span = soup.find('span', string='💸 Upkeep')
                
                if bank_span is not None:
                    bank_amount = bank_span.next_sibling.strip()
                    upkeep_amount = upkeep_span.next_sibling.strip()
                    print(f'Found bank amount: {bank_amount}')
                    print(f'Found upkeep amount: {upkeep_amount}')
                    
                    # Create a DataFrame and print it
                    new_row = pd.DataFrame({'Town Name': [town_name], 'Bank Amount': [bank_amount], 'Upkeep': [upkeep_amount]})
                    self.data = pd.concat([self.data, new_row], ignore_index=True)
                    print(self.data)
                    print(f'Clicking back button')
                    self.driver.execute_script(f'''var xpath = '//*[@id="app"]/div[1]/div[1]/div[5]/div/a';
                                    var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                                    element.click();''')
                else:
                    print(f"Bank amount not found for {town_name}")

    def quit(self):
        self.driver.quit()

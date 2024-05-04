# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from hider import Hider
import pandas as pd

# Class
class TownScraper:
    def __init__(self, towns, world):
        self.towns = towns
        self.world = world
        
        self.driver = webdriver.Edge()
        self.wait = WebDriverWait(driver=self.driver, timeout=20)
        self.hider = Hider()

    def scrape_towns(self):
        url = self.world
        self.driver.get(url)
        
        time.sleep(2)
        self.hider.hide(driver=self.driver)
        for town_name, town_xpath in self.towns.items():
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"{town_xpath}")))
            self.driver.execute_script(f'''var xpath = '{town_xpath}';
                            var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                            element.click();''')
            
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            bank_span = soup.find('span', string='💰 Bank')
            upkeep_span = soup.find('span', string='💸 Upkeep')
            
            if bank_span is not None:
                bank_amount = bank_span.next_sibling.strip()
                upkeep_amount = upkeep_span.next_sibling.strip()
                
                # Create a DataFrame and print it
                data = pd.DataFrame({'Town Name': [town_name], 'Bank Amount': [bank_amount], 'Upkeep': [upkeep_amount]})
                print(data)
                
                self.driver.execute_script(f'''var xpath = '//*[@id="app"]/div[1]/div[1]/div[5]/div/a';
                                var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                                element.click();''')
            else:
                print(f"Bank amount not found for {town_name}")

    def quit(self):
        self.driver.quit()

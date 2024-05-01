from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variables
kievan_url = 'https://map.ccnetmc.com/nationsmap/#world;flat;7992,64,-6392;1'
american_url = 'https://map.ccnetmc.com/nationsmap/#world;flat;-12240,64,-5136;0'
towns = ['//*[@id="app"]/div[1]/div[1]/div[10]/div[87]', '//*[@id="app"]/div[1]/div[1]/div[10]/div[462]', '//*[@id="app"]/div[1]/div[1]/div[10]/div[567]', '//*[@id="app"]/div[1]/div[1]/div[10]/div[690]']
js_script = '''element = document.getElementsByClassName('clock leaflet-control');
element[0].style.display = 'none';'''

driver = webdriver.Edge()  # launch chrome

url = kievan_url
driver.get(url)
# wait for element
wait = WebDriverWait(driver=driver, timeout=20)
time.sleep(2)  # wait for the page to load
start = str(input('Would you like to start (Y/N)')).lower()
if start == 'y':
    driver.execute_script(js_script)
    for town in towns:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, town)))
        # click element
        element.click()
        
        # get updated page
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        closing_button = element.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[5]/div/a')
        closing_button.click()
        
        # find bank amount
        bank_span = soup.find('span', string='💰 Bank')
        name_span = soup.find('span')
        if bank_span is not None:
            bank_amount = bank_span.next_sibling.strip()
            print(bank_amount, name_span)
        else:
            print("Bank amount not found")
    quit_choice = str(input('Would you like to quit? (Y/N): ')).lower()

if quit_choice == "y":
    driver.quit()

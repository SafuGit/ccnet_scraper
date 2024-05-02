"""  ______   ______ .__   __.  _______ .___________.                              
 /      | /      ||  \ |  | |   ____||           |                              
|  ,----'|  ,----'|   \|  | |  |__   `---|  |----`                              
|  |     |  |     |  . `  | |   __|      |  |                                   
|  `----.|  `----.|  |\   | |  |____     |  |                                   
 \______| \______||__| \__| |_______|    |__|                                   
                                                                                
     _______.  ______ .______          ___      .______    _______ .______      
    /       | /      ||   _  \        /   \     |   _  \  |   ____||   _  \     
   |   (----`|  ,----'|  |_)  |      /  ^  \    |  |_)  | |  |__   |  |_)  |    
    \   \    |  |     |      /      /  /_\  \   |   ___/  |   __|  |      /     
.----)   |   |  `----.|  |\  \----./  _____  \  |  |      |  |____ |  |\  \----.
|_______/     \______|| _| `._____/__/     \__\ | _|      |_______|| _| `._____|"""


# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hider import Hider

# Variables
right_world = 'https://map.ccnetmc.com/nationsmap/#world;flat;7184,64,-5152;0'
left_world = 'https://map.ccnetmc.com/nationsmap/#world;flat;-8176,64,-1168;0'
towns = {
    'Envy': '//*[@id="app"]/div[1]/div[1]/div[10]/div[697]',
    'Greed': '//*[@id="app"]/div[1]/div[1]/div[10]/div[85]',
    'Camelot': '//*[@id="app"]/div[1]/div[1]/div[10]/div[135]',
    'Arizona': '//*[@id="app"]/div[1]/div[1]/div[10]/div[309]'
}
hider = Hider()

driver = webdriver.Edge()  

url = right_world
driver.get(url)

# wait for element
wait = WebDriverWait(driver=driver, timeout=20)
time.sleep(2)  

# Main Loop
start = str(input('Would you like to start (Y/N)')).lower()
while start == 'y':
    hider.hide(driver=driver)
    for town_name, town_xpath in towns.items():
        driver.execute_script(f'''var xpath = '{town_xpath}';
                        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                        element.click();''')
        
        # get updated page
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # find bank amount
        bank_span = soup.find('span', string='💰 Bank')
        upkeep_span = soup.find('span', string='💸 Upkeep')
        if bank_span is not None:
            bank_amount = bank_span.next_sibling.strip()
            upkeep_amount = upkeep_span.next_sibling.strip()
            print(f"{town_name} Balance: {bank_amount} Upkeep: {upkeep_amount}")
            driver.execute_script(f'''var xpath = '//*[@id="app"]/div[1]/div[1]/div[5]/div/a';
                            var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                            element.click();''')
        else:
            print(f"Bank amount not found for {town_name}")
            
    # Ask the user if they want to change the URL
    change_url = str(input('would you like to scan the left side? (Y/N): ')).lower()
    if change_url == "y":
        url = left_world if url == right_world else right_world
        driver.get(url)
        time.sleep(2)
        
    # Ask the user if they want to continue
    start = str(input('are you sure? (Y/N): ')).lower()

if start != "y":
    driver.quit()

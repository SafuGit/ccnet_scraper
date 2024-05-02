# Imports
from townscraper import TownScraper

print("""  ______   ______ .__   __.  _______ .___________.                              
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
|_______/     \______|| _| `._____/__/     \__\ | _|      |_______|| _| `._____|""")

########################################################################################################

# Variables
world = 'https://map.ccnetmc.com/nationsmap/#world;flat;7184,64,-5152;0'

towns = {
    'Envy': '//*[@id="app"]/div[1]/div[1]/div[10]/div[697]',
    'Greed': '//*[@id="app"]/div[1]/div[1]/div[10]/div[85]',
    'Camelot': '//*[@id="app"]/div[1]/div[1]/div[10]/div[135]',
    'Arizona': '//*[@id="app"]/div[1]/div[1]/div[10]/div[309]'
}

# Main Loop
filepath = str(input('Where would you like to save your csv file? (Copy-Paste the directory) '))
start = str(input('\nWould you like to start (Y/N)')).lower()
scraper = TownScraper(towns, world)
while start == 'y':
    scraper.scrape_towns()
    start = str(input('do you want to quit or re-scan? (Y/N): ')).lower()
if start != "y":
    scraper.quit()
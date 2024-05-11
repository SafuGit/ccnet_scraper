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
    'Envy': 'style="margin-left: -8px; margin-top: -8px; height: 16px; transform: translate3d(847px, -133px, 0px);"',
    'Greed': 'style="margin-left: -8px; margin-top: -8px; height: 16px; transform: translate3d(871px, -108px, 0px);"',
    'Camelot': 'style="margin-left: -8px; margin-top: -8px; height: 16px; transform: translate3d(810px, 343px, 0px);"',
    'Arizona': 'style="margin-left: -8px; margin-top: -8px; height: 16px; transform: translate3d(-334px, -21px, 0px);"'
}

# Main Loop
start = str(input('\nOpen Browser? (Y/N)')).lower()
scraper = TownScraper(towns, world)
while start == 'y':
    scraper.scrape_towns()
    start = str(input('do you want to rescan? (Y/N): ')).lower()
if start != "y":
    scraper.quit()

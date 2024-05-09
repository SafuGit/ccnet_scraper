# ccnet_scraper
this is a WebScraper that extracts data from the popular geopolital game CCNets Map Website, and gives you their Upkeep and Bank Amount values.

## How to add more towns?
This app uses HTML XPaths to track the location of each town. now as a demo there is already 4 towns listed in the software but if you want to add functionality for more towns here is the step by step guide

**1. Open Edge Developer tools**

**2. Inspect the town icon**

**3. Click the element above the town icon element**

**4. Right click and select copy XPath**

**5. Type the town name in quotation marks on the left side and value in the right side example:-**

'Envy': '//* [@id="app"]/div[1]/div[1]/div[10]/div[697]'

## How to use?
Just run the main.py script, and correctly input the questions and it will open a new microsoft edge instance and your result will be outputted in the console!

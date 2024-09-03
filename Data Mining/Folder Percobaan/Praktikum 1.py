Import ModulePython
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def scraper(url):
    print("isinya scraper")
    try :
        # Configure WebDriver to use headless Firefox
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
    except Exception as e :
        #print The error Message
        print('error: ',e)

if __name__ =='__main__'
    print("main")
    url="https://www.dicoding.com/blog/tutorial-membuat-web-scraper-dengan-python/ 
    scraper(url)
"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json

def scraper(url):
    print('Scraping Lazada...')
    try:
        # Configure WebDriver to use headless Firefox
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        
        # Get the URL given
        driver.get(url)

        # Wait for the page to load by checking the presence of a reliable element
        try:
            wait = WebDriverWait(driver, timeout=10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-qa-locator="product-item"]')))
            print('Element present')
        except:
            raise LookupError("The specified element was not found.")

        # BeautifulSoup to parse the URL
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')

        # Prepare the variable for JSON data
        Handphone = []
        
        # Find all product containers
        for hp in soup.find_all('div', {'data-qa-locator': 'product-item'}):
            content_hape = hp.find('a', {'data-qa-locator': 'product-item-title'}).text.strip()
            content_harga = hp.find('span', {'class': 'ooOxS'}).text.strip()
            content_diskon = hp.find('span', {'class': 'qzqFw'}).text.strip() if hp.find('span', {'class': 'qzqFw'}) else ''
            content_terjual = hp.find('div', {'class': '_6uN7R'}).find('span').text.strip() if hp.find('div', {'class': '_6uN7R'}) else ''
            
            # Append the scraped data into the Handphone list
            Handphone.append(
                {
                    'Nama Barang': content_hape,    
                    'Harga': content_harga,    
                    'Total Terjual': content_terjual,    
                    'Total Diskon': content_diskon
                }
            )
        
        # Close the WebDriver
        driver.quit()

        print(Handphone)
        return Handphone

    except Exception as e:
        print('Error:', e)
        driver.quit()

if __name__ == '__main__':
    print('Starting...')
    url = "https://www.lazada.co.id/beli-handphone/?up_id=7932874482&clickTrackInfo=matchType--20___description--Diskon%2B3%2525___seedItemMatchType--c2i___bucket--0___spm_id--category.hp___seedItemScore--0.0___abId--333258___score--0.097348616___pvid--ef167e71-4f26-49ac-a4a1-66250324690b___refer--___appId--7253___seedItemId--7932874482___scm--1007.17253.333258.0___categoryId--3443___timestamp--1725292040063&from=hp_categories&item_id=7932874482&version=v2&q=Handphone&params=%7B%22catIdLv1%22%3A%223441%22%2C%22pvid%22%3A%22ef167e71-4f26-49ac-a4a1-66250324690b%22%2C%22src%22%3A%22ald%22%2C%22categoryName%22%3A%22Handphone%22%2C%22categoryId%22%3A%223443%22%7D&src=hp_categories&spm=a2o4j.homepage.categoriesPC.d_2_3443"
    data = scraper(url)
    
    # Save data to JSON file
    with open('dicoding_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

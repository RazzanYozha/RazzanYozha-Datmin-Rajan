from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json
def scraper(url):
    print('mau scraper Lazada')
     #Function to scrape data from Dicoding
    try:
        # Configure WebDriver to use headless Firefox
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        
        # Get the URL given
        driver.get(url)
 
        # Selenium will wait for a maximum of 5 seconds for an element matching the given criteria to be found. 
        # If no element is found in that time, Selenium will raise an error.
        try:
            wait = WebDriverWait(driver, timeout=5)
            wait.until(EC.presence_of_element_located((By.ID, 'root')))
            print('element present')
        except:
            raise LookupError("There is no element specified")
        # BeautifulSoup will parse the URL
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
 
        # Prepare the variable for JSON data
        Handphone = []
        
        # BeautifulSoup will find the CSS class that contain product container
        for hp in soup.find_all('div', class_='Bm3ON'):
            content_hape = hp.find('div', class_ = 'RfADt').text
            content_harga = hp.find('span', {'class':'ooOxS'}).text

            content_diskon = hp.find('span', {'class' :'qzqFw'}).text
            # content_domisili = hp.find_all('div',{'class':'oa6ri'})[2].find['title'].get_text()
            content_domisili = hp.find('span',class_='oa6ri')
            content_domisilis = content_domisili['title'] if content_domisili else None

            # content_hape = hp.find_all('span', {'class':'css-20kt3o'})[0].text
            # content_hape = hp.find_all('span', {'class':'css-20kt3o'})[0].text
            
            # Get the text from the specified element and assign them to the variables
            # course_name = hp.find_all('span', {'class':'VKNwBTYQmj8+cxNrCQBD6g=='})[0].text 
            
            try:
                content_terjual = hp.find_all('div', class_ = '_6uN7R')[0].find('span').get_text()
                # content_domisili = hp.find_all('div',{'class':'oa6ri'})[2].find['title'].get_text()
                
            except IndexError:
                # Handle the case when no span elements with the specified class are found
               
                content_terjual = ''
            # try:
            #     content_domisili = hp.find_all('div',{'class':'_6uN7R'})[2].find('span').get_text()

            # except IndexError:

            #     content_domisili = ''


                
            # Append the scraped data into courses variable for JSON data

            Handphone.append(
                {
                    'Nama Barang':  content_hape,    
                    'Harga':  content_harga,    
                    'tottal terjual':  content_terjual,    
                    'total rating': content_diskon,
                    'Kota' : content_domisilis
                }
            )
        print(Handphone)
        
        # Close the WebDriver
        driver.quit()
 
        return Handphone
    except Exception as e:
        print('error: ', e)

if __name__ == '__main__':
    print('mulai')
    url = "https://www.lazada.co.id/beli-handphone/?up_id=7932874482&clickTrackInfo=matchType--20___description--Diskon%2B3%2525___seedItemMatchType--c2i___bucket--0___spm_id--category.hp___seedItemScore--0.0___abId--333258___score--0.097348616___pvid--ef167e71-4f26-49ac-a4a1-66250324690b___refer--___appId--7253___seedItemId--7932874482___scm--1007.17253.333258.0___categoryId--3443___timestamp--1725292040063&from=hp_categories&item_id=7932874482&version=v2&q=Handphone&params=%7B%22catIdLv1%22%3A%223441%22%2C%22pvid%22%3A%22ef167e71-4f26-49ac-a4a1-66250324690b%22%2C%22src%22%3A%22ald%22%2C%22categoryName%22%3A%22Handphone%22%2C%22categoryId%22%3A%223443%22%7D&src=hp_categories&spm=a2o4j.homepage.categoriesPC.d_2_3443"
    data = scraper(url)
    # Save data to JSON file
    with open('dicoding_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json

def scraper(url):
    print("isinya scraper")
    try :
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
            wait.until(EC.presence_of_element_located((By.ID,'zeus-root')))
            print('element present')
        except:
            raise LookupError("There is no element specified")
        
        # BeautifulSoup will parse the URL
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
 
        # Prepare the variable for JSON data
        barangs = []
        # BeautifulSoup will find the CSS class that contain product container
        for barang in soup.find_all('div',class_="css-bk6tzz e1nlzfl2"):
            
            # Get the text from the specified element and assign them to the variables
            try :
                barang_name = barang.find_all('span', class_="css-20kt3o")[0].text
                barang_price = barang.find_all('span', class_="css-o5uqvq")[0].text
            except IndexError:
                barang_name = ''
                barang_price =''
                
            # barang_price = barang.find('div', {'class'="_8cR53N0JqdRc+mQCckhS0g== Phc0SDQ0Yjt43vf3XuwYOg=="}).text
            # domisili_barang = barang.find('span',{'class':"prd_link-shop-loc css-1kdc32b"}).text
            # penjualan_barang = barang.find('span', class_="eLOomHl6J3IWAcdRU8M08A==").text
            # rating_barang = barang.find('span', class_="nBBbPk9MrELbIUbobepKbQ==").text
            

            
            # Append the scraped data into courses variable for JSON data
        barangs.append(
                {
                    'Nama Barang': barang_name,
                    'Harga': barang_price,
                    # 'Domisili Penjual': domisili_barang,
                    # 'Jumlah Terjual': penjualan_barang,
                    # 'Rating': rating_barang,
                }
            )
            
        # Close the WebDriver
        driver.quit()
 
        return barangs
    
    except Exception as e :
        #print The error Message
        print('error: ',e)

        #Close The Webdriver
        driver.quit()

if __name__ == '__main__':
    # Define the URL
    url = 'https://www.tokopedia.com/p/dapur/aksesoris-dapur'
 
    data = scraper(url)
 
    # Save data to JSON file
    with open('Data_Tokopedia', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        


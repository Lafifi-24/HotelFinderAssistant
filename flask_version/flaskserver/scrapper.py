import re

import requests
from seleniumbase import Driver
from bs4 import BeautifulSoup



class Hotel:
    def __init__(self):
        self.name = None
        self.stars = None
        self.link = None
        self.price = None
        self.score = None
        self.taxes = None
        self.suggestions = None
        self.client_order = None
    
    def extract_hotel_info(self,soup: BeautifulSoup):
        self.name = soup.find("div", {"data-testid": "title"}).text
        try :
            self.stars = int(soup.find("div", {"aria-label":re.compile(".*out of.*")})['aria-label'][0])
        except:
            self.stars=0
        try : 
            self.score = float(soup.find("div", {"aria-label": re.compile("Scored")}).text)
        except:
            self.score = 0
        self.price = soup.find("span", {"data-testid": "price-and-discounted-price"}).text
        self.taxes = soup.find("div", {"data-testid": "taxes-and-charges"}).text
        self.client_order = soup.find("div", {"data-testid":"price-for-x-nights"}).text
        self.link = soup.find("a", {"data-testid":"availability-cta-btn"})['href']
        self.suggestions = " + ".join([suggestion.text for suggestion in soup.find_all("h4", {"role":re.compile("link")})])
    
    
class BookingScrapper:
    def __init__(self):
        
        self.booking_url = "https://www.booking.com/searchresults.en-gb.html"
        
    def build_path(self,params):
        path = self.booking_url + '?ss=' + params['city'] + ',' + params['country']
        for key in params.keys():
            if key in ['checkin','checkout','group_adults','no_rooms','group_children','age'] and params[key] != 'none':
                if isinstance(params[key],list):
                    for value in params[key]:
                        path += '&'+key+'='+str(value)
                else:
                    path += '&'+key+'='+str(params[key])
            if key in ['class'] and params[key] != 'none':
                path += '&nflt=class%3D'+params["class"]
        path += '&selected_currency=USD'
        return path
        
        
    def scrape(self,params):

        
        path = self.build_path(params)
        print('Start')
                
        driver = Driver(uc=True, headless=True)
        driver.get(path)
        import time
        print('get_path')
        try :
            print('try')
            driver.click("//button[@aria-label='Dismiss sign in information.']")
        except :
            print('pass')
            pass
        soup = BeautifulSoup(driver.page_source,features="html.parser")
        print(path)
        file = open("result.txt", "w")
        
 
        
        file.write(soup.prettify())
        
        #close file
        file.close()
        driver.quit()
        hotels=[]
        for hotel_info in soup.find_all("div", {"data-testid": "property-card-container"}):
            hotel = Hotel()
            hotel.ExtractHotelInfo(hotel_info)
            hotels.append(hotel)
        
        return hotels
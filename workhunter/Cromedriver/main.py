import requests
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#constants
ask = input('Введите вакансию для поиска : ')
URL = 'https://hh.ru/search/vacancy?text='+ask+'&area=1'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'}
#DRIVEPATH = "C:\Projects\workhunter\Cromedriver\chromedriver.exe"
#options
#options = webdriver.ChromeOptions()
#options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36')


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    work = soup.find('div', class_='serp-item')
    workhref = soup.find_all('a', class_='serp-item__title')
    
    workhref_href = []
    for i in workhref:
        hr = i.get('href')
        workhref_href.append(hr)
    
    workhref_title = []
    for i in workhref:
        ti = i.get('title')
        workhref_title.append(ti)  
        #f = open('work.txt', 'a')
    try:            
      for n in range(15, 30):
        print(workhref_title[n])
        print(workhref_href[n])
        webbrowser.open(workhref_href[n])
        #for site in workhref_href[n]:
         #   driver = webdriver.Chrome(
          #     executable_path=DRIVEPATH, 
           #    options=options
           # )
            #driver.get(workhref_href[n])
            #time.sleep(33)        
            #n=+1 
        #webbrowser.open(a)
    except Exception as ex:
       print(ex)       
    #finally:
        #driver.close()
        #driver.quit()                   
       #element = driver.find_element_by_class("bloko-button bloko-button_kind-success bloko-button_scale-large bloko-button_stretched")
       #element.click()
def parse():
    html = get_html(URL)
    if html.status_code == 200:
       get_content(html.text)
    else:
        print('Error')    
    
parse()
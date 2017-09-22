# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
2
3
#import sys
#sys.path.insert(0, 'D:\\Program_Files\\Python\\Lib\\site-packages\\')
#sys.path
## Ici on teste cinq librairies conseillées


#%% 1) Essai de la première librairie : requests
import requests
page = requests.get('http://www.google.fr')
contents = page.content
print(contents)


#%% 2) Essai de la deuxième librairie : Beautifulsoup	
from bs4 import BeautifulSoup
soup1 = BeautifulSoup(contents, 'html.parser')
contents2=soup1.find_all('div')




#%% 3) Troisième librairie : Ixml
from lxml import html
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')



#%% 4) Quatrième librairie
import selenium




#%% 5) Utilisation de Scrapy
import scrapy

class SncfSpider(scrapy.Spider):
    name = "Ferroviaire_trainline"  # Name of the Spider, required value
    start_urls = ["https://www.trainline.fr"]  # The starting url, Scrapy will request this URL in parse




        
        
        
        
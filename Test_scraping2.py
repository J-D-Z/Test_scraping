# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:03:08 2017

@author: NHNBYB
"""

import scrapy

class SncfSpider(scrapy.Spider):
    name = "Ferroviaire_trainline"  # Name of the Spider, required value
    start_urls = ["https://www.trainline.fr"]  # The starting url, Scrapy will request this URL in parse

//*[(@id = "ember1132")] | //*[contains(concat( " ", @class, " " ), concat( " ", "search__add-participants", " " ))]//*[(@id = "ember1156")]//*[(@id = "ember1142")]//*[(@id = "ember1109")]//*[(@id = "ember1100")]


# -*- coding: utf-8 -*- 
import shutil # to save it locally
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict
import csv
import time
import sys
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

geckodriver_autoinstaller.install()

optionsFox = Options()
optionsFox.headless = True
driverFox = webdriver.Firefox(options=optionsFox)
print ("Headless Firefox Initialized")


#  -------- FUNCTIONS --------

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#  -------- / FUNCTIONS -------

# ook = Workbook()
# sheet = book.active
# rows = []b

dict = {}
arr = []

# BEJELENTKEZÉS -- DRIVER
with open("urllist4.txt", "a") as myfile:
    driverFox.get( "https://www.autodoc.hu/jarmu-alkatreszek" )
    categories = driverFox.find_elements_by_class_name("list_links")
    # print (len(categories))
    for cat in categories:
        lis = cat.find_elements_by_tag_name("span")
        for k in lis:
            # print (k.get_attribute("url") + "\n")
            if k.get_attribute("url") is not None:
                print (k.get_attribute("url"))
                myfile.write(k.get_attribute("url") + "\n")

        lis2 = cat.find_elements_by_tag_name("a")
        for k2 in lis2:
            # print (k.get_attribute("url") + "\n")
            if k2.get_attribute("href") is not None:
                print (k2.get_attribute("href"))
                myfile.write(k2.get_attribute("href") + "\n")


def urlspan( url ):
    driverFox.get( url )
    carlist = ""
    modellist = ""
    typelist = "" 
    carlist = driverFox.find_elements_by_xpath("//*[@id="form_maker_id"]/optgroup/option")




   


# //*[@id="category-10341"]
# username = driver.find_element_by_id("system_login")
# username.clear()
# username.send_keys("gigor.lorant@gmail.com")
# password = driver.find_element_by_id("system_pass")
# password.clear()
# password.send_keys("wokxy3-Hejfom-fezdiw")
# driver.find_element_by_id("shopuser_login_button").click()

# BEJELENTKEZÉS -- DRIVER2
# driver2.get( "https://panzishop.hu/" )
# username = driver2.find_element_by_id("system_login")
# username.clear()
# username.send_keys("gigor.lorant@gmail.com")
# password = driver2.find_element_by_id("system_pass")
# password.clear()
# password.send_keys("wokxy3-Hejfom-fezdiw")
# driver2.find_element_by_id("shopuser_login_button").click()

# book = Workbook()
# sheet = book.active
# rows = []

# counter = 0
# links5 = []
# name = ""
# category = ""
# price = ""
# secd = ""
# description = ""

# file = open('productlinks2.txt', 'r')
# Lines = file.readlines() 


# for p in Lines:
#     counter += 1
#     # if ( counter > 1000):
#     #     break
#     print ( counter )
#     print ( p )
#     print ( "***** " + p )
#     driver.get( p )
#     if len( driver.find_elements_by_xpath("//a") ) < 3:
#         continue
#     # ár
#     prices = driver.find_elements_by_xpath("//div[starts-with(@class, 'price')]/span")
#     price = prices[0].text
#     # név
#     name = driver.find_element_by_xpath("//div[starts-with(@class, 'col-md-5')]/H1").text
#     print ( str (counter) + " :  " + name + " -- " + price)
#     # kategória
#     cats = driver.find_elements_by_xpath("//div[starts-with(@class, 'page-title-address text-right')]/a")
#     category = ""
#     for cat in cats:
#         category = category + "*" + cat.text
#     # leírás
#     descs = driver.find_elements_by_xpath("//div[starts-with(@class, 'col-md-5')]/p")
#     for d in descs:
#         description = description + " " + d.text
#     # cikkszám
#     sku = driver.find_element_by_xpath("//span[starts-with(@class, 'gray-italic')]").get_attribute('innerHTML')
#     print ( sku )
#     rows.insert( 0, ( sku, name, description, price,  category ))
#     description = ""

# for row in rows:
#     sheet.append(row)

# book.save('panzi4.xlsx')

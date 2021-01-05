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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

geckodriver_autoinstaller.install()

optionsFox = Options()
optionsFox.headless = False
driverFox = webdriver.Firefox(options=optionsFox)

selectArr = []

# with open("triples.txt") as file_in:
#     for line in file_in:
#         x = line.split(";")


with open("urllist3.txt") as file_in:
    for line in file_in:
        getdata(line)

getdata(url):
    # driverFox.get( url )

    # makerselect = driverFox.find_elements_by_xpath("//select[@id='form_maker_id']/optgroup[@label='Gépkocsigyártók abc sorrendben']")
    # modelselect = driverFox.find_elements_by_xpath("//select[@id='form_model_id']/optgroup[@label='...']")
    # carselect = driverFox.find_elements_by_xpath("//select[@id='form_car_id']/optgroup[@label='...']")
   
    with open("triples.txt") as file_in:
        for line in file_in:
            x = line.split(";")
            


    
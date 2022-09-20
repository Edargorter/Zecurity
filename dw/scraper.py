#!/usr/bin/env python3 

# Inspired by https://towardsdatascience.com/how-to-scrape-the-dark-web-53145add7033

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd

ff_path = "/usr/bin/firefox"
ff_path = "/usr/lib/firefox"
#ff_path = "/etc/firefox"

binary = FirefoxBinary(ff_path)
driver = webdriver.Firefox(firefox_binary=binary)

url = "https://edargorter.xyz"

driver.get(url)

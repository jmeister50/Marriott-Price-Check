from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import config as cfg

url = cfg.url
browser = webdriver.Chrome(cfg.driver)

def search_city(city):
	
	browser.get(url)

	element = WebDriverWait(browser, 20).until(
		EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced-search-form"]/div/div[1]'))
		)
	element.click()

	browser.find_element_by_name('destinationAddress.destination').send_keys(city)

	element = WebDriverWait(browser, 20).until(
		EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced-search-form"]/div/div[9]/button'))
		)
	element.click()

	#TODO: Add filtering logic here

	hotel_names = browser.find_elements_by_class_name('l-property-name')
	hotel_prices = browser.find_elements_by_class_name('m-display-block')
	
	names = []
	for name in hotel_names:
		names.append(name.text)

	prices = []
	for price in hotel_prices:
		if len(price.text) > 0:
			prices.append(price.text)
		else:
			pass

	hotel_info = dict(zip(names,prices))
	print(hotel_info)

search_city('Chicago, IL')
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

def wait_until_clickable_xpath(xpath):

	element = WebDriverWait(browser, 20).until(
		EC.element_to_be_clickable((By.XPATH, str(xpath)))
		)
	element.click()

def search_city(city, state, start_date, end_date):
	
	# Go to starting url
	browser.get(url)

	# Clicking Destination Form Box. 
 	wait_until_clickable_xpath('//*[@id="advanced-search-form"]/div/div[1]')

 	# Sending City and State to destination box. 
	browser.find_element_by_name('destinationAddress.destination').send_keys(city + ', ' + state)
	element.click()

	# TODO: Finish date functionality
	element = browser.find_elements_by_class_name('ccheckin')

	# TODO: Add filtering logic here
	# Clicking the Search Button.
	wait_until_clickable_xpath('//*[@id="advanced-search-form"]/div/div[9]/button')

	# Create list of Hotel names and Rates. 
	hotel_names = browser.find_elements_by_class_name('l-property-name')
	hotel_prices = browser.find_elements_by_class_name('m-display-block')

	# Append name of Hotel to list.
	names = []
	for name in hotel_names:
		names.append(name.text)

	# Append Rate to list. 
	prices = []
	for price in hotel_prices:
		if len(price.text) > 0:
			prices.append(price.text)
		else:
			pass

	# Pairs names and rates in a Dictionary.
	hotel_info = dict(zip(names,prices))
	print(hotel_info)

search_city('Chicago', 'IL', 1, 1)
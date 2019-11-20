"""
Python script dynamic_web_scraping.py is used to scrape content from dynamic web pages
Packages that we have to install are: Selenium, WebDriver, BeautifulSoup
Selenium needs webdriver to interface with web browser
python3 -m pip install selenium, beautifulsoup4 
"""

from selenium import webdriver # have to be installed 
from bs4 import BeautifulSoup # have to be installed
import time

# opening web page
driver = webdriver.Chrome() # instantiate Chrome driver
# driver.get('https://pluralsight.com/') # opening web page

# close previous opened web browser window
#driver.quit()

# opening web page with argument
# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito") # open in icognito window
# options.add_argument("--kiosk") # maximize window
# options.add_argument("--headless") # web browser without GUI
# driver = webdriver.Chrome(options=options)
keys = webdriver.common.keys.Keys()

driver.get('https://pluralsight.com/')
# driver.get('https://python.org/')

ele = driver.find_element_by_name('q') # find element by name
time.sleep(1)
ele.clear()
ele.send_keys('Patheerth Padman') # fulfill input fileld name = q with name in brackets 
ele.send_keys(keys.RETURN) # press ENTER

# ele_link = driver.find_element_by_link_text('Building Image Classification Solutions Using Keras and Transfer Learning')
# ele_link = driver.find_element_by_partial_link_text('Building Image')
ele_link = driver.find_element_by_link_text('Courses')
time.sleep(1)
ele_link.click()
time.sleep(1)

ele_link_txt = driver.find_element_by_link_text('Building Image Classification Solutions Using Keras and Transfer Learning')
time.sleep(1)
ele_link_txt.click()


# time.sleep(5)
# driver.quit()

# ele = driver.find_element_by_id('id-search-field') # find element by id
# ele = driver.find_element_by_link_text()
# time.sleep(1)
# ele.clear()
# ele.send_keys('lists') # fulfill input fileld id = 'id-search-field' with name in brackets 
# ele.send_keys(keys.RETURN) # press ENTER
# time.sleep(5)
# driver.quit()


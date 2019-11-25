"""
Python script dynamic_web_scraping.py is used to scrape content from dynamic web pages
Packages that we have to install are: Selenium, WebDriver, BeautifulSoup
Selenium needs webdriver to interface with web browser
python3 -m pip install selenium, beautifulsoup4 
"""

from selenium import webdriver # have to be installed 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup # have to be installed
import time

########## Adding options on Chrome ###################################
chrome_options = Options()
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--incognito") # open in icognito window
chrome_options.add_argument("--kiosk") # maximize window
# chrome_options.add_argument("--headless") # web browser without GUI
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--disable-infobars") # prevents Chrome from displaying the notification 'Chrome is being controlled by automated software
# chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})


########## Navigate to web site page #################################
driver = webdriver.Chrome(options=chrome_options)  # instantiation Chrome driver w/ options
# driver = webdriver.Chrome() # instantiation Chrome driver w/o options
driver.get('https://premierleague.com/') # opening web page
# driver.get('https://pluralsight.com/')
# driver.get('https://python.org/')
# cookies_ele = driver.find_element_by_link_text('I accept cookies from this site').click()
try:
    advert_close = driver.find_element_by_id("advertClose").click()
except:
    print('No advert')

try:
    cookie_wind = driver.find_element_by_xpath('//div[@class="btn-primary cookies-notice-accept"]').click()
except:
    print('No cookies window')

players_ele = driver.find_element_by_link_text('Players').click() # find element and click on tab Players
# ele_link = driver.find_element_by_link_text('Building Image Classification Solutions Using Keras and Transfer Learning')
# ele_link = driver.find_element_by_partial_link_text('Building Image')
# ele_link = driver.find_element_by_link_text('Courses')
# ele = driver.find_element_by_name('q') # find element by name
# ele = driver.find_element_by_xpath('//input[@name="q"]') # find element by name

try:
    advert_close = driver.find_element_by_id("advertClose").click()
except:
    print('No advert')

try:
    cookie_wind = driver.find_element_by_xpath('//div[@class="btn-primary cookies-notice-accept"]').click()
except:
    print('No cookies window')

########## web driver wait ##
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search-input")))

search_ele = driver.find_element_by_id("search-input")
# ele = driver.find_element_by_id('id-search-field') # find element by id
# search_ele.clear()
search_ele.send_keys("Wayne Rooney")
# ele.send_keys('Patheerth Padman') # fulfill input fileld name = q with name in brackets
# # ele.send_keys('lists') # fulfill input fileld id = 'id-search-field' with name in brackets 
time.sleep(1)

keys = Keys() 
search_ele.send_keys(keys.RETURN) # keys = Keys() keys.RETURN
time.sleep(1)

try:
    cookie_wind = driver.find_element_by_xpath('//div[@class="btn-primary cookies-notice-accept"]').click()
except:
    print('No cookies window')


# driver.implicitly_wait(2)
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Photo for Wayne Rooney']")))
# click_wayne = driver.find_element_by_xpath("//img[@alt='Photo for Wayne Rooney']").click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@data-player='p13017']")))
click_wayne = driver.find_element_by_xpath("//img[@data-player='p13017']").click()

time.sleep(1)

try:
    advert_close = driver.find_element_by_id("advertClose").click()
except:
    print('No advert')

page_source_overview = driver.page_source


########################## BeautifulSoup ########################################################
soup = BeautifulSoup(page_source_overview, 'lxml')

title_finder = soup.find_all("span", class_ = "title")

print(title_finder)

print('\n'+'*'*10 + " These are the leatest news headlines about Wayne Rooney " + "*"*10 + '\n')
for title in title_finder:
    print(title.string)




# close previous opened web browser window
#driver.quit()





time.sleep(5)
driver.quit()




"""
Python script dynamic_web_scraping.py is used to scrape content from dynamic web pages
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://app.pluralsight.com/search/?q=python%20web%20scraping&m_sort=relevance&page=1&query_id=065549a7-753b-460c-98cf-4461f6f146e3')
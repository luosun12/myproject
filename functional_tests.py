from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhsot:8000')

assert 'Django' in browser.page_source
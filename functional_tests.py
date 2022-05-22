from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-profile")
options.add_argument("/home/pedro/snap/firefox/common/.mozilla/firefox/va7i427w.pedro")
browser=webdriver.Firefox(options=options)

browser.get('http://localhost:8000')

assert 'Django' in browser.title


	


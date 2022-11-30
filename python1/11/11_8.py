from selenium import webdriver

browser = webdriver.Chrome()
print(type(browser))
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
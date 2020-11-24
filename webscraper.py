from selenium import webdriver

url = 'https://www.youtube.com/c/Pranavchandran/videos'

browser = webdriver.Firefox(executable_path="/root/scraping_project/geckodriver.exe")
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()


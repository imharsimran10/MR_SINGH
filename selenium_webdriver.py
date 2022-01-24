from selenium  import webdriver

class infow():
    def __init__(self):
        #set Chrome path acc to your pc ikku
        self.driver = webdriver.Chrome(executable_path='C:/Users/imhar/OneDrive/Desktop/chromedriver.exe')

    def get_info(self,text):
        self.text = text
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(text)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()



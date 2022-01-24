from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/imhar/OneDrive/Desktop/chromedriver.exe')

    def play(self,text):
        self.text = text
        self.driver.get(url='https://www.youtube.com/results?search_query=' + text)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()
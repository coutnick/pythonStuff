import time
from selenium import webdriver

driver = webdriver.Chrome()

class Browser:
    def __init__(self, driver: str):
        print('Starting up...')
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        print(f'Opening: {url}')
        self.browser.get(url)


if __name__ == "__main__":
    browser = Browser('chromedriver')

    browser.open_page('https://www.python.org')
    time.sleep(5)
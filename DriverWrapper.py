from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DriverWrapper:
    def __init__(self, base_url):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = base_url

    def open_page(self, path=""):
        full_url = f"{self.base_url}/{path.strip('/')}" if path else self.base_url
        self.driver.get(full_url)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class FlagScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.flags = []

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)

    def scrape_flags_general(self):
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'flag-') or contains(@id, 'flag-') or contains(@class, 'flag-')]")
        for element in elements:
            possible_flags = re.findall(r'flag-\d+', element.text + element.get_attribute('id') + element.get_attribute('class'))
            for flag in possible_flags:
                if flag not in self.flags:
                    self.flags.append(flag)
                    print(flag)

    def click_and_capture_flags(self, start, end):
        for i in range(start, end + 1, 2):
            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, f'flag-{i}'))
                )
                button.click()
                time.sleep(2)
                flag = f"flag-{i + 1}"  # Assuming subsequent flag ID
                if flag not in self.flags:
                    self.flags.append(flag)
                    print(flag)
            except Exception as e:
                print(f"Button with ID flag-{i} not found. Error: {e}")

    def enter_text_and_capture_flag(self):
        try:
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'input'))
            )
            input_field.send_keys('!!flag-61!!')
            time.sleep(2)
            flag = self.driver.find_element(By.XPATH, "//div[contains(text(), 'flag-61')]").text
            if flag not in self.flags:
                self.flags.append(flag)
                print(flag)
        except Exception as e:
            print("Final flag not found. Error:", e)

    def run(self):
        self.open_page("https://hertie-scraping-website.vercel.app/")
        self.scrape_flags_general()  # Adjusted to a more general method

        self.open_page("https://hertie-scraping-website.vercel.app/wowimlevel2")
        self.scrape_flags_general()

        self.open_page("https://hertie-scraping-website.vercel.app/goodjobfindinglevel3")
        self.click_and_capture_flags(55, 59)

        self.open_page("https://hertie-scraping-website.vercel.app/finalboss")
        self.enter_text_and_capture_flag()

        self.driver.quit()
        self.print_all_flags()

    def print_all_flags(self):
        print("\nAll collected flags:")
        for flag in sorted(self.flags, key=lambda x: int(re.search(r'\d+', x).group())):
            print(flag)

if __name__ == "__main__":
    scraper = FlagScraper()
    scraper.run()

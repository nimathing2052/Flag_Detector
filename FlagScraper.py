import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FlagScraper:
    def __init__(self, driver_wrapper):
        self.driver = driver_wrapper
        self.flags = []

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

    def print_all_flags(self):
        print("\nAll collected flags:")
        for flag in sorted(self.flags, key=lambda x: int(re.search(r'\d+', x).group())):
            print(flag)
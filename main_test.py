import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Main:
    def __init__(self, url):
        self.url = url

    def run(self):
        # Initialize the Chrome driver with WebDriver Manager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        try:
            # Go to the URL
            driver.get(self.url)
            driver.maximize_window()

            # Capture initial list of flags using their specific IDs
            first_list_elements = driver.find_elements(By.XPATH, "//*[contains(@id, 'nesting-')]")
            first_list_flags = [elem.text for elem in first_list_elements if 'flag-' in elem.text]

            # Use JavaScript to get all elements in the document
            all_elements = driver.execute_script("return document.querySelectorAll('*');")

            # Initialize a set to keep unique flag identifiers
            flags_set = set(first_list_flags)

            for element in all_elements:
                # Extract 'id' and 'class' attributes
                elem_id = element.get_attribute('id')
                elem_class = element.get_attribute('class')

                # Check if 'flag-' is in the id or class attribute (starts with 'flag-')
                if elem_id.startswith('flag-'):
                    flags_set.add(elem_id)
                if any(cls.startswith('flag-') for cls in elem_class.split()):
                    flags_set.add(elem_class)

            # Combine counts and print each flag
            for flag in flags_set:
                print(flag)

            print(f"Total unique 'flag-' occurrences: {len(flags_set)}")

        except Exception as e:
            print("Sorry, something went wrong:", e)

        finally:
            # Close the driver
            driver.quit()


if __name__ == '__main__':
    program = Main("https://hertie-scraping-website.vercel.app/")
    program.run()

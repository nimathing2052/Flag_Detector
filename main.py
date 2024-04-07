import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Main:
    def __init__(self, url):
        self.url = url

    def run(self):
        # initialize the Chrome driver with WebDriver Manager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        try:
            # go to the URL
            driver.get(self.url)
            driver.maximize_window()

            # Find all elements with the ID 'nesting-1' (if there are multiple elements with this ID)
            first_list_elements = driver.find_elements(By.ID, "nesting-1")
            first_list_texts = [elem.text for elem in first_list_elements]  # Get the text of each element

            # Find all the div elements with the class 'size-10'
            # Find all div elements within 'size-10' divs that have an id or class containing 'flag-'
            size_10_elements = driver.find_elements(By.XPATH,
                                                    "//div[@class='size-10']/div[contains(@id, 'flag-') or contains(@class, 'flag-')]")

            # Capture the id attribute of each 'size-10' element
            flags_list = []
            for index, size_10_element in enumerate(size_10_elements, start=1):
                # Try to get the 'id' attribute first
                flag_attribute = size_10_element.get_attribute('id')
                # If 'id' is empty or doesn't contain 'flag-', try to get the 'class' attribute
                if not flag_attribute or 'flag-' not in flag_attribute:
                    flag_attribute = size_10_element.get_attribute('class')
                # Append the relevant attribute to the list, default to "No Flag" if neither attribute contains 'flag-'
                flags_list.append(flag_attribute if 'flag-' in flag_attribute else "No Flag")

            # Combine the two lists
            combined_list = first_list_texts + flags_list

            # Print each element of the combined list
            for item in combined_list:
                print(item)


        except Exception as e:
            print("Sorry, something went wrong:", e)

        finally:
            # close the driver
            driver.quit()


if __name__ == '__main__':
    program = Main("https://hertie-scraping-website.vercel.app/")
    program.run()


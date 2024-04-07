from DriverWrapper import DriverWrapper
from FlagScraper import FlagScraper


class FlagFinder:
    def __init__(self):
        base_url = "https://hertie-scraping-website.vercel.app"
        self.driver_wrapper = DriverWrapper(base_url)
        self.scraper = FlagScraper(self.driver_wrapper.driver)  # Pass the actual WebDriver

    def run(self):
        self.driver_wrapper.open_page()
        self.scraper.scrape_flags_general()
        self.driver_wrapper.open_page("wowimlevel2")
        self.scraper.scrape_flags_general()
        self.driver_wrapper.open_page("goodjobfindinglevel3")
        self.scraper.click_and_capture_flags(55, 59)
        self.driver_wrapper.open_page("finalboss")
        self.scraper.enter_text_and_capture_flag()
        self.driver_wrapper.quit()

    def print_all_flags(self):
        self.scraper.print_all_flags()


if __name__ == "__main__":
    flag_finder = FlagFinder()
    flag_finder.run()

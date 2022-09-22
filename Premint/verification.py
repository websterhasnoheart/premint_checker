from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# from selenium.webdriver.support import expected_conditions as EC

class Verification:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def land_page(self, url):
        self.driver.get(url)

    def check_win(self):
        card = self.driver.find_element(By.CLASS_NAME, "card")
        # heading = card.find_element(By.CLASS_NAME,"heading-1")
        sub_heading = card.find_element(By.CLASS_NAME, "heading-1").text + card.find_element(By.CLASS_NAME, "heading-3").text
        return sub_heading

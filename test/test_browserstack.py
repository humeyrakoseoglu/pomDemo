import time

from selenium import webdriver
from pages.home_page import Homepage
from pages.sign_in_page import SignInPage


class Test:
    driver = webdriver.Chrome()
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    time.sleep(2)
    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    time.sleep(2)
    sign_in_page.click_login()
    time.sleep(2)
    homepage.get_username()
    driver.quit()

import time
from assertpy import assert_that
from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import test_login


@mark.customer
def test_nav_sales(browser, test_login):
    time.sleep(3)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'o_app_icon')])[3]"))).click()
    time.sleep(1)
    # click orders
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//a[contains(.,'Orders')])[1]"))).click()
    time.sleep(3)
    # select draft orders
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Draft Orders')]"))).click()
    time.sleep(10)
    # select create
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Create')]"))).click()
    print("I have clicked")
    time.sleep(5)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//select[contains(@id,'o_field_input_272')]"))).click()
    time.sleep(3)
    # Enter Details here
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "o_field_input_272"))).click()
    time.sleep(1)
    # WebDriverWait(browser, 20).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[@id="o_field_input_741"]"))).click()
    time.sleep(1)

    # Click save
    rsult = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//button[contains(.,'Save')])[1]"))).click()
    time.sleep(1)

    assert_that(rsult).is_true()
    # -------------------------------------------------------------------------------------------------------------
    time.sleep(20)
    browser.close()
# //option value[@
# //*[@id="o_field_input_741"]/option[8]
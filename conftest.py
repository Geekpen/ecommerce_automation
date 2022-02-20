import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
import time


@pytest.fixture
def browser(scope="session"):

    driver_path = 'C:\Projects\Copia\driver\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)

    link = "https://qa.copiadev.copiakenya.com/web"

    driver.get(link)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "// input[ @ id = 'login']")))
    time.sleep(1)
    driver.maximize_window()
    yield driver


@pytest.fixture
def test_login(browser, scope="session"):
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "// input[ @ id = 'login']"))).click()
    time.sleep(1)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "// input[ @ id = 'login']"))).send_keys("test@copiakenya.com")
    time.sleep(1)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).click()
    time.sleep(1)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("79hSF'TaUY6M+~&t1")
    time.sleep(1)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Log in')]"))).click()
    time.sleep(1)

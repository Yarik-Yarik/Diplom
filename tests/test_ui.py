# tests/test_ui.py
from re import search

import pytest
from black.lines import field
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import URL
from test_data import LOGIN_CREDENTIALS
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search_field(browser):
    shop = 'магнит'
    browser.get (URL)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Да")]')))
    yes_button = browser.find_element(By.XPATH, '//span[contains(text(), "Да")]')
    yes_button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="search-input"]')))
    search_field = browser.find_element(By.XPATH, '//input[@data-testid="search-input"]')
    search_field.send_keys(shop)
    search_button = browser.find_element(By.XPATH, '//span[contains(text(), "Найти")]')
    search_button.click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@data-testid="place-header-title"]'),text_='Магнит'))

def test_pozitive_search(browser):
    browser.get (URL)
    sleep(5)
    yes_button = browser.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]')
    yes_button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'input'))).send_keys('Вкусно и точка')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]'))).click()


def test_negative_search(browser):
    browser.get (URL)
    sleep(5)
    yes_button = browser.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]')
    yes_button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'input'))).send_keys('£$!£%^')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]'))).click()

def test_plus_pozition_delivery(browser):
    browser.get(URL)
    sleep(5)
    yes_button = browser.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]')
    yes_button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='ckb1wui'])[3]"))).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[3]/button[1]/*[name()='svg'][1]/*[name()='use'][1]"))).click()
    sleep(4)


def test_minus_pozition_delivery(browser):
    browser.get(URL)
    sleep(5)
    yes_button = browser.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]')
    yes_button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ckb1wui'])[3]"))).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[3]/button[1]/*[name()='svg'][1]/*[name()='use'][1]"))).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='UiKitUiKitIcon_m UiKitUiKitIcon_root UiKitCounter_icon'])[1]"))).click()
    sleep(4)

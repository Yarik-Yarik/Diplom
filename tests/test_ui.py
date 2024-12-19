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

def test_delivery(browser):
    browser.get (URL)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/main/div[10]/div/div/div/div/div/div[10]/div/a/article/section[1]/div/div')))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popular"]/ul/li[7]/div/div[3]/button/span')))
    search_field = browser.find_element(By.XPATH, '//*[@id="main"]/div/div/aside[2]/div/div/div[2]/div[2]/div/div/div/button[2]/span')
    browser.find_element(By.XPATH, '//button[@data-testid="ui-switcher-with-text-option"]').click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//data-testid="bottom-banner-name"]'), text_='Самовывоз'))

def clear_delivery(browser):
    browser.get (URL)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/main/div[10]/div/div/div/div/div/div[10]/div/a/article/section[1]/div/div')))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popular"]/ul/li[7]/div/div[3]/button/span')))
    browser.find_element(By.XPATH, '//*[@id="main"]/div/div/aside[2]/div/div/div[1]/button').click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[3]/div/div/div/div/div/span'), text_='Очистить корзину?'))
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/button[2]').click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="main"]/div/div/aside[2]/div/div/div[2]/h3'),text_='В вашей корзине пока пусто'))


def detected_delivery(browser):
    browser.get (URL)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/main/div[10]/div/div/div/div/div/div[10]/div/a/article/section[1]/div/div')))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popular"]/ul/li[7]/div/div[3]/button/span')))
    browser.find_element(By.XPATH, '//*[@id="main"]/div/div/aside[2]/div/div/div[3]/button[2]').click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(By.XPATH, 'data-testid="desktop-checkout-pay-button'))
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/button[2]').click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="main"]/div/div/aside[2]/div/div/div[2]/h3'),text_='В вашей корзине пока пусто'))

def minus_pozition_delivery(browser):
    browser.get(URL)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div/main/div[10]/div/div/div/div/div/div[10]/div/a/article/section[1]/div/div')))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popular"]/ul/li[7]/div/div[3]/button/span')))
    browser.find_element(By.XPATH, 'data-testid="amount-select-decrement').click()

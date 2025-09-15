import hashlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions



def search_start_head_less():  #不用关驱动

    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('detach', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    chrome = webdriver.Chrome(options=options, service=Service('chromedriver.exe'))
    chrome.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigable, "webdriver", {get: () => undefined})"'
    })
    return chrome

def search_start_no_sand_box():  #不用关驱动
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_experimental_option('detach', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    chrome = webdriver.Chrome(options=options, service=Service('chromedriver.exe'))
    chrome.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigable, "webdriver", {get: () => undefined})"'
    })
    return chrome

def search_start_contain_proxy(driver_proxy):
    options = ChromeOptions()
    options.add_argument('--proxy-server=http://' + driver_proxy)
    options.add_experimental_option('detach', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    chrome = webdriver.Chrome(options=options, service=Service('chromedriver.exe'))
    chrome.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigable, "webdriver", {get: () => undefined})"'
    })
    return chrome

def search_encrypted_something(something_needed):
    first_content = 'abc'
    second_content = 'def'
    third_content = 'ghi'
    full_content = f'{first_content} {second_content} {third_content}{something_needed}'
    result_full_content = hashlib.sha3_256(full_content.encode()).hexdigest()
    return result_full_content


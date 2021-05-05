from tests.helpers.support_functions import *
from time import sleep
from selenium.webdriver.common.keys import Keys

key_tab = 'keypresses-header'
key_content = 'keypresses-content'
key_field = 'target'

def click_key_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, key_tab)
    elem = driver_instance.find_element_by_id(key_tab)
    elem.click()
    sleep(3)


def key_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, key_content)
    return elem.is_displayed()


def click_key_field(driver_instance):
    wait_for_visibility_of_element(driver_instance, key_field)
    elem = driver_instance.find_element_by_id(key_field)
    elem.click()
    sleep(3)
    action = ActionChains(driver_instance)
    action.key_down(Keys.TAB).perform()
    action.key_down(Keys.ENTER).perform()
    action.key_down(Keys.ESCAPE).perform()
    sleep(3)
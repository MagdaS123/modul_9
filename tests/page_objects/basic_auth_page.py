from tests.helpers.support_functions import *
from time import sleep

basic_tab = 'basicauth-header'
basic_content = 'basicauth-content'
username = 'ba_username'
password = 'ba_password'
button = '//*[@id="content"]/button'
button_return = '//*[@id="retrun button"]'

def click_basic_auth_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, basic_tab)
    elem = driver_instance.find_element_by_id(basic_tab)
    elem.click()


def basic_auth_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, basic_tab)
    return elem.is_displayed()


def send_corret_keys_to_username(driver_instance):
    wait_for_visibility_of_element(driver_instance, username, time_to_wait=1)
    elem = driver_instance.find_element_by_id(username)
    elem.send_keys('admin')
    sleep(3)
    value = 'admin'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def send_corret_keys_to_password(driver_instance):
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem = driver_instance.find_element_by_id(password)
    elem.send_keys('admin')
    sleep(3)
    value = 'admin'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def hover_and_click_button(driver_instance):
    hover_over_element(driver_instance, button)
    elem = driver_instance.find_element_by_xpath(button)
    elem.click()
    sleep(3)


def hover_and_click_button_return(driver_instance):
    hover_over_element(driver_instance, button_return)
    elem = driver_instance.find_element_by_xpath(button_return)
    elem.click()
    sleep(3)



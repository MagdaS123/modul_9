from tests.helpers.support_functions import *
#from selenium.webdriver.common.alert import Alert
from time import sleep


form_tab = 'form-header'
form_content = 'form-content'
first_name = 'fname'
last_name = 'lname'
submit = 'formSubmitButton'

def click_form_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, form_tab)
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()
    sleep(3)


def form_tab_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()


def send_corret_keys_to_first_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name, time_to_wait=1)
    elem = driver_instance.find_element_by_id(first_name)
    elem.send_keys('Magda')
    sleep(3)
    value = 'Magda'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def send_corret_keys_to_last_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    elem = driver_instance.find_element_by_id(last_name)
    elem.send_keys('Ślusarczyk')
    sleep(3)
    value = 'Ślusarczyk'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def click_submit_form(driver_instance):
    wait_for_visibility_of_element(driver_instance, submit)
    elem = driver_instance.find_element_by_id(submit)
    elem.click()
    sleep(5)
    alert = driver_instance.switch_to.alert
    alert.accept()




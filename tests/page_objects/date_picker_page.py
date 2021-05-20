from tests.helpers.support_functions import *
from time import sleep

datepicker_tab = 'datepicker-header'
datepicker_content = 'datepicker-content'
datepicker_field = 'start'

def click_datepicker_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_tab)
    elem = driver_instance.find_element_by_id(datepicker_tab)
    elem.click()
    sleep(3)

def datepicker_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, datepicker_content)
    return elem.is_displayed()


def datepicker_send_correct_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_field, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_field)
    elem.send_keys('2020-10-20')
    value='2020-10-20'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def datepicker_send_incorrect_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_field, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_field)
    elem.send_keys('abcde')
    value = 'abcde'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True

def datepicker_send_outofscope_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_field, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_field)
    elem.send_keys('20102021')
    value = '2021-10-20'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True




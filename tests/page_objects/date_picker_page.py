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


def choose_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_field)
    elem = driver_instance.find_element_by_id(datepicker_field)
    elem.click()





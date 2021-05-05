from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from time import sleep

dropdwon_tab = 'dropdownlist-header'
dropdwon_content = 'dropdownlist-content'
dropdwon_list = 'dropdown'

def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element_by_id(dropdwon_tab)
    elem.click()


def dropdwon_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, dropdwon_content)
    return elem.is_displayed()

def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(dropdwon_list))
    wait_for_visibility_of_element(driver_instance, dropdwon_list, time_to_wait=1)
    elem_list.select_by_index(1)
    sleep(3)

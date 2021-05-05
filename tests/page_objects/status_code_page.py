from tests.helpers.support_functions import *
from time import sleep

status_tab = 'statuscodes-header'
status_content = 'statuscodes-content'
status_200 = '//*[@id="200siteAnchor"]'
status_305 = '//*[@id="305siteAnchor"]'
status_404 = '//*[@id="404siteAnchor"]'
status_500 = '//*[@id="500siteAnchor"]'


def click_staus_code_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_tab)
    elem = driver_instance.find_element_by_id(status_tab)
    elem.click()


def status_code_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_content)
    elem = driver_instance.find_element_by_id(status_content)
    return elem.is_displayed()
    sleep(3)


def status_code200(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_content)
    hover_over_element(driver_instance, status_200)
    elem = driver_instance.find_element_by_xpath(status_200)
    elem.click()
    sleep(3)


def status_code305(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_content)
    hover_over_element(driver_instance, status_305)
    elem = driver_instance.find_element_by_xpath(status_305)
    elem.click()
    sleep(3)


def status_code404(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_content)
    hover_over_element(driver_instance, status_404)
    elem = driver_instance.find_element_by_xpath(status_404)
    elem.click()
    sleep(3)


def status_code500(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_content)
    hover_over_element(driver_instance, status_500)
    elem = driver_instance.find_element_by_xpath(status_500)
    elem.click()
    sleep(3)
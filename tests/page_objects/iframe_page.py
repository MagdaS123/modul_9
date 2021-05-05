from tests.helpers.support_functions import *
from time import sleep

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
iframe = '//*[@id="iframe-content"]/div/div/iframe'
button1 = '//*[@id="simpleButton1"]'
button2 = '//*[@id="simpleButton2"]'


def click_iframe_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_tab)
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()
    sleep(3)


def iframe_content_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_content)
    elem = driver_instance.find_element_by_id(iframe_content)
    return elem.is_displayed()


def click_button1(driver_instance):
    elem1 = driver_instance.find_element_by_xpath(iframe)
    driver_instance.switch_to.frame(elem1)
    hover_over_element(driver_instance, button1)
    elem2 = driver_instance.find_element_by_xpath(button1)
    elem2.click()
    driver_instance.switch_to.default_content()
    sleep(3)


def click_button2(driver_instance):
    elem1 = driver_instance.find_element_by_xpath(iframe)
    driver_instance.switch_to.frame(elem1)
    hover_over_element(driver_instance, button2)
    elem2 = driver_instance.find_element_by_xpath(button2)
    elem2.click()
    driver_instance.switch_to.default_content()
    sleep(3)
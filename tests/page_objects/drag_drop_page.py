from tests.helpers.support_functions import *
from time import sleep

dragdrop_tab = 'draganddrop-header'
dragdrop_content = 'draganddrop-content'
column_a = 'column-a'
column_b = 'column-b'


def click_dragdrop_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, dragdrop_tab)
    elem = driver_instance.find_element_by_id(dragdrop_tab)
    elem.click()


def dragdrop_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, dragdrop_content)
    return elem.is_displayed()


def draganddrop(driver_instance):
    action = ActionChains(driver_instance)
    source_element = driver_instance.find_element_by_id(column_a)
    target_element = driver_instance.find_element_by_id(column_b)
    action.drag_and_drop(source_element, target_element)
    #action.click_and_hold(source_element).move_to_element(target_element)
    action.perform()
    sleep(3)

    assert "B" in target_element.text
    print(target_element.text)


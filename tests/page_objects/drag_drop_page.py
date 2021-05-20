from tests.helpers.support_functions import *
from time import sleep
import os.path

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

def check_drag_and_drop(driver_instance):
    driver_instance.implicitly_wait(10)
    driver_instance.get('http://simpletestsite.fabrykatestow.pl/')

    path = os.path.abspath('drag_and_drop_helper.js')
    with open(path, 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    sleep(10)
    return True

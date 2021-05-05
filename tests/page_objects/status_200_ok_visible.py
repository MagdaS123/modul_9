from tests.helpers.support_functions import *

status = '/html/body/pre'


def status200_ok(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, status)
    return elem.is_displayed()
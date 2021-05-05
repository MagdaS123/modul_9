import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, add_remove_page, date_picker_page, basic_auth_page, form_page, key_presses_page, drag_drop_page, status_code_page, status_200_ok_visible, status_305_visible, status_404_visible, status_500_visible, iframe_page

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hover(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_elemnt_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_corret_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdwon_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_datepicker(self):
        date_picker_page.click_datepicker_visible(self.driver)
        self.assertTrue(date_picker_page.datepicker_content_displayed(self.driver))
        date_picker_page.choose_date(self.driver)


    def test11_basic_auth(self):
        basic_auth_page.click_basic_auth_visible(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_displayed(self.driver))
        self.assertTrue(basic_auth_page.send_corret_keys_to_username(self.driver))
        self.assertTrue(basic_auth_page.send_corret_keys_to_password(self.driver))
        basic_auth_page.hover_and_click_button(self.driver)
        basic_auth_page.hover_and_click_button_return(self.driver)


    # def test12_basic_auth_username(self):
    #     basic_auth_page.click_basic_auth_visible(self.driver)
    #     self.assertTrue(basic_auth_page.send_corret_keys_to_username(self.driver))
    #
    #
    # def test13_basic_auth_password(self):
    #     basic_auth_page.click_basic_auth_visible(self.driver)
    #     self.assertTrue(basic_auth_page.send_corret_keys_to_password(self.driver))
    #
    #
    # def test14_basic_auth_button(self):
    #     basic_auth_page.click_basic_auth_visible(self.driver)
    #     basic_auth_page.hover_and_click_button(self.driver)


    # def test15_form(self):
    #     form_page.click_form_tab(self.driver)
    #     self.assertTrue(form_page.form_tab_visible(self.driver))
    #
    #
    # def test16_form_first_name(self):
    #     form_page.click_form_tab(self.driver)
    #     self.assertTrue(form_page.send_corret_keys_to_first_name(self.driver))
    #
    # def test17_form_last_name(self):
    #     form_page.click_form_tab(self.driver)
    #     self.assertTrue(form_page.send_corret_keys_to_last_name(self.driver))
    #
    #
    # def test18_submit_form(self):
    #     form_page.click_form_tab(self.driver)
    #     self.assertTrue(form_page.click_submit_form(self.driver))


    def test12_test_form(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.send_corret_keys_to_first_name(self.driver))
        self.assertTrue(form_page.send_corret_keys_to_last_name(self.driver))
        form_page.click_submit_form(self.driver)


    def test13_key_presses(self):
        key_presses_page.click_key_tab(self.driver)
        self.assertTrue(key_presses_page.key_content_visible(self.driver))
        key_presses_page.click_key_field(self.driver)


    def test14_dragdrop(self):
        drag_drop_page.click_dragdrop_tab(self.driver)
        self.assertTrue(drag_drop_page.dragdrop_visible(self.driver))
        drag_drop_page.draganddrop(self.driver)


    def test15_stauscode_200(self):
        status_code_page.click_staus_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_visible(self.driver))
        status_code_page.status_code200(self.driver)
        self.assertTrue(status_200_ok_visible.status200_ok(self.driver))


    def test16_statuscode_305(self):
        status_code_page.click_staus_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_visible(self.driver))
        status_code_page.status_code305(self.driver)
        self.assertTrue(status_305_visible.status305_proxy(self.driver))


    def test17_statuscode_404(self):
        status_code_page.click_staus_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_visible(self.driver))
        status_code_page.status_code404(self.driver)
        self.assertTrue(status_404_visible.status404(self.driver))


    def test18_statuscode_500(self):
        status_code_page.click_staus_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_visible(self.driver))
        status_code_page.status_code500(self.driver)
        self.assertTrue(status_500_visible.status500(self.driver))


    def test19_iframe(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))
        iframe_page.click_button1(self.driver)
        iframe_page.click_button2(self.driver)

if __name__ == '__main__':
    unittest.main()










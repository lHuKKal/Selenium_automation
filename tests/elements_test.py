import time
import pytest
from pages.base_page import BasePage
from pages.element_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()  # test test
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_per_adr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name don't match"
            assert email == output_email, "the email don't match"
            assert current_address == output_current_address, "the current address don't match"
            assert permanent_address == output_per_adr, "the permanent address don't match"

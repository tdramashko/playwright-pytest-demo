import pytest
from playwright.sync_api import Page, expect
from pages.buttons_page import ButtonsPage


class TestButtons:
    """Tests for DemoQA Buttons page."""

    def test_double_click(self, page: Page):
        """Test double click button functionality."""
        buttons_page = ButtonsPage(page)
        buttons_page.navigate()
        
        buttons_page.double_click()
        
        message = buttons_page.get_double_click_message()
        assert "You have done a double click" in message

    def test_right_click(self, page: Page):
        """Test right click button functionality."""
        buttons_page = ButtonsPage(page)
        buttons_page.navigate()
        
        buttons_page.right_click()
        
        message = buttons_page.get_right_click_message()
        assert "You have done a right click" in message

    def test_single_click(self, page: Page):
        """Test single click button functionality."""
        buttons_page = ButtonsPage(page)
        buttons_page.navigate()
        
        buttons_page.single_click()
        
        message = buttons_page.get_dynamic_click_message()
        assert "You have done a dynamic click" in message

    def test_all_button_types(self, page: Page):
        """Test all three button types in sequence."""
        buttons_page = ButtonsPage(page)
        buttons_page.navigate()
        
        # Double click
        buttons_page.double_click()
        expect(buttons_page.double_click_message).to_be_visible()
        
        # Right click
        buttons_page.right_click()
        expect(buttons_page.right_click_message).to_be_visible()
        
        # Single click
        buttons_page.single_click()
        expect(buttons_page.dynamic_click_message).to_be_visible()

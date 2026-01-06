import pytest
from playwright.sync_api import Page, expect
from pages.text_box_page import TextBoxPage


class TestTextBox:
    """Tests for DemoQA Text Box page."""

    def test_fill_and_submit_form(self, page: Page):
        """Test filling out and submitting the text box form."""
        text_box_page = TextBoxPage(page)
        text_box_page.navigate()
        
        # Fill form
        text_box_page.fill_form(
            full_name="John Doe",
            email="john.doe@example.com",
            current_address="123 Main Street, City",
            permanent_address="456 Oak Avenue, Town"
        )
        
        # Submit and verify
        text_box_page.submit()
        output_text = text_box_page.get_output_text()
        
        assert "John Doe" in output_text
        assert "john.doe@example.com" in output_text
        assert "123 Main Street, City" in output_text
        assert "456 Oak Avenue, Town" in output_text

    def test_output_section_visibility(self, page: Page):
        """Test that output section appears after form submission."""
        text_box_page = TextBoxPage(page)
        text_box_page.navigate()
        
        # Output should not be visible initially
        expect(text_box_page.output_section).not_to_be_visible()
        
        # Fill and submit
        text_box_page.fill_form(
            full_name="Jane Smith",
            email="jane@test.com",
            current_address="789 Test St",
            permanent_address="321 Demo Ave"
        )
        text_box_page.submit()
        
        # Output should be visible after submission
        expect(text_box_page.output_section).to_be_visible()

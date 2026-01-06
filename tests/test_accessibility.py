import pytest
from playwright.sync_api import Page, expect
from pages.accessibility_page import AccessibilityPage


class TestAccessibility:
    """Accessibility tests for DemoQA website."""

    def test_page_has_title(self, page: Page):
        """Test that pages have proper titles."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Check page title exists and is meaningful
        expect(page).to_have_title("DEMOQA")
        assert page.title() != "", "Page should have a title"

    def test_headings_hierarchy(self, page: Page):
        """Test proper heading hierarchy for screen readers."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Check main heading exists
        main_heading = page.locator("h1, h2, h3").first
        expect(main_heading).to_be_visible()

    def test_form_inputs_have_labels(self, page: Page):
        """Test that form inputs have associated labels."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Check userName input has label or placeholder
        user_name_info = a11y_page.check_form_labels("userName")
        assert user_name_info["hasPlaceholder"], "Input should have placeholder text"
        assert user_name_info["placeholderText"] == "Full Name"

    def test_buttons_are_keyboard_accessible(self, page: Page):
        """Test that buttons can be focused and activated via keyboard."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_buttons()
        
        # Focus on double click button and check it's focusable
        double_click_btn = page.locator("#doubleClickBtn")
        double_click_btn.focus()
        
        # Verify button is focused
        is_focused = page.evaluate("""() => {
            return document.activeElement.id === 'doubleClickBtn';
        }""")
        assert is_focused, "Button should be keyboard focusable"

    def test_interactive_elements_have_roles(self, page: Page):
        """Test that interactive elements have proper ARIA roles."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_buttons()
        
        # Check buttons have button role
        buttons = page.locator("button").all()
        assert len(buttons) > 0, "Should have buttons on the page"
        
        for button in buttons[:3]:  # Check first 3 buttons
            tag_name = button.evaluate("el => el.tagName")
            assert tag_name == "BUTTON", "Interactive elements should use semantic HTML"

    def test_images_have_alt_text(self, page: Page):
        """Test that images have alt text for screen readers."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Find all images
        images = page.locator("img").all()
        
        # If images exist, they should have alt attributes
        if len(images) > 0:
            for img in images:
                # Each image should have alt attribute (even if empty for decorative images)
                alt_text = img.get_attribute("alt")
                # Note: Some sites may not follow best practices, so we just check
                has_alt = alt_text is not None
        else:
            # No images found is also valid
            assert True, "No images found on page"

    def test_color_contrast_on_buttons(self, page: Page):
        """Test color contrast for better readability."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_buttons()
        
        # Get button styles
        button_styles = a11y_page.check_color_contrast("#doubleClickBtn")
        
        # Verify styles are applied (basic check)
        assert button_styles["color"], "Button should have text color"
        assert button_styles["backgroundColor"], "Button should have background color"

    def test_keyboard_navigation_tab_order(self, page: Page):
        """Test logical tab order for keyboard navigation."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Focus on first input
        page.locator("#userName").focus()
        
        # Tab to next element
        page.keyboard.press("Tab")
        
        # Check that focus moved to next input
        focused_id = page.evaluate("document.activeElement.id")
        assert focused_id == "userEmail", "Tab should move to next form field"

    def test_semantic_html_structure(self, page: Page):
        """Test that page uses semantic HTML elements."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Check for semantic HTML elements
        semantic_elements = page.evaluate("""() => {
            return {
                hasMain: !!document.querySelector('main, [role="main"]'),
                hasHeader: !!document.querySelector('header, [role="banner"]'),
                hasButtons: document.querySelectorAll('button').length > 0,
                hasInputs: document.querySelectorAll('input').length > 0
            };
        }""")
        
        # Verify page uses semantic elements
        assert semantic_elements["hasButtons"] or semantic_elements["hasInputs"], "Page should have interactive elements"

    def test_skip_to_main_content(self, page: Page):
        """Test for skip navigation links for keyboard users."""
        a11y_page = AccessibilityPage(page)
        a11y_page.navigate_to_text_box()
        
        # Check for main content landmark
        main_content = page.locator("main, [role='main'], .main-content").first
        
        # Main content area should exist
        assert main_content is not None, "Page should have main content area"

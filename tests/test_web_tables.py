import pytest
from playwright.sync_api import Page, expect
from pages.web_tables_page import WebTablesPage


class TestWebTables:
    """Tests for DemoQA Web Tables page."""

    def test_add_new_record(self, page: Page):
        """Test adding a new record to the table."""
        tables_page = WebTablesPage(page)
        tables_page.navigate()
        
        # Get initial row count
        initial_count = tables_page.get_table_row_count()
        
        # Add new record
        tables_page.click_add_button()
        tables_page.fill_registration_form(
            first_name="Alice",
            last_name="Johnson",
            email="alice@example.com",
            age="30",
            salary="50000",
            department="Engineering"
        )
        tables_page.submit_form()
        
        # Verify row count increased
        new_count = tables_page.get_table_row_count()
        assert new_count == initial_count + 1

    def test_search_functionality(self, page: Page):
        """Test the search box functionality."""
        tables_page = WebTablesPage(page)
        tables_page.navigate()
        
        # Search for existing record
        tables_page.search("Cierra")
        
        # Verify table content
        table_text = tables_page.table.text_content()
        assert "Cierra" in table_text

    def test_search_no_results(self, page: Page):
        """Test search with no matching results."""
        tables_page = WebTablesPage(page)
        tables_page.navigate()
        
        # Search for non-existent record
        tables_page.search("NonExistentName123")
        
        # Verify no data rows are visible
        visible_rows = 0
        for row in tables_page.table_rows.all():
            if row.text_content().strip() and "NonExistentName123" not in row.text_content():
                visible_rows += 1
        
        # Should have minimal or no visible content rows
        assert visible_rows <= 1

import pytest
from playwright.sync_api import Page, BrowserContext


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context settings."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(page: Page, request):
    """Take screenshot on test failure."""
    yield
    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")


def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot fixture."""
    if call.when == "call":
        item.rep_call = call

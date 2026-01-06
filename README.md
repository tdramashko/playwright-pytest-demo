# DemoQA Playwright Test Automation

A simple Playwright pytest project demonstrating automated UI testing on [demoqa.com](https://demoqa.com/).

## Features

- **Page Object Model** design pattern for maintainable test code
- **pytest** framework with Playwright integration
- **Automated screenshot capture** on test failures
- **HTML test reports** for easy result analysis

## Test Scenarios

### Text Box (`test_text_box.py`)
- Form filling and submission
- Output validation
- Element visibility checks

### Buttons (`test_buttons.py`)
- Double-click interactions
- Right-click (context menu) interactions
- Single-click events
- Multiple button types in sequence

### Web Tables (`test_web_tables.py`)
- Adding new table records
- Search functionality
- Table data validation

## Project Structure

```
Python-demo/
├── tests/
│   ├── test_text_box.py      # Text box form tests
│   ├── test_buttons.py        # Button interaction tests
│   └── test_web_tables.py     # Web table CRUD tests
├── pages/
│   ├── text_box_page.py       # Text box page object
│   ├── buttons_page.py        # Buttons page object
│   └── web_tables_page.py     # Web tables page object
├── conftest.py                # pytest configuration & fixtures
├── pytest.ini                 # pytest settings
└── requirements.txt           # Project dependencies
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## Running Tests

**Run all tests (headed mode with slow motion):**
```bash
pytest
```

**Run specific test file:**
```bash
pytest tests/test_buttons.py
```

**Run in headless mode:**
```bash
pytest --headless
```

**Generate HTML report:**
```bash
pytest --html=report.html --self-contained-html
```

**Run with different browser:**
```bash
pytest --browser firefox
pytest --browser webkit
```

## Configuration

Default settings in `pytest.ini`:
- Base URL: `https://demoqa.com`
- Browser: Chromium (headed mode)
- Slow motion: 500ms (easier to observe test execution)

Modify these settings via command line or update `pytest.ini`.

## Requirements

- Python 3.8+
- pytest 8.3.4+
- playwright 1.49.1+
- pytest-playwright 0.6.2+

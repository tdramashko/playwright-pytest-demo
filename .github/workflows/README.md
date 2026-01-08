# GitHub Actions Workflows

This directory contains CI/CD workflows for automated testing and code quality checks.

## Workflows

### 1. Playwright Tests (`playwright-tests.yml`)
**Trigger**: Push to main/develop/feature branches, Pull Requests, Manual dispatch

**What it does**:
- Runs tests across all three browsers (Chromium, Firefox, WebKit) in parallel
- Uses native Playwright installation (faster for CI)
- Generates HTML reports for each browser
- Uploads test reports and screenshots as artifacts
- Fails fast on test failures

**Artifacts**:
- `test-report-{browser}` - HTML reports (kept 30 days)
- `screenshots-{browser}` - Failure screenshots (kept 30 days)

### 2. Docker Tests (`docker-tests.yml`)
**Trigger**: Push to main/develop, Pull Requests, Manual dispatch

**What it does**:
- Builds the Docker image
- Runs all tests inside Docker container
- Validates Docker setup works correctly
- Uploads test results and screenshots

**Artifacts**:
- `docker-test-report` - HTML report (kept 30 days)
- `docker-screenshots` - Failure screenshots (kept 30 days)

### 3. Code Quality (`lint.yml`)
**Trigger**: Push to main/develop/feature branches, Pull Requests

**What it does**:
- Checks code formatting with Black
- Checks import sorting with isort
- Lints code with Flake8
- Enforces basic Python code quality standards

**Note**: Formatting checks are non-blocking (continue-on-error) but provide warnings

## Viewing Results

### In GitHub UI:
1. Go to **Actions** tab in your repository
2. Click on a workflow run to see results
3. Download artifacts from the **Artifacts** section at the bottom

### Status Badges:
Add these to your README.md to show build status:

```markdown
![Playwright Tests](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/playwright-tests.yml/badge.svg)
![Docker Tests](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/docker-tests.yml/badge.svg)
![Code Quality](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/lint.yml/badge.svg)
```

## Manual Workflow Dispatch

Both test workflows support manual triggering:
1. Go to **Actions** tab
2. Select the workflow
3. Click **Run workflow**
4. Choose the branch and click **Run workflow**

## Configuration

### Matrix Testing
The Playwright workflow uses matrix strategy to test across browsers:
- Chromium
- Firefox  
- WebKit

### Caching
- Python dependencies are cached using `cache: 'pip'`
- Docker layers are cached with Buildx

## Customization

### Run specific tests:
Edit the test command in the workflow file:
```yaml
run: pytest tests/test_text_box.py --browser=${{ matrix.browser }}
```

### Change Python version:
Update the `python-version` in setup-python step:
```yaml
python-version: '3.12'
```

### Adjust artifact retention:
Change `retention-days` value (default: 30 days)

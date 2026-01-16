# Linux Setup Instructions for Kiosk Automation

## Prerequisites

- Python 3.8 or higher
- pip and venv
- Linux distribution (Ubuntu, Debian, Fedora, etc.)

## Initial Setup

### 1. Clone and Navigate to Project

```bash
git clone <repository-url>
cd KioskAutomation
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install WebDriver Manager (Automatic)

The project uses `webdriver-manager` which automatically downloads the correct WebDriver versions for your system. This handles ChromeDriver, GeckoDriver (Firefox), and EdgeDriver automatically.

## WebDriver Setup

### Option 1: Automatic Setup (Recommended)

The `webdriver-manager` package handles automatic downloading and setup. No manual intervention needed!

### Option 2: Manual WebDriver Installation

If you prefer manual setup, download drivers from:

- **ChromeDriver:** https://googlechromelabs.github.io/chrome-for-testing/ or https://chromedriver.chromium.org/
- **GeckoDriver (Firefox):** https://github.com/mozilla/geckodriver/releases
- **EdgeDriver:** https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

#### Installation Steps:

1. **Download the driver for Linux (x64)**
2. **Extract and place in `drivers/` folder:**
   ```bash
   mkdir -p drivers/
   # For ChromeDriver
   mv chromedriver drivers/
   chmod +x drivers/chromedriver
   
   # For GeckoDriver
   mv geckodriver drivers/
   chmod +x drivers/geckodriver
   
   # For EdgeDriver
   mv msedgedriver drivers/
   chmod +x drivers/msedgedriver
   ```

3. **Make scripts executable:**
   ```bash
   chmod +x drivers/chromedriver
   chmod +x drivers/geckodriver
   chmod +x drivers/msedgedriver
   ```

## Running Tests

### Make Scripts Executable

```bash
chmod +x test.sh run_tests.sh
```

### Run Tests on Specific Browser

```bash
./test.sh chrome
./test.sh firefox
./test.sh edge
./test.sh all
```

### Run Tests on All Browsers with Report

```bash
./run_tests.sh
```

### Run Tests Manually with pytest

```bash
# Single browser
pytest --alluredir=reports/allure tests/ -v -m "chrome"

# All browsers
pytest --alluredir=reports/allure tests/ -v

# Generate and serve Allure report
allure generate reports/allure --clean
allure serve reports/allure
```

## System Requirements for Different Distributions

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv google-chrome-stable firefox
```

### Fedora

```bash
sudo dnf install -y python3-pip google-chrome-stable firefox
```

### Arch Linux

```bash
sudo pacman -S python-pip google-chrome firefox
```

## Troubleshooting

### WebDriver Issues

If you encounter WebDriver issues, try clearing the cache and letting webdriver-manager re-download:

```bash
rm -rf ~/.wdm  # Clear WebDriver Manager cache
pytest --alluredir=reports/allure tests/ -v
```

### Permission Denied on Scripts

Make sure scripts are executable:

```bash
chmod +x test.sh run_tests.sh
```

### Chrome/Firefox Not Found

Install the browsers:

```bash
# Ubuntu/Debian
sudo apt install -y google-chrome-stable firefox

# Or use Snap
sudo snap install chromium
sudo snap install firefox
```

### Selenium Compatibility Issues

Ensure your browser versions match the WebDriver versions. webdriver-manager should handle this automatically, but you can force an update:

```bash
pip install --upgrade webdriver-manager
```

## Virtual Environment Management

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### List Installed Packages

```bash
pip list
```

## Notes

- All Python test files are platform-agnostic and work on Linux without modification
- The `webdriver-manager` automatically detects your OS and downloads appropriate drivers
- Reports are generated in `reports/allure/` directory
- Allure report HTML is generated in `allure-report/` directory

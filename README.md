# Kiosk Automation Testing

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.39.0-green.svg)](https://www.selenium.dev/)

Multi-browser automated testing for visitor check-in kiosk systems using Selenium WebDriver.

## 🎯 What This Project Does

Tests the complete visitor registration workflow across Chrome, Firefox, and Edge browsers:
- Homepage → Check-in → Visitor Type → Contact Info → Host Selection → Document Upload
- Automatic screenshots and video recording
- Comprehensive Allure reporting

## 🚀 Quick Start

### Install
```bash
git clone https://github.com/abdul-rafay8900/Kiosk_Automation.git
cd Kiosk_Automation
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Run Tests
```powershell
# All browsers
.\test.ps1 all

# Specific browser
.\test.ps1 chrome   # Chrome only
.\test.ps1 firefox  # Firefox only
.\test.ps1 edge     # Edge only
```

## 📁 Structure

```
├── test_runner.py     # Python test runner
├── test.ps1          # PowerShell test runner
├── tests/test_Home.py # Visitor check-in tests
├── pages/Home_page.py # Page objects
├── reports/          # Test reports & screenshots
└── commands.txt      # All commands reference
```

## 🛠️ Browsers

| Browser | Setup | Status |
|---------|-------|--------|
| Chrome  | Auto | ✅ Ready |
| Firefox | Auto | ✅ Ready |
| Edge    | Manual* | ✅ Ready |

*Download Edge WebDriver to `drivers/` folder

## 📊 Reports

### Allure (Recommended)
```bash
allure generate reports/allure --clean
allure serve reports/allure
```

### HTML
```bash
pytest --html=reports/report.html --self-contained-html -v
```

**Note**: Test runners automatically clean reports, run tests, and serve Allure reports.

## 🔧 Tech Stack

- **Python 3.11+** - Core language
- **Selenium 4.39.0** - Browser automation
- **pytest 9.0.2** - Test framework
- **Allure 2.36.0** - Test reporting
- **OpenCV + MSS** - Screen recording

## 📋 Commands

See `commands.txt` for complete command reference.

## 🔧 Troubleshooting

### Edge Issues
Download WebDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Extract to `drivers/msedgedriver.exe`

### Virtual Environment
```bash
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # macOS/Linux
```

## 📈 CI/CD

```yaml
- name: Run tests
  run: python test_runner.py all
- name: Generate reports
  run: allure generate reports/allure --clean
```

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Add tests for new features
4. Run: `python test_runner.py all`
5. Create Pull Request

---

**Built for reliable kiosk system testing** 🧪

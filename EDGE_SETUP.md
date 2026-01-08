# Edge WebDriver Setup Instructions

## Manual Installation (Required due to network restrictions)

1. **Download Edge WebDriver:**
   - Go to: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Download the version that matches your Edge browser version
   - For Windows, download the .zip file

2. **Extract the WebDriver:**
   - Extract `msedgedriver.exe` from the downloaded zip
   - Place it in the `drivers/` folder in your project root
   - Final path should be: `C:\Users\AbdulRafay\PycharmProjects\KioskAutomation\drivers\msedgedriver.exe`

3. **Run Tests:**
   - Once the WebDriver is in place, run: `pytest --alluredir=reports/allure tests/ -v`

## Alternative: Use Chrome and Firefox Only

If Edge setup is problematic, you can continue with Chrome and Firefox only by updating conftest.py:

```python
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param
```
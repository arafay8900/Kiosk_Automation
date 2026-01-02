# run_tests.ps1
# Script to run tests with Allure reporting, clearing previous data

# Activate virtual environment
. "$PSScriptRoot\.venv\Scripts\Activate.ps1"

# Clear previous reports and data
Remove-Item -Recurse -Force reports/allure -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force allure-report -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force reports/screenshots -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force reports/videos -ErrorAction SilentlyContinue

# Run tests and generate Allure report
pytest --alluredir=reports/allure tests/
if ($LASTEXITCODE -eq 0) {
    allure generate reports/allure --clean
    # Open the report in browser
    Start-Process -FilePath "cmd" -ArgumentList "/c", "allure serve reports/allure"
}
#!/bin/bash

# run_tests.sh
# Script to run tests with Allure reporting, clearing previous data

# Activate virtual environment
source ./.venv/bin/activate

# Clear previous reports and data
rm -rf reports/allure
rm -rf allure-report
rm -rf reports/screenshots
rm -rf reports/videos

# Run tests and generate Allure report
echo "Running tests on multiple browsers: Chrome, Firefox, and Edge..."
pytest --alluredir=reports/allure tests/ -v
if [ $? -eq 0 ]; then
    allure generate reports/allure --clean
    # Open the report in browser
    allure serve reports/allure
fi

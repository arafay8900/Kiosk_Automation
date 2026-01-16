#!/bin/bash

# Kiosk Automation Test Runner
# Usage: ./test.sh [all|chrome|firefox|edge]

if [ $# -eq 0 ]; then
    echo "Usage: ./test.sh [all|chrome|firefox|edge]"
    exit 1
fi

BROWSER=$1

# Validate browser argument
if [[ ! "$BROWSER" =~ ^(all|chrome|firefox|edge)$ ]]; then
    echo "Invalid browser: $BROWSER"
    echo "Valid options: all, chrome, firefox, edge"
    exit 1
fi

VENV_PATH="./.venv/bin/python"

echo "🧪 Running Kiosk Automation Tests on $BROWSER..."

# Clean previous reports BEFORE running tests
echo "🧹 Cleaning previous reports..."
DIRS_TO_CLEAN=("reports/allure" "allure-report" "reports/screenshots" "reports/videos")
for dir in "${DIRS_TO_CLEAN[@]}"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
        echo "   ✅ Cleaned: $dir"
    fi
done

# Run the test using the virtual environment Python
$VENV_PATH test_runner.py $BROWSER

if [ $? -eq 0 ]; then
    echo "✅ Tests completed successfully!"
    echo "📊 Generating Allure report..."

    # Generate Allure report
    allure generate reports/allure --clean
    if [ $? -eq 0 ]; then
        echo "✅ Report generated successfully!"
        echo "🌐 Serving Allure report..."
        echo "   📱 Report will open in your default browser"
        echo "   🔄 Press Ctrl+C to stop the server"
        allure serve reports/allure
    else
        echo "❌ Failed to generate report!"
        exit 1
    fi
else
    echo "❌ Tests failed!"
    exit 1
fi

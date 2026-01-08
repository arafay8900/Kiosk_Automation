# Kiosk Automation Test Runner
# Usage: .\test.ps1 [all|chrome|firefox|edge]

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("all", "chrome", "firefox", "edge")]
    [string]$Browser
)

$venvPath = ".\.venv\Scripts\python.exe"

Write-Host "🧪 Running Kiosk Automation Tests on $Browser..." -ForegroundColor Green

# Clean previous reports BEFORE running tests
Write-Host "🧹 Cleaning previous reports..." -ForegroundColor Yellow
$dirsToClean = @("reports/allure", "allure-report", "reports/screenshots", "reports/videos")
foreach ($dir in $dirsToClean) {
    if (Test-Path $dir) {
        Remove-Item -Recurse -Force $dir -ErrorAction SilentlyContinue
        Write-Host "   ✅ Cleaned: $dir" -ForegroundColor Green
    }
}

# Run the test using the virtual environment Python
$arguments = @("test_runner.py", $Browser)
& $venvPath $arguments

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Tests completed successfully!" -ForegroundColor Green
    Write-Host "📊 Generating Allure report..." -ForegroundColor Cyan

    # Generate Allure report
    & allure generate reports/allure --clean
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Report generated successfully!" -ForegroundColor Green
        Write-Host "🌐 Serving Allure report..." -ForegroundColor Cyan
        Write-Host "   📱 Report will open in your default browser" -ForegroundColor White
        Write-Host "   🔄 Press Ctrl+C to stop the server" -ForegroundColor White
        try {
            & allure serve reports/allure
        } catch {
            Write-Host "🛑 Allure server stopped" -ForegroundColor Yellow
        }
    } else {
        Write-Host "❌ Failed to generate report!" -ForegroundColor Red
    }
} else {
    Write-Host "❌ Tests failed!" -ForegroundColor Red
    exit $LASTEXITCODE
}
#!/usr/bin/env python3
"""
Kiosk Automation Test Runner
Simple commands for multi-browser testing

Usage: python test_runner.py [chrome|firefox|edge|all]
"""

import sys
import subprocess
import os
import shutil

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))


def resolve_python_executable():
    """Use local repo virtualenv Python, fallback to current interpreter."""
    local_venv_python = os.path.join(REPO_ROOT, ".venv", "Scripts", "python.exe")
    if os.path.exists(local_venv_python):
        return local_venv_python
    return sys.executable

def cleanup_reports():
    """Clean previous test reports and data."""
    print("🧹 Cleaning previous reports...")
    dirs_to_clean = [
        "reports/allure",
        "allure-report",
        "reports/screenshots",
        "reports/videos"
    ]

    for dir_path in dirs_to_clean:
        if os.path.exists(dir_path):
            try:
                shutil.rmtree(dir_path)
                print(f"   ✅ Cleaned: {dir_path}")
            except Exception as e:
                print(f"   ⚠️  Could not clean {dir_path}: {e}")

def generate_allure_report():
    """Generate Allure report from test results."""
    print("📊 Generating Allure report...")
    cmd = "allure generate reports/allure --clean"
    result = subprocess.call(cmd, shell=True)
    if result == 0:
        print("✅ Report generated successfully!")
    else:
        print("❌ Failed to generate report!")
    return result

def serve_allure_report():
    """Serve Allure report in browser."""
    print("🌐 Serving Allure report...")
    print("   📱 Report will open in your default browser")
    print("   🔄 Press Ctrl+C to stop the server")
    cmd = "allure serve reports/allure"
    try:
        subprocess.call(cmd, shell=True)
    except KeyboardInterrupt:
        print("\n🛑 Allure server stopped")

def run_test(browser_filter=None):
    """Run tests with optional browser filter."""
    venv_python = resolve_python_executable()

    if browser_filter:
        cmd = [
            venv_python,
            "-m",
            "pytest",
            "--alluredir=reports/allure",
            "tests/",
            "-k",
            browser_filter,
            "-v",
        ]
    else:
        cmd = [
            venv_python,
            "-m",
            "pytest",
            "--alluredir=reports/allure",
            "tests/",
            "-v",
        ]

    print(f"🚀 Running: {' '.join(cmd)}")
    return subprocess.call(cmd)

def main():
    os.chdir(REPO_ROOT)

    if len(sys.argv) != 2:
        print("Kiosk Automation Test Runner")
        print("Usage: python test_runner.py [chrome|firefox|edge|all]")
        print()
        print("Commands:")
        print("  all      - Run all browsers (Chrome + Firefox + Edge)")
        print("  chrome   - Run Chrome only")
        print("  firefox  - Run Firefox only")
        print("  edge     - Run Edge only")
        print()
        print("Examples:")
        print("  python test_runner.py all     # Test everything")
        print("  python test_runner.py chrome  # Quick Chrome test")
        sys.exit(1)

    command = sys.argv[1].lower()

    # Clean previous reports BEFORE running tests
    cleanup_reports()

    if command == "all":
        print("🧪 Testing on ALL browsers...")
        exit_code = run_test()
    elif command in ["chrome", "firefox", "edge"]:
        print(f"🧪 Testing on {command.upper()}...")
        exit_code = run_test(command)
    else:
        print(f"❌ Unknown command: {command}")
        print("Valid commands: all, chrome, firefox, edge")
        sys.exit(1)

    if exit_code == 0:
        print("✅ Tests completed successfully!")
        # Automatically generate and serve report
        if generate_allure_report() == 0:
            serve_allure_report()
    else:
        print("❌ Tests failed!")
        sys.exit(exit_code)

if __name__ == "__main__":
    main()
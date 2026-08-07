from pages.Home_page import HomePage


def test_homepage(driver, browser, logger, screen_recorder):
    """Test the complete visitor check-in flow from home to acknowledgment on {browser}."""
    home = HomePage(driver, logger)

    def step(action, message):
        action()
        logger(message)

    def assert_url(expected_url, message):
        home.wait.until(lambda d: d.current_url == expected_url)
        assert driver.current_url == expected_url, f"Expected {expected_url}, got {driver.current_url}"
        logger(message)

    # Home page
    home.open()
    logger("Opened home page")
    assert_url(home.home_url(), "Asserted homepage URL")

    # Clear browser cache and cookies (browser-specific handling)
    if browser == "chrome":
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
    else:
        driver.delete_all_cookies()
    logger("Cleared browser cache and cookies")

    # Check-in -> visitor type -> num people -> visitor info
    step(home.click_check_in, "Clicked check-in button")
    assert_url(home.visitor_type_url(), "Asserted visitor type URL")

    step(home.click_chose_workflow, "Chose workflow")
    assert_url(home.num_people_url(), "Asserted num people URL")

    step(home.click_next_multiparty, "Clicked next for multiparty")
    assert_url(home.visitor_info_url(), "Asserted visitor info URL")

    # Phone and profile
    home.phone_input()
    home.click_phone_next()
    logger("Entered phone number and proceeded")

    home.chose_profile()
    logger("Chose profile")
    assert_url(home.chose_host_url(), "Asserted choose host URL")

    step(home.click_chose_host, "Clicked choose host")

    # Upload flow
    home.upload_file()
    logger("Uploaded file")
    step(home.click_upload_next, "Clicked upload next")

    for _ in range(2):
        step(home.click_dox_next, "Clicked dox next")

    for _ in range(8):
        step(home.click_pptx_next2, "Clicked agreement next2")

    # Test form
    step(home.click_test_option, "Clicked test option")
    step(home.click_close_image, "Clicked close image")
    step(home.click_test_submit, "Clicked test submit")

    step(home.click_test_option_without, "Clicked test option")
    step(home.click_test_submit, "Clicked test submit")

    # External links
    step(home.click_visit_link, "Clicked visit link")
    step(home.click_visit_link, "Clicked link next")

    step(home.click_test_option_without, "Clicked test option")
    step(home.click_test_submit, "Clicked test submit")

    # Content pages
    step(home.click_test_submit, "Clicked content next")
    for _ in range(6):
        step(home.click_content_next, "Clicked content next")

    # Acknowledgment
    step(home.click_test_option_without, "Clicked acknowledgment option")
    step(home.click_test_submit, "Clicked acknowledgment submit")

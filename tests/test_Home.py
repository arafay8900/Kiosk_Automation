from pages.Home_page import HomePage

def test_homepage(driver, browser, logger, screen_recorder):
    """Test the complete visitor check-in flow from home to upload on {browser}."""
    home = HomePage(driver, logger)
    home = HomePage(driver, logger)

    # Open the home page
    home.open()
    logger("Opened home page")

    # Wait for homepage to load
    home.wait.until(lambda d: d.current_url == home.home_url())

    # Clear browser cache and cookies (browser-specific handling)
    if browser == "chrome":
        # Chrome supports CDP commands
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
    else:
        # For other browsers, just clear cookies (cache clearing is more complex)
        driver.delete_all_cookies()

    logger("Cleared browser cache and cookies")

    # Assert homepage URL
    assert driver.current_url == home.home_url(), f"Expected {home.home_url()}, got {driver.current_url()}"
    logger("Asserted homepage URL")

    # Click check-in button
    home.click_check_in()
    logger("Clicked check-in button")

    # Wait for visitor type page
    home.wait.until(lambda d: d.current_url == home.visitor_type_url())

    # Assert visitor type URL
    assert driver.current_url == home.visitor_type_url(), f"Expected {home.visitor_type_url()}, got {driver.current_url()}"
    logger("Asserted visitor type URL")

    # Choose workflow
    home.click_chose_workflow()
    logger("Chose workflow")

    # Wait for num people page
    home.wait.until(lambda d: d.current_url == home.num_people_url())

    # Assert num people URL
    assert driver.current_url == home.num_people_url(), f"Expected {home.num_people_url()}, got {driver.current_url()}"
    logger("Asserted num people URL")

    # Click next for multiparty
    home.click_next_multiparty()
    logger("Clicked next for multiparty")

    # Wait for visitor info page
    home.wait.until(lambda d: d.current_url == home.visitor_info_url())

    # Assert visitor info URL
    assert driver.current_url == home.visitor_info_url(), f"Expected {home.visitor_info_url()}, got {driver.current_url()}"
    logger("Asserted visitor info URL")

    # Enter phone number and proceed
    home.phone_input()
    home.click_phone_next()
    logger("Entered phone number and proceeded")

    # Choose profile
    home.chose_profile()
    logger("Chose profile")

    # Wait for choose host page
    home.wait.until(lambda d: d.current_url == home.chose_host_url())

    # Assert choose host URL
    assert driver.current_url == home.chose_host_url(), f"Expected {home.chose_host_url()}, got {driver.current_url()}"
    logger("Asserted choose host URL")

    # Click choose host
    home.click_chose_host()
    logger("Clicked choose host")

    # Upload file
    home.upload_file()
    logger("Uploaded file")

    # Click upload next
    home.click_upload_next()
    logger("Clicked upload next")

    # click dox next
    home.click_dox_next()
    logger("Clicked dox next")

    # click dox next
    home.click_dox_next()
    logger("Clicked dox next")

    # click pptx next2
    home.click_pptx_next2()
    logger("Clicked agreement next2")

    # click pptx next2
    home.click_pptx_next2()
    logger("Clicked agreement next2")

    # click pptx next2
    home.click_pptx_next2()
    logger("Clicked agreement next2")

     # click pptx next2
    home.click_pptx_next2()
    logger("Clicked agreement next2")

    # click pptx next2
    home.click_pptx_next2()
    logger("Clicked agreement next2")

     # click image1
    home.click_pptx_next2()
    logger("Clicked agreement next2")

     # click image2
    home.click_pptx_next2()
    logger("Clicked agreement next2")

     # click image3
    home.click_pptx_next2()
    logger("Clicked agreement next2")

    # click external next
    home.click_upload_next()
    logger("Clicked external next")

    # click external next
    home.click_upload_next()
    logger("Clicked external next")

    #click Form option
    home.click_test_option()    
    logger("Clicked test option")

    #click close image
    home.click_close_image()
    logger("Clicked close image")

    #click Form submit
    home.click_test_submit()    
    logger("Clicked test submit")

    #click test option
    home.click_test_option_without()    
    logger("Clicked test option")

    #click test submit
    home.click_test_submit()    
    logger("Clicked test submit")

     # click Emoti next
    home.click_upload_next()
    logger("Clicked external next")

    # click Emoti next
    home.click_upload_next()
    logger("Clicked external next")

    #click test option
    home.click_test_option_without()    
    logger("Clicked test option")

    #click test submit
    home.click_test_submit()    
    logger("Clicked test submit")

    #click Content next
    home.click_test_submit()    
    logger("Clicked content next")

    #click content next
    home.click_content_next()
    logger("Clicked content next")

    #click content next
    home.click_content_next()
    logger("Clicked content next")

    #click content next
    home.click_content_next()
    logger("Clicked content next")

    #click content next
    home.click_content_next()
    logger("Clicked content next")

    #click content next
    home.click_content_next()
    logger("Clicked content next")

    #click content next
    home.click_content_next()
    logger("Clicked content next")

    #click Acknowledgment option
    home.click_test_option_without()    
    logger("Clicked acknowledgment option")

    #click Acknowledgement submit
    home.click_test_submit()    
    logger("Clicked acknowledgment submit")

import time

from pages.Home_page import HomePage

def test_homepage(driver, logger):
    home = HomePage(driver, logger)

    home.open()
    time.sleep(2)

    driver.execute_cdp_cmd('Network.clearBrowserCache', {})
    driver.execute_cdp_cmd('Network.clearBrowserCookies', {})

    # Verify Homepage URL
    if driver.current_url == home.home_url():
        print("✅ HomePage is Loaded:", driver.current_url)
    else:
        print("❌ HomePage is Not Loaded:", driver.current_url)
        assert False, f"URL mismatch! Expected: {home.home_url()}, Found: {driver.current_url}"

    home.click_check_in()
    time.sleep(2)

    # Verify Visitor Type URL
    if driver.current_url == home.visitor_type_url():
        print("✅ Visitor Types are Loaded:", driver.current_url)
    else:
        print("❌ Visitor Types are not Loaded:", driver.current_url)
        assert False, f"URL mismatch! Expected: {home.visitor_type_url()}, Found: {driver.current_url}"

    home.click_chose_workflow()
    time.sleep(2)

    # Verify Multiparty URL
    if driver.current_url == home.num_people_url():
        print("✅ Enter Phone is Loaded:", driver.current_url)
    else:
        print("❌ Enter Phone is not Loaded:", driver.current_url)
        assert False, f"URL mismatch! Expected: {home.num_people_url()}, Found: {driver.current_url}"

    home.click_next_multiparty()
    time.sleep(2)

    # Verify Phone Number URL
    if driver.current_url == home.visitor_info_url():
        print("✅ Visitor info screen is Loaded:", driver.current_url)
    else:
        print("❌ Visitor info screen is not Loaded:", driver.current_url)
        assert False, f"URL mismatch! Expected: {home.visitor_info_url()}, Found: {driver.current_url}"

    home.phone_input()
    home.click_phone_next()

    home.chose_profile()
    time.sleep(30)

    # Verify Chose Host URL
    if driver.current_url == home.chose_host_url():
        print("✅ Profile is Selected and we are on Chose Host Screen:", driver.current_url)
    else:
        print("❌ Profile is not Select:", driver.current_url)
        assert False, f"URL mismatch! Expected: {home.chose_host_url()}, Found: {driver.current_url}"

    home.click_chose_host()

    time.sleep(30)
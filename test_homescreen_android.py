from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Case 1: Verify the list of Ships shows by default when open App with 4 elements on the page, the 4 Ships
def test_list_of_ships_contains_title(driver):

    wait = WebDriverWait(driver, 10)
    assert wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Norwegian Gem"]'))).text == 'Norwegian Gem'
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Norwegian Sky"]').text == 'Norwegian Sky'
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Norwegian Bliss"]').text == 'Norwegian Bliss'
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Norwegian Encore"]').text == 'Norwegian Encore'

# Test Case 2: Verify the ship's card shows the Ship's information
def test_card_ship_contains_description_image(driver):
    
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@index=2]'))).is_displayed()
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@index=1]').is_displayed()
    driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@index=0]').is_displayed()
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@index=1]').text == 'Norwegian Gem'
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@index=2]').text == 'Norwegian Gem has it all. Tons of dining choices and no set dining times; chill out by the pool, get lucky in the casino, unwind at the spa, and make the kids happy with spaces built with them in mind. Accommodations range from the luxurious multi-room or romantic suites to spacious and affordable staterooms.'

#Test Case 3: Verify Ship's details page for Norwegian Gem shows after clicking on the ship's card 
def test_ship_details_screen(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@index=2]'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView[@resource-id="com.ncl.nclcruiseinfo:id/cruiseDetailImageView"]'))).is_displayed()
    driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@resource-id="com.ncl.nclcruiseinfo:id/cruiseDetailImageView"]').is_displayed()
    assert wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Ship Facts"]'))).text == "Ship Facts"

# Test Case 4: Verify Ship's details page information for Norwegian Gem
def test_ship_details_page(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@index=2]'))).click()
    assert wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Ship Facts"]'))).text == "Ship Facts"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Crew"]').text == "Crew"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.ncl.nclcruiseinfo:id/valueLabel"]').text == "1,070"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Cruise Speed"]').text == "Cruise Speed"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="24 knots"]').text == "24 knots"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Draft"]').text == "Draft"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="28.2 feet"]').text == "28.2 feet"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Engines"]').text == "Engines"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Diesel Electric"]').text == "Diesel Electric"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Gross Register Tonnage"]').text == "Gross Register Tonnage"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="93,530"]').text == "93,530"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Inaugural Date"]').text == "Inaugural Date"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="2007"]').text == "2007"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Max Beam"]').text == "Max Beam"
    assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="125 feet"]').text == "125 feet"
# purpose
# automate web applications

# components 
# IDE - record and play
# RC - deprecated
# webdriver - set of web apis for communication between client(programming language) and browser
# grid - parallel on diff browsers and platforms remotely

# architecture
# browser driver - server to interpret json of our code and perform actions on the browser

# xpath formation
# right click on web page -> inspect element -> right click on source code -> copy xpath/selector -> ctrl+f on source code -> enter xpath/css

# installation
# pip install selenium
# pip install ddt

# downloads
# geckodriver (for FF)
# chrome driver
# IE driver

# compatibility checks
# selenium
# browser driver
# browser

# precautions
# IE zoom level and protection enabled/disabled for all zones
# dynamic attribute values

# source code structure
# dom -> html -> head and body -> element tags and attributes
# input tag - type = text/radiobutton inside fieldset/checkbox inside fieldset
# disabled attribute = somevalue - disabled
# fieldset -> select -> option - dropdown
# "style=display:none;" - hidden
# selection tag for calendar
# iframe - page inside page

# best locators
# unique direct attributes like id, name, link_text, class_name
# css
# xpath (reliable)

# css selector
"""
#someid
.someclass
sometag

input#someid
input.someclass

.someclass1.someclass2

sometag1>anyabovecssselector

sometag[someattribute<<blank|^|$|*>>='somevalue']

sometag[someindex]
"""

# xpath
"""
/ - immediate child
// - anywhere ahead child

//sometag

//sometag[@someattribute='somevalue']//furthersimilarpath
//sometag[text()='sometext']//furthersimilarpath

//sometag[contains(@someattribute,'somevalue')]//furthersimilarpath # can use and inside
//sometag[contains(text(),'sometext')] # can use and inside

//sometag[starts-with(@someattribute,'somevalue')]//furthersimilarpath

somexpath//parent::somexpath
somexpath//preceding-sibling::somexpath
somexpath//following-sibling::somexpath

//li[someindex]

[position()=1] for calendar

//iframe
"""

# explicit wait types
# alert_is_present
# element_located_selection_state_to_be
# element_located_to_be_selected
# element_selection_state_to_be
# element_to_be_clickable
# element_to_be_selected
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# presence_of_all_elements_located
# presence_of_element_located
# staleness_of
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# title_contains
# title_is
# visibility_of
# visibility_of_element_located

# code
from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # pass in driver call

binary = FirefoxBinary("browserexepathwith\\")
driver = webdriver.Firefox(executable_path="driverexepathwith\\", firefox_binary=binary)  # or Chrome/Ie  # or set exe path in env vars
driver.get("someurl")
driver.implicitly_wait(10)  # find -> wait -> find -> fail
driver.maximize_window()  # or refresh/back/forward/close/quit
title = driver.title
url = driver.current_url
page_source = driver.page_source
element = driver.find_element_by_id("someid")  # or name/class_name/tag_name/link_text/partial_link_text/xpath/css_selector  # option 1
element = driver.find_element(By.ID, "someid")  # or NAME/CLASS_NAME/TAG_NAME/LINK_TEXT/PARTIAL_LINK_TEXT/XPATH/CSS_SELECTOR  # option 2
elements_list = driver.find_elements_by_id("someid") # or name/class_name/tag_name/link_text/partial_link_text/xpath/css_selector  # option 1
elements_list = driver.find_elements(By.ID, "someid") # or NAME/CLASS_NAME/TAG_NAME/LINK_TEXT/PARTIAL_LINK_TEXT/XPATH/CSS_SELECTOR  # option 2
text = element.text
value = element.get_attribute("class")  # innerText for text
element.send_keys("sometext")
element.click()  # or clear
enabled = element.is_enabled()
selected = element.is_selected()  # checkbox and radiobuttons
displayed = element.is_displayed()
s = Select(element)  # select element
s.select_by_value("somevalue")  # or index or visible_text
wait=WebDriverWait(driver,timeout=10,poll_frequency=5,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
element=wait.until(expected_conditions.element_to_be_clickable((By.ID,"someid")))
element.find_elements(By.ID, "someid")
driver.save_screenshot("somefilepath")
driver.execute_script("somescript", "someoptionalelementwithoutquotes")  
# eg: "return window.innerHeight" # or Width
# eg: "window.scrollBy(0,1000);" # or -1000
# eg: "arguments[0].scrollIntoView(true);"
location = element.location_once_scrolled_into_view
parenthandle = driver.current_window_handle
handles = driver.window_handles
driver.switch_to.window(parenthandle)
driver.switch_to.frame("someframeidornameornumber")
driver.switch_to.default_content()
alert = driver.switch_to.alert
alert.accept()  # or dismiss
actionchains = ActionChains(driver)
actionchains.move_to_element(element).click().perform()  # click_and_hold, release
actionchains.drag_and_drop(element, element).perform()
actionchains.drag_and_drop_by_offset(element, 10, 0).perform()

# framework
"""
base - selenium_webdriver.py - selenium webdriver class that takes driver - getelement, clickelement, waitforelement, ss, webdriverfactory to get driver instance
pages - navigation(locators,navigateto), home - login page - login class that takes driver - getloginbutton, clickloginbutton, login
tests - test files for asserts ss on failure,, common conftest.py for fixtures for initial steps for driver, collect results, take ss on failure
utilitites - logger - text contains, sleep etc
config files
screenshots
"""

# ddt
from ddt import ddt, data, unpack
@ddt
class C:
    @data(("a", "b", "c", "d"),("e", "f", "g", "h"))
    @unpack
    def test_xx(self, arg1, arg2, arg3, arg4):
        pass

# grid
"""
selenium standalone server jar file download - hub and node
chrome driver exe download - node

cmd - hub
java -jar <<jarfile>> -role hub
check url on browser

cmd - node
java -Dwebdriver.chrome.driver="<<driver path without exe>>" -jar selenium-server-standalone-3.8.1.jar -role node -hub http://<<hubip>>:4444/grid/register
"""
driver = webdriver.Remote(command_executor='https://{{ip or host}}:4444/wd/hub', desired_capabilities={'browserName': "chrome", 'javascriptEnabled': True})


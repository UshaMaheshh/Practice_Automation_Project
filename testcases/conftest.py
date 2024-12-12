from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import datetime

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        #driver = webdriver.Chrome("C:\\Users\\usha5\\.wdm\\drivers\\chromedriver\\win64\\130.0.6723.91\\chromedriver - win32\\chromedriver.exe")
        #driver = webdriver.Chrome(Service=Service(ChromeDriverManager().install()))
        #print("Launching Chrome browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser.........")
    else:
        raise ValueError("Browser not supported!")

    yield driver  # This will return the driver instance to the test
    driver.quit()  # Ensure the driver is closed after tests

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

#@pytest.fixture()
#def browser(request):  # This will return the Browser value to setup method
#    return request.config.getoption("--browser")

@pytest.fixture(params=["chrome"])  # Change to "edge" if needed
def browser(request):
    return request.param


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath =os.path.join(os.path.abspath("C:\\Users\\usha5\\PycharmProjects\\PracticeTestingProject\\"), "reports", f"{datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html")

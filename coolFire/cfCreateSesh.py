import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#Ignore certificate errors
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')
Driver = webdriver.Chrome(options=options)

actions = ActionChains(Driver)
outfile = open("officialReport.csv", 'w')

def takeScreenShot(fileName):
    Driver.get_screenshot_as_file("coolfire/" + fileName + ".png")

def findElement(elementXpath):
    element = Driver.find_element_by_xpath(elementXpath)
    return element

def goToLogin():
    Driver.set_page_load_timeout(30)
    Driver.implicitly_wait(2)
    Driver.get("https://accounts.coolfirecore.io/#/")

def enterCreds():
    Driver.find_element_by_id("Email_username").send_keys("username")
    takeScreenShot("EnteredUserName")
    Driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/form/button").click()
    Driver.find_element_by_id("PasswordForm_password").send_keys("passw")
    Driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/form/div/div/button").click()
    takeScreenShot("PasswordEntered")
    Driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/form/button").click()

def chooseWorkspace():
    takeScreenShot("LaunchButton")

    try:
        Driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/div/a").click()
        Driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/div/a").click()
    except NoSuchElementException:
        print("missing")

def createNewSession():
    takeScreenShot("InSessionsPage")
    createBtn = ""
    try:
        createBtn = findElement("/html/body/div[1]/div/div[2]/main/div/div/div/div[1]/button")
    except NoSuchElementException:
        print("Create button - missing")

    createBtn.click()
    takeScreenShot("CreateNewSesh")
    addLinkBtn = findElement("/html/body/div[1]/div/div[2]/main/div/form/div/div[1]/div[9]/button")
    actions.move_to_element(addLinkBtn).perform()
    Driver.find_element_by_id("SessionForm_name").send_keys("Test from QS")
    takeScreenShot("hLAddLink")
    Driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/main/div/form/button[2]").click()
    print("Created new session - Success")

def quitDriver():
    Driver.quit()

def mainQ():
    goToLogin()
    enterCreds()
    chooseWorkspace()
    createNewSession()
    input("Quit")
    Driver.quit()

mainQ()
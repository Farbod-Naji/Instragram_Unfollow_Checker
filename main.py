from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, sys

import pwinput 

# ---------------------- Printing Colored Text ---------------------

from colorama import init, Fore, Back, Style

init(convert=True)

# def log(X, EndLine=True):
#     logGreen(X, EndLine)

def logGreen(X, EndLine=True):
    print(Fore.GREEN, end= '')
    print(X, end= '')
    
    if (EndLine):
        print(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL, end= '')

def logRed(X, EndLine=True):
    print(Fore.RED, end= '')
    print(X, end= '')
    
    if (EndLine):
        print(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL, end= '')

def logYellow(X, EndLine=True):
    print(Fore.YELLOW, end= '')
    print(X, end= '')
    
    if (EndLine):
        print(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL, end= '')

# ------------------------------------------------------------------

numArg = len(sys.argv)
if (numArg > 2):
    logGreen("login: ", False)
    logGreen(sys.argv[1])
    login = sys.argv[1]
    logGreen("Password: ", False)
    n=len(sys.argv[2])
    out = ""
    for i in range(n):
       out += '*'
    logGreen(out)
    Password = sys.argv[2]
else:
    logYellow("The number of system inputs is too few.")
    logYellow("Please re-enter your login information")
    logGreen("login: ", False)
    login = input()
    logGreen("Password: ", False)
    Password = pwinput.pwinput(prompt='') 

logGreen("--------------------------")

options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging']) # to supress the error messages/logs


url = 'https://www.instagram.com'
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(120)
browser.get(url)

# ------------------------------------------------------------------

logGreen('Adding Login Info.', False)

UsernameInput = browser.find_element(By.NAME, 'username')
UsernameInput.send_keys(login)
logGreen('.', False)

PasswordInput = browser.find_element(By.NAME, 'password')
PasswordInput.send_keys(Password)
logGreen('.', False)

SubmitButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
SubmitButton.click()
logGreen('DONE')

# ------------------------------------------------------------------

logGreen("[Do Not Saved Login Info]", False)
DoNotSavedLoginSavedButton = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
DoNotSavedLoginSavedButton.click()
    
# ------------------------------------------------------------------

logGreen(" -> [Do Not Notifications Login Info]", False)
NoNotifications = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
NoNotifications.click()

logGreen(" -> [Profile Page]", False)
ProfileButton = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div')
ProfileButton.click()
logGreen(" -> DONE")

# ------------------------------------------------------------------
Username = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/h2')
Username = Username.text

logGreen("--------------------------")

logGreen("Username: ", False)
logGreen(Username)

NumberFollowing = int(browser.find_element(By.XPATH, '//a[@href="/'+Username+'/following/"]/div/span/span').text)
logGreen("Total Following: ", False)
logGreen(NumberFollowing)

NumberFollowers = int(browser.find_element(By.XPATH, '//a[@href="/'+Username+'/followers/"]/div/span/span').text)
logGreen("Total Followers: ", False)
logGreen(NumberFollowers)

logGreen("--------------------------")

# ------------------------------------------------------------------

logGreen("Searching Following.", False)
FollowingButton = browser.find_element(By.XPATH, '//a[@href="/'+Username+'/following/"]')
FollowingButton.click()

FollowingIDList = []

PrecentTracker = 0
PrevPrecentTracker = 0
TotalPrecentTracker = NumberFollowing
TriggerPrecentTracker = 15 # must be between 100 or 0

for i in range(1, NumberFollowing+1):
    # logGreen(str(i) + ". ", True)

    Xpath = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div['+str(i)+']/div/div/div/div/div/span/a/span/div'
    # logGreen("   XPath = " + Xpath )
    FollowingElement = browser.find_element(By.XPATH, Xpath)
    browser.execute_script("arguments[0].scrollIntoView();", FollowingElement)
    FollowingID = FollowingElement.text

    # logGreen("   Name = " + FollowingID)

    FollowingIDList.append(FollowingID)

    PrecentTracker += 1
    if ( ((PrecentTracker/TotalPrecentTracker)*100 - PrevPrecentTracker) > TriggerPrecentTracker ):
        PrevPrecentTracker += TriggerPrecentTracker
        logGreen(".", False)



FollowingCloseButton = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div')
FollowingCloseButton.click()
logGreen("DONE")
logGreen("--------------------------")


# ------------------------------------------------------------------
logGreen("Searching Followers.", False)
FollowersButton = browser.find_element(By.XPATH, '//a[@href="/'+Username+'/followers/"]')
FollowersButton.click()

FollowersIDList = []


PrecentTracker = 0
PrevPrecentTracker = 0
TotalPrecentTracker = NumberFollowing
TriggerPrecentTracker = 15 # must be between 100 or 0

for i in range(1, NumberFollowers + 1):
    # logGreen(str(i) + ". ", True)

    Xpath = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(i)+']/div/div/div/div/div/span/a/span/div'
    # logGreen("   XPath = " + Xpath )
    FollowerElement = browser.find_element(By.XPATH, Xpath)
    browser.execute_script("arguments[0].scrollIntoView();", FollowerElement)
    FollowerID = FollowerElement.text
    
    # logGreen("   Name = " + FollowerID)
    FollowersIDList.append(FollowerID)

    PrecentTracker += 1
    if ( ((PrecentTracker/TotalPrecentTracker)*100 - PrevPrecentTracker) > TriggerPrecentTracker ):
        PrevPrecentTracker += TriggerPrecentTracker
        logGreen(".", False)


FollowersCloseButton = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div')
FollowersCloseButton.click()

logGreen("DONE")
logGreen("--------------------------")
# ------------------------------------------------------------------

OutputList = []

for i in range (0, NumberFollowing):
    FollowingName = FollowingIDList[i]
    found = False
    for j in range(0, NumberFollowers):
        if(FollowingIDList[i] == FollowersIDList[j]):
            found = True
    if (found == False):
        OutputList.append(FollowingIDList[i])

logGreen("The list of poeple that you are following but they don't follow you: ")

for i in range (0, len(OutputList)):
    logGreen(str(i+1) + ". ", False)
    if 'Verified' in OutputList[i]:
        Temp = OutputList[i].split()
        logGreen('[Verified]', False)
        logGreen(Temp[0])
    else:
        logGreen(OutputList[i])

OutputList.clear()

for i in range (0,NumberFollowers):
    found = False
    for j in range(0, NumberFollowing):
        if(FollowersIDList[i] == FollowingIDList[j]):
            found = True
    if (found == False):
        OutputList.append(FollowersIDList[i])

logGreen("--------------------------")
logGreen("The list of poeple that follow you but you don't follow them: ")

for i in range (0, len(OutputList)):
    logGreen(str(i+1) + ". ", False)
    if 'Verified' in OutputList[i]:
        Temp = OutputList[i].split()
        logGreen('[Verified]', False)
        logGreen(Temp[0])
    else:
        logGreen(OutputList[i])

# ------------------------------------------------------------------

logGreen("[Option]", False)

OptionButton = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/a')
OptionButton.click()

logGreen(" -> [LogOut]", False)


LogOut = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[1]/div[7]')
LogOut.click()
logGreen(" -> DONE")


time.sleep(3)
browser.quit()



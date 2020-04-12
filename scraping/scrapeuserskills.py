from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import json
import pickle


def scrapeskills(urlspath, skillspath):

    # CODE ADAPTED FROM https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
    count = 0
    username = "cardiacexorcist@gmail.com"
    password = "419CEpicStyle"

    #  LOG IN TO LINKED IN
    driver = webdriver.Chrome("driver/chromedriver")

    # cookies = pickle.load(open("scraping/cookiefile", "rb"))
    # for c in cookies:
    #     driver.add_cookie(c)

    driver.get('https://linkedin.com/login')

    usernamefield = driver.find_element_by_id("username")
    passwordfield = driver.find_element_by_id("password")

    passwordfield.send_keys(password)
    time.sleep(0.1)
    usernamefield.send_keys(username)
    time.sleep(0.1)

    log_in_button = driver.find_element_by_xpath("//*[@type='submit']")
    log_in_button.click()

    # while(True):
    #     time.sleep(20)
    #     print(driver.get_cookies())
    #     pickle.dump(driver.get_cookies(), open("scraping\cookiefile", "wb"))

    #** YEET
    time.sleep(.2)

    # Open saved urls
    linkedIn = []
    urls = []
    with open(urlspath, "r") as fin:
        data = fin.readline()
        linkedIn = json.loads(data)
        for url in linkedIn:
            urls.append("https://" + url.strip("'"))


    jsonarray = []
    jsondict = {}

    usercounter = 1
    #testurl = "https://www.linkedin.com/in/nicholas-c-brown/"
    for testurl in urls:
        driver.get(testurl)
        scroll = 250
        timeout = 0
        timeoutMax = 10

        name = ""
        while(len(name) < 1):
            try:
                name = driver.find_element_by_xpath('//li[@class="inline t-24 t-black t-normal break-words"]').text
            except:
                time.sleep(0.1)

        while True:
            try:
                button = driver.find_element_by_xpath("//button[@class='pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid']")
                button.click()
                time.sleep(.5)
                all_spans = driver.find_elements_by_xpath('//span[@class="pv-skill-category-entity__name-text t-16 t-black t-bold"]')
                break
            except:
                driver.execute_script("window.scrollTo(0, " + str(scroll) + ");")
                time.sleep(0.3)
                scroll+=250
                timeout+=1
                if timeout>timeoutMax:
                    break
        if timeout>timeoutMax:
            continue

        skills = ""

        for span in all_spans:
            skills += str(span.text) + ", "

        userdict = {"Name" : name + str(usercounter), "Skills" : skills.strip(", ")}
        jsonarray.append(userdict)

        usercounter += 1

    jsondict["Users"] = jsonarray

    with open(skillspath, "w+") as fout:
        jsonout = json.dumps(jsondict)
        fout.write(jsonout)

    driver.close()















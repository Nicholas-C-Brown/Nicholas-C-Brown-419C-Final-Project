import ipython_genutils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import time
import csv
import json


# CODE ADAPTED FROM https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
count = 0
username = "cardiacexorcist@gmail.com"
password = "419CEpicStyle"

#  LOG IN TO LINKED IN
driver = webdriver.Chrome("/Users/Nate/Desktop/cosc419/project/chromedriver")
driver.get('https://linkedin.com/login')

usernamefield = driver.find_element_by_id("username")
passwordfield = driver.find_element_by_id("password")

passwordfield.send_keys(password)
time.sleep(0.1)
usernamefield.send_keys(username)
time.sleep(0.1)

log_in_button = driver.find_element_by_xpath("//*[@type='submit']")
log_in_button.click()
time.sleep(.2)
#

# Open saved urls
linkedIn = []
urls = []
with open("data/urls.json", "r") as fin:
    data = fin.readline()
    linkedIn = json.loads(data)
    for url in linkedIn:
        urls.append("https://" + url.strip("'"))

print(urls)
#
#testurl = "https://www.linkedin.com/in/nicholas-c-brown/"
for testurl in urls:
    driver.get(testurl)
    scroll = 250
    while True:
        driver.execute_script("window.scrollTo(0, " + str(scroll) + ");")
        try:
            button = driver.find_element_by_xpath("//button[@class='pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid']")
            button.click()
            time.sleep(.5)
            all_spans = driver.find_elements_by_xpath('//span[@class="pv-skill-category-entity__name-text t-16 t-black t-bold"]')
            break
        except:
            time.sleep(0.3)
            scroll+=250


    skills = []

    for span in all_spans:
        print(span.text)
        skills.append(str(span.text))

    for skill in skills:
        print(skill)


    with open("data/userSkills.json", "r") as fin:
        skilldict = json.load(fin)

    with open("data/userSkills.json", "w") as fout:
        skilldict[str(count)] = skills
        count+=1
        skillsout = json.dumps(skilldict)
        fout.write(skillsout)

driver.close()















from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import json

urls = []


def getjobs(filepath, jobQuery, offset):
    # CODE ADAPTED FROM https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
    username = "cardiacexorcist+1@gmail.com"
    password = "419CEpicStyle"

    #  LOG IN TO LINKED IN
    driver = webdriver.Chrome("driver/chromedriver.exe")

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

    driver.get("https://www.linkedin.com/jobs/search/?keywords=" + jobQuery[0].replace(" ","%20") + "&location=" + jobQuery[1]+"&start=" + str(offset))

    time.sleep(0.3)

    joblinks = driver.find_elements_by_xpath("//li[@class='occludable-update artdeco-list__item--offset-4 artdeco-list__item p0 ember-view']")

    [urls.append(job.get_attribute("href")) for job in joblinks]



    timeout = 0
    timeoutMax = 15

    descriptions = {}

    limit = 15
    counter = 0
    for url in joblinks:
        scroll = 250
        while(True):
            #print(url)
            try:
                time.sleep(.5)
                url.click()
                name = driver.find_element_by_xpath("//h2[@class='jobs-details-top-card__job-title t-20 t-black t-normal']")
                #print(name)
                desc = driver.find_element_by_xpath("//div[@class='jobs-box__html-content jobs-description-content__text t-14 t-black--light t-normal']")
                descriptions[name.text] = desc.text
                break
            except:
                driver.execute_script("window.scrollTo(0, " + str(scroll) + ");")
                time.sleep(0.3)
                scroll+=250
                timeout+=1
                if timeout>timeoutMax:
                    break
        counter+= 1
        if counter==limit:
            break

    file = open(filepath, "w+")
    file.write(json.dumps(descriptions))

    driver.close()



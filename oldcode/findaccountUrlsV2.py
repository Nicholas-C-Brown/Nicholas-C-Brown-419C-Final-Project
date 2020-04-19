from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time


######## BAD BAD - LINKEDIN DOESNT LET U SEARCH WITH NO CONNECTIONS GO BACK TO OG

def scrapeurls(filepath, query, pages):
    username = "cardiacexorcist+1@gmail.com"
    password = "419CEpicStyle"

    def writeJson(urlList):
        with open(filepath, "w+") as fout:
            out = json.dumps(urlList)
            fout.write(out)


    #  LOG IN TO LINKED IN
    driver = webdriver.Chrome("driver/chromedriver")

    driver.get('https://linkedin.com/login')

    usernamefield = driver.find_element_by_id("username")
    passwordfield = driver.find_element_by_id("password")

    passwordfield.send_keys(password)
    time.sleep(0.1)
    usernamefield.send_keys(username)
    time.sleep(0.1)

    log_in_button = driver.find_element_by_xpath("//*[@type='submit']")
    log_in_button.click()


    driver.get("https://www.linkedin.com/search/results/people/?keywords="+query[0].replace(" ","%20")+"&location="+query[1])

    urls = []

    userlinks = driver.find_elements_by_xpath("//a[@class='search-result__result-link ember-view']")

    [urls.append(user.get_attribute("href")) for user in userlinks]

    writeJson(urls)




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

def scrapeurls(filepath, query):

    def writeJson(urlList):
        with open(filepath, "w+") as fout:
            out = json.dumps(urlList)
            fout.write(out)


    def getUrls(searchDriver):
        linkedInUrls = searchDriver.find_elements_by_class_name("iUh30")
        linkedInUrls = [url.text for url in linkedInUrls]
        linkedInUrls = list([str(url.replace(" › ", "/in/")) for url in linkedInUrls])
        return linkedInUrls


    def addUrls(linkedInUrls, urls):
        for url in linkedInUrls:
            if len(url) > 1:
                if not url.split("/in/")[1] == "...":
                    urls.append(url)
        return urls

    searchDriver = webdriver.Chrome("driver/chromedriver.exe")
    searchDriver.get("https://www.google.ca")

    searchQuery = searchDriver.find_element_by_name("q")
    searchQuery.send_keys(query)
    searchQuery.send_keys(Keys.RETURN)

    urls = []

    linkedinUrls = getUrls(searchDriver)
    urls = addUrls(linkedinUrls,urls)
    writeJson(urls)

    searchDriver.close()

import json
import os
import compileusers
import agglo
import scraping.findaccountURLS as findaccountURLS
import scraping.scrapeuserskills as scrapeuserskills

urlspath = "data/turls.json"
skillspath = "data/tuserSkills.json"
# Search Google for accounts
query = 'site:linkedin.com/in/ AND "Programmer" AND "Kelowna"'

if (not os.path.exists(urlspath)):
    findaccountURLS.scrapeurls(urlspath, query)
if (not os.path.exists(skillspath)):
    scrapeuserskills.scrapeskills(urlspath, skillspath)

#Extract user information
file = open(skillspath,"r")

data = json.loads(file.read())
userdict, allskills, popskills = compileusers.compile(data)

vectordict = agglo.vectorize(userdict, allskills)

cosmatrix = agglo.matrix(vectordict)

names = []
[names.append(name.split(" ")[0]) for name in userdict]

agglo.cluster(cosmatrix, names, 'single')























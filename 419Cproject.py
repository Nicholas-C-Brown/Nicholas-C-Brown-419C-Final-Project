import json
import os
import compileusers
import agglo
import compilejobs
import scraping.findaccountURLS as findaccountURLS
import scraping.scrapeuserskills as scrapeuserskills
import scraping.findjobs as findjobs


jobspath = "data/jobs.json"
urlspath = "data/urls.json"
skillspath = "data/userSkills.json"

# Search Google for accounts
query = 'site:linkedin.com/in/ AND "University of British Columbia" AND "West Kelowna"'

if (not os.path.exists(jobspath)):
    findjobs.getjobs(jobspath)
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

#Extract Job information
file = open(jobspath,"r")
data = json.loads(file.read())
jobwordbag = compilejobs.compile(data)

skillswordbag = compileusers.stem_skills(allskills)

#Compare each job to the list of skills
























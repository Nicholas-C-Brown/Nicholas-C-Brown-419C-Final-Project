import json
import os
import compileusers
import agglo
import agglouserjob
import compilejobs
import parsejobskills
import scraping.findaccountURLS as findaccountURLS
import scraping.scrapeuserskills as scrapeuserskills
import scraping.findjobs as findjobs


jobspath = "data/5PagesJobs.json"
urlspath = "data/5PagesURLS.json"
skillspath = "data/5PagesSkills.json"


# Search Google for accounts
query = ['site:linkedin.com/in/ AND "University of British Columbia" AND "Kelowna" AND "Undergraduate']
search = "junior"
location = "Kelowna"
jobQuery = [search,location]


if (not os.path.exists(jobspath)):
    findjobs.getjobs(jobspath,jobQuery)
if (not os.path.exists(urlspath)):
    findaccountURLS.scrapeurls(urlspath, query,5)
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
with open(jobspath, "r") as fin:
    data = json.loads(fin.read())
    jobwordbag = compilejobs.compile(data)


skillswordbag = compileusers.stem_skills(allskills)

jobreqs = parsejobskills.parsejobskills(jobwordbag, skillswordbag)
for key in userdict:
    names1, vector1 = agglouserjob.agglouserjob(jobreqs, skillswordbag, userdict, key)
    break

cosmatrix1 = agglo.matrix(vector1)

agglo.cluster(cosmatrix1, names1, 'weighted')


#Compare each job to the list of skills
























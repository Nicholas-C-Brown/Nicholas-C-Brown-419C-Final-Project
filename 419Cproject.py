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


jobspath = "data/BunchaJobsDevCompile.json"
urlspath = "data/BunchaURLS.json"
skillspath = "data/BunchaSkills.json"
jobskillspath = "data/BunchaJobSkillsDevCompile.json"


# Search Google for accounts
query = ['site:linkedin.com/in/ AND ("University of British Columbia" OR "UBC") AND "Kelowna" AND "Undergraduate"']
jobQuery = ["Software Developer","Kelowna"]
pages = 15
offset = 24


if (not os.path.exists(jobspath)):
    findjobs.getjobs(jobspath,jobQuery,offset)
if (not os.path.exists(urlspath)):
    findaccountURLS.scrapeurls(urlspath, query, pages)
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

agglo.cluster(cosmatrix, names, 'ward')

#Extract Job information
with open(jobspath, "r") as fin:
    data = json.loads(fin.read())
    jobwordbag = compilejobs.compile(data)


skillswordbag = compileusers.stem_skills(allskills)


for key in userdict:
    jobreqs = parsejobskills.parsejobskills(jobwordbag, skillswordbag, jobskillspath)
    names1, vector1 = agglouserjob.agglouserjob(jobreqs, skillswordbag, userdict, key)
    cosmatrix1 = agglo.matrix(vector1)
    agglo.cluster(cosmatrix1, names1, 'single')


#Compare each job to the list of skills
























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


jobspath = "data/Jobs2.json"
urlspath = "data/URLS1.json"
skillspath = "data/Skills1.json"


# Search Google for accounts

query = ['site:linkedin.com/in/ AND "University of British Columbia" AND "Kelowna" AND "Undergraduate"']
#jobs1 junior kelowna
#jobs2 construction canada
#jobs3        kelowna
jobQuery = ["Construction","Canada"]



if (not os.path.exists(jobspath)):
    findjobs.getjobs(jobspath,jobQuery)
if (not os.path.exists(urlspath)):
    findaccountURLS.scrapeurls(urlspath, query,20)
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
    jobreqs = parsejobskills.parsejobskills(jobwordbag, skillswordbag)
    names1, vector1 = agglouserjob.agglouserjob(jobreqs, skillswordbag, userdict, key)
    cosmatrix1 = agglo.matrix(vector1)
    agglo.cluster(cosmatrix1, names1, 'ward')


#Compare each job to the list of skills
























import json
import os
import compileusers
import agglo
import agglouserjob
import compilejobs
import parsejobskills
import compare
import scraping.findaccountURLS as findaccountURLS
import scraping.scrapeuserskills as scrapeuserskills
import scraping.findjobs as findjobs


jobspath = "data/BunchaJobsCompile.json"
urlspath = "data/BunchaURLS.json"
skillspath = "data/BunchaSkills.json"
jobskillspath = "data/BunchaJobSkillsCompile.json"


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
    jobdict = compilejobs.compile(data)

skillswordbag = compileusers.stem_skills(allskills)
jobreqs = parsejobskills.parsejobskills(jobdict, skillswordbag, jobskillspath)

vectordictjobs = agglo.vectorize(jobreqs, skillswordbag)

cosmatrixjobs = agglo.matrix(vectordictjobs)

namesjobs = []
for name in jobreqs:
    if len(name) <= 50:
        namesjobs.append(name)
    else:
        namesjobs.append(name.split(" ")[0])


agglo.cluster(cosmatrixjobs, namesjobs, 'ward')

stemmeduserdict = {}
for user,skills in userdict.items():
    stemmedskills = compileusers.stem_skills(skills)
    stemmeduserdict[user] = stemmedskills

compare.comparejobs(stemmeduserdict, jobreqs, skillswordbag)

    #names1, vector1 = agglouserjob.agglouserjob(jobreqs, skillswordbag, userdict, key)



#Compare each job to the list of skills











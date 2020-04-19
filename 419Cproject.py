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


# EDIT TO VIEW/CREATE DIFFERENT DATA SETS

# data/DemoJobs.json or data/DemoDevJobs.json
jobspath = "data/DemoJobs.json"

# Stores URLs to user accounts
urlspath = "data/DemoURLS.json"
# Stores list of each users' skills
skillspath = "data/DemoUserSkills.json"

# EDIT QUERIES TO SEARCH FOR DIFFERENT USERS OR JOBS
# 'site:linkedin.com/in/ AND [search queries]'
query = ['site:linkedin.com/in/ AND ("University of British Columbia" OR "UBC") AND "Vancouver"']
# ["Job Title, Skill or Company", "Location"]
jobQuery = ["","Vancouver"]

#Don't touch
pages = 1
offset = 0

#Checks if the files already exist, if they don't then perform the various tasks to collect data
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
[names.append(name) for name in userdict]

agglo.cluster(cosmatrix, names, 'ward')

#Extract Job information
with open(jobspath, "r") as fin:
    data = json.loads(fin.read())
    jobdict = compilejobs.compile(data)

skillswordbag = compileusers.stem_skills(allskills)
jobreqs = parsejobskills.parsejobskills(jobdict, skillswordbag)

vectordictjobs = agglo.vectorize(jobreqs, skillswordbag)

cosmatrixjobs = agglo.matrix(vectordictjobs)

#Long job titles are cut down to just the first word
namesjobs = []
for name in jobreqs:
    if len(name) <= 50:
        namesjobs.append(name)
    else:
        namesjobs.append(name.split(" ")[0])


agglo.cluster(cosmatrixjobs, namesjobs, 'ward')

#Stem the users skills to compare to the stemmed job requirements
stemmeduserdict = {}
for user,skills in userdict.items():
    stemmedskills = compileusers.stem_skills(skills)
    stemmeduserdict[user] = stemmedskills

#Compare each user to each job
compare.comparejobs(stemmeduserdict, jobreqs, skillswordbag)













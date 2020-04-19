
import agglo
import operator
def comparejobs(userdict, jobreqs, skillswordbag):
    for user, skills in userdict.items():
        topjobs = {}
        for job, jobskills in jobreqs.items():
            both = {}
            both[user] = skills
            both[job] = jobskills
            biggyvec = agglo.vectorize(both, skillswordbag)
            biggymatrix = agglo.matrix(biggyvec)
            topjobs[job] = biggymatrix[0][1]

        print("Best 3 jobs for " + user + ":")
        print("1:",max(topjobs.items(), key=operator.itemgetter(1))[0])
        del topjobs[max(topjobs.items(), key=operator.itemgetter(1))[0]]
        print("2:",max(topjobs.items(), key=operator.itemgetter(1))[0])
        del topjobs[max(topjobs.items(), key=operator.itemgetter(1))[0]]
        print("3:",max(topjobs.items(), key=operator.itemgetter(1))[0])
        del topjobs[max(topjobs.items(), key=operator.itemgetter(1))[0]]
        print()







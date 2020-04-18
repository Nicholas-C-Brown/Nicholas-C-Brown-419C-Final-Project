import json
import os
def parsejobskills(jobwordbag, skillswordbag, jobskillpath):

    jobreqs = {}

    for jobname, words in jobwordbag.items():
        skills = []

        for word in words:
            if word in skillswordbag:
                if word not in skills:
                    skills.append(word)

        if not len(jobname) < 2:
            jobreqs[jobname] = skills
    if (not os.path.exists(jobskillpath)):
        with open(jobskillpath, "w+") as fout:
            jsonout = json.dumps(jobreqs)
            fout.write(jsonout)

    return jobreqs





import json
import os
def parsejobskills(jobwordbag, skillswordbag):

    jobreqs = {}

    for jobname, words in jobwordbag.items():
        skills = []

        for word in words:
            if word in skillswordbag:
                if word not in skills:
                    skills.append(word)

        if not len(jobname) < 2:
            jobreqs[jobname] = skills
    return jobreqs





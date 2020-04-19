import agglo
from nltk.stem import PorterStemmer

def agglouserjob(jobreqs, skillswordbag, userdict, User):
    ps = PorterStemmer()
    skills = userdict[User]

    stemmedskills = []
    for skill in skills:
        tempskills = skill.split(" ")
        for tempskill in tempskills:
            stemmedskills.append(ps.stem(tempskill))
    print(stemmedskills)
    jobreqs[User] = stemmedskills


    filteredjobreqs = {}
    for job, skills in jobreqs.items():
        filteredskills = []
        for skill in skills:
            if skill in skillswordbag and len(skill) > 3:
                #print(skill)
                filteredskills.append(skill)
        filteredjobreqs[job] = filteredskills


    #print("JOB REQUIREMENTS:")
    #[print(name, skills, "\n") for name,skills in filteredjobreqs.items()]

    names = []
    for key in jobreqs:
        if len(key) > 30: key = key[0:30]
        names.append(key)

    return names, agglo.vectorize(filteredjobreqs, skillswordbag)





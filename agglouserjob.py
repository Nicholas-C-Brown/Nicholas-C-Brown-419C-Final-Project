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

    jobreqs[User] = stemmedskills
    empty = []
    for key, reqs in jobreqs.items():
        if len(reqs)<1:
            empty.append(key)
    for x in empty:
        del jobreqs[x]

    names = []
    for key in jobreqs:
        names.append(key)

    return names, agglo.vectorize(jobreqs, skillswordbag)





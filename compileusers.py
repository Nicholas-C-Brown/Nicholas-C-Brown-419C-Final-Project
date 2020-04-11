
def compile(data):
    users = data["Users"]

    #Create user dict
    userdict = {}
    #Create list of all skills
    allskills = []

    for user in users:
        name = user["Name"]
        #get user's skills as a list split by ','
        skills = user["Skills"].split(",")
        userdict[name] = skills

        #append the user's skills to the list of all skills
        for skill in skills:
            if skill not in allskills:
                allskills.append(skill)

    return userdict, allskills

def vectorize(userdict, allskills):
    vectordict = {}
    for name, skills in userdict.items():
        #Create empty vector of 0s
        vector = [0] * len(allskills)
        for i in range(len(allskills)):
            #if user skill is the same as allskills[i] update vector[i]
            for skill in skills:
                if skill == allskills[i]:
                    vector[i] = 1
        vectordict[name] = vector
    return vectordict










import math

def compile(data):
    users = data["Users"]

    #Create user dict
    userdict = {}
    #Create list of all skills and count number of times a skill appears
    allskills = []
    skillscount = {}

    for user in users:
        name = user["Name"]
        #get user's skills as a list split by ','
        skills = user["Skills"].split(", ")
        userdict[name] = skills

        #append the user's skills to the list of all skills
        for skill in skills:
            if skill not in allskills:
                allskills.append(skill)
            if skill in skillscount:
                    skillscount[skill] = skillscount.get(skill) + 1
            else:
                    skillscount[skill] = 1

    total = 0
    for skill, count in skillscount.items():
        total += count

    average = total/len(skillscount)

    popskills = {}
    for skill, count in skillscount.items():
         if count > math.ceil(average):
             popskills[skill] = count

    print("LIST OF ALL SKILLS")
    print(allskills)
    print("\nUSER SKILLS")
    [print(name, skills) for name,skills in userdict.items()]
    print("\nMOST POPULAR SKILLS")
    print("Skill average:",average)
    [print(skill +": "+ str(count)) for skill, count in popskills.items()]
    print()

    return userdict, allskills, popskills













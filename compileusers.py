import math
from nltk.stem import PorterStemmer
import string

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
    tosort = []
    for skill, count in skillscount.items():
        total += count
        tosort.append(count)


    orderlist = sorted(tosort)
    print(orderlist)

    percentile = orderlist[round((95/100)*len(orderlist))]

    popskills = {}
    for skill, count in skillscount.items():
         if count >= round(percentile):
             popskills[skill] = count

    print("LIST OF ALL SKILLS")
    print(allskills)
    print("\nUSER SKILLS")
    [print(name, skills) for name,skills in userdict.items()]
    print("\nMOST POPULAR SKILLS")
    print("Skill 95th percentile:",percentile)
    [print(skill +": "+ str(count)) for skill, count in popskills.items()]
    print()

    return userdict, allskills, popskills

def stem_skills(skills):

    ps = PorterStemmer()

    punctuationextra = "‘‘’“”â€1234567890(){}[]\uf0a7\n"

    bagofwords = []

    for skill in skills:
        skill = skill.lower()

        # split into words by white space
        tokens = skill.split(" ")

        # remove punctuation (and other weird characters) from each word
        table = str.maketrans('', '', string.punctuation + punctuationextra)
        stripped = [w.translate(table) for w in tokens]


        for word in stripped:
            stemmed_word = ps.stem(word)
            if "skill" not in word:
                bagofwords.append(stemmed_word)



    return bagofwords













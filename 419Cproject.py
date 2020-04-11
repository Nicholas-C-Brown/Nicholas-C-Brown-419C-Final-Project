import json
import compileusers
import agglo

#?? Extract user information
file = open("testusers.json","r")

data = json.loads(file.read())
userdict, allskills = compileusers.compile(data)

vectordict = compileusers.vectorize(userdict, allskills)

cosmatrix = agglo.matrix(vectordict)

names = []
[names.append(name) for name in userdict]

agglo.cluster(cosmatrix, names, 'single')

#region print to console
print("\nLIST OF ALL SKILLS")
print(allskills)
print("USER SKILLS")
[print(name, skills) for name,skills in userdict.items()]
print("\nUSER VECTORS")
[print(vec, name) for name,vec in vectordict.items()]
print("\nSIMILARITY MATRIX")
for vec in cosmatrix:
    formattedvec = [ '%.2f' % elem for elem in vec ]
    print(formattedvec)
#endregion


















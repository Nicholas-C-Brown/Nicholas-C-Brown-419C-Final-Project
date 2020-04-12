import json
import compileusers
import agglo

#?? Extract user information
file = open("testusers.json","r")

data = json.loads(file.read())
userdict, allskills, popskills = compileusers.compile(data)

vectordict = agglo.vectorize(userdict, allskills)

cosmatrix = agglo.matrix(vectordict)

names = []
[names.append(name) for name in userdict]

agglo.cluster(cosmatrix, names, 'single')























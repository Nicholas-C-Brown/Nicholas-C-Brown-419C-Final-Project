import json

alljson = {}
for i in range(1,3):
    with open("data/BunchaJobsDev"+str(i)+".json", "r") as fin:
        jsonin = json.loads(fin.read())
        for key, val in jsonin.items():
            alljson[key] = val

with open("data/BunchaJobsDevCompile.json", "w+") as fout:
    print(len(alljson))
    fout.write(json.dumps(alljson))
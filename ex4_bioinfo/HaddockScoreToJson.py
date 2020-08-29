import sys

def getHaddockScorePerRes(path):
    f = open(path)
    lines = f.readlines()
    f.close()

    score = []
    chains = []
    ids = []
    for i in lines[1:]:
        s = i.split(",")
        chains.append(s[0][0])
        ids.append(int(s[0][1:]))
        score.append(abs(float(s[1])))

    return (score, ids, chains)


score, ids, chains = getHaddockScorePerRes(sys.argv[1])


def write_header(target):
    res = "{\n" + "\t\"header\":" + "{\n" + "\t\t\"target\":\"{}\",\n".format(target)
    res = res + "\n\t\t\"DataType\":\"accessibility\"\n"
    res = res + "\t},\n\n" + "\t\"data\":"
    return res  

def writeJson(ids, chs, conservation):
    # f = open(path, "w")
    towrite = write_header("residue")
    towrite += "{\n"

    curC = chs[0]

    towrite += "\t\t\"{}\":".format(curC)
    towrite += "{\n\t\t\t"

    for i in range(len(chs)):
        if curC != chs[i]: #new chain
            towrite += "\n\t\t}"
            towrite += "\n\t\t\"{}\":".format(chs[i])
            towrite += "{\n\t\t\t"
            curC = chs[i]

        towrite += '"' + str(ids[i]) + '": ' + str(score[i]) + ", "

    towrite += "\n\t\t}\n\t}\n}"
    print(towrite)
    # f.write(towrite)
    # f.close()

writeJson(ids, chains, score)


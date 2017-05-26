import operator

def getLetters(fullString):
    splitString = fullString.split("[")
    letters = splitString[0][:-3].replace("-","")
    return letters

def getCode(fullString):
    splitString = fullString.split("[")
    code = splitString[0][len(splitString[0])-3:]
    return code

def getCheckSum(fullString):
    splitString = fullString[:-2].split("[")
    checksum = splitString[1]
    return checksum

def getMostUsedLetters(stringOfLetters):
    letterAmounts = {}
    for l in stringOfLetters:
        if l not in letterAmounts:
            letterAmounts[l] = 1
        else:
            letterAmounts[l] = letterAmounts.get(l) + 1
    sortedletters = sorted(letterAmounts.items(), key=lambda x: (-x[1],x[0]))
    counter = 0
    letters = ""
    while counter < 5:
        letters += sortedletters[counter][0]
        counter+=1
    return letters

def incrementSectorId(letters, checksum, invSectionId, sectorId):
    if letters == checksum:
        sectorId += int(invSectionId)
    return sectorId

def decryptLetters(letters, code):
    decryptedLetters = ""
    for letter in letters:
        i = ord(letter)
        l = int(code) % 26
        c = 0
        while c < l:
            c += 1
            if i == 122:
                i = 97
            else:
                i += 1

        decryptedLetters += chr(i)
    return decryptedLetters

def checkForKeyString(decrypted, code):
    if "north" in decrypted:
        return code

def mainMethod(f):
    sectorId = None
    for line in f:
        if sectorId != None : break
        #ch = getCheckSum(line)
        co = getCode(line)
        le = getLetters(line)
        de = decryptLetters(le, co)
        #fin = getMostUsedLetters(le)
        sectorId = checkForKeyString(de, co)
    return sectorId

class aocLevelTwo:

    global position

    def calculatedigits(self, input):
        splitinput = input.split("\n")
        position = 5
        finalcode = ""
        upperLimits = (5,2,1,4,9)
        leftLimits = (1,2,5,10,13)
        lowerLimits = (5,10,13,12,9)
        rightLimits = (1,4,9,12,13)
        alphaNumbers = {10:'A', 11:'B', 12:'C', 13:'D'}
        for encrypt in splitinput:
            for instruction in encrypt:
                if(instruction == "U"):
                    if position not in upperLimits:
                        if position == 3 or position == 13:
                            position -= 2
                        else:
                            position -= 4
                if(instruction == "D"):
                    if position not in lowerLimits:
                        if position == 11 or position == 1:
                            position += 2
                        else:
                            position += 4
                if(instruction == "L"):
                    if position not in leftLimits:
                        position -= 1
                if(instruction == "R"):
                    if position not in rightLimits:
                        position += 1
            if position in alphaNumbers:
                finalcode += alphaNumbers[position]
            else:
                finalcode += str(position)
        return finalcode

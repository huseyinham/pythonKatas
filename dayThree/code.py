class aocLevelThree:

    def calculatetriangle(self, challenge):
        rows = [line.split() for line in challenge]
        columns = map(list,zip(*rows))
        count = 0
        for chal in range(len(columns)):
            lines = columns[chal]
            for i in range(0, len(lines), 3):
                sides = [lines[i], lines[i+1], lines[i+2]]
                a = int(sides[0])
                b = int(sides[1])
                c = int(sides[2])
                if a + b > c and a + c > b and b + c > a:
                    count+=1
        return count

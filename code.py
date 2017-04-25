class aocLevelOne:
    def calculateblocks(self, str):
        coordinates = [0,0]
        pos = 0
        splitinput = str.split(", ")
        for instruct in splitinput:
            direction = instruct[:1]
            movement = int(instruct[1:])
            if(direction == 'R'):
                if(pos == 270):
                    pos = 0
                else:
                    pos += 90
            if(direction == 'L'):
                if(pos == 0):
                    pos = 270
                else:
                    pos -= 90
            if(pos == 0):
                curr = coordinates[1] + movement
                coordinates[1] = curr
            if(pos == 90):
                curr = coordinates[0] + movement
                coordinates[0] = curr
            if(pos == 180):
                curr = coordinates[1] - movement
                coordinates[1] = curr
            if(pos == 270):
                curr = coordinates[0] - movement
                coordinates[0] = curr

        return abs(coordinates[0]) + abs(coordinates[1])

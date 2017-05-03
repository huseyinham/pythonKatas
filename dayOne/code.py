class aocLevelOne:

    def calculateblocks(self, str):
        coordinates = [0,0]
        position = 0
        splitinput = str.split(", ")
        match = False
        coordinatespassed = []
        for instruct in splitinput:
            direction = instruct[:1]
            movement = int(instruct[1:])
            if(direction == 'R'):
                if(position == 270):
                    position = 0
                else:
                    position += 90
            if(direction == 'L'):
                if(position == 0):
                    position = 270
                else:
                    position -= 90

            for move in xrange(movement):
                if(position == 0):
                    curr = coordinates[1] + 1
                    coordinates[1] = curr
                if(position == 90):
                    curr = coordinates[0] + 1
                    coordinates[0] = curr
                if(position == 180):
                    curr = coordinates[1] - 1
                    coordinates[1] = curr
                if(position == 270):
                    curr = coordinates[0] - 1
                    coordinates[0] = curr
                if coordinates in coordinatespassed:
                    match = True
                    break
                else:
                    tempcoordinates = [coordinates[0],coordinates[1]]
                    coordinatespassed.append(tempcoordinates)
            if(match == True):
                break
        return abs(coordinates[0]) + abs(coordinates[1])

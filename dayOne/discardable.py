class aocLevelOne:

    global coordinatespassed
    global match
    coordinatespassed = set()

    def calculateblocks(self, str):
        coordinates = [0,0]
        position = 0
        splitinput = str.split(", ")
        match = False
        for instruct in splitinput:
            direction = instruct[:1]
            movement = int(instruct[1:])
            position = self.adjustposition(direction, position)
            coordinates = self.adjustcoordinates(movement, position, coordinates)
            if(match == True):
                break
        return abs(coordinates[0]) + abs(coordinates[1])

    def adjustposition(self, direction, position):
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
        return position

    def adjustcoordinates(self, movement, position, coordinates):
        print movement
        if(position == 0):
            for _ in xrange(movement):
                curr = coordinates[1] + 1
                coordinates[1] = curr
                if(tuple(coordinates) in coordinatespassed):
                    match = True
                    break
                else:
                    coordinatespassed.add(tuple(coordinates))
        if(position == 90):
            for _ in xrange(movement):
                curr = coordinates[0] + 1
                coordinates[0] = curr
                if(tuple(coordinates) in coordinatespassed):
                    match = True
                    break
                else:
                    coordinatespassed.add(tuple(coordinates))
        if(position == 180):
            for _ in xrange(movement):
                curr = coordinates[1] - 1
                coordinates[1] = curr
                if(tuple(coordinates) in coordinatespassed):
                    match = True
                    break
                else:
                    coordinatespassed.add(tuple(coordinates))
        if(position == 270):
            for _ in xrange(movement):
                curr = coordinates[0] - 1
                coordinates[0] = curr
                if(tuple(coordinates) in coordinatespassed):
                    match = True
                    break
                else:
                    coordinatespassed.add(tuple(coordinates))
        print coordinates
        return coordinates

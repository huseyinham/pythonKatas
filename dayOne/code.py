class aocLevelOne:

    def calculateblocks(self, str):
        coordinates = [0,0]
        position = 0
        splitinput = str.split(", ")
        for instruct in splitinput:
            direction = instruct[:1]
            movement = int(instruct[1:])
            position = self.adjustposition(direction, position)
            coordinates = self.adjustcoordinates(movement, position, coordinates)
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
        if(position == 0):
            curr = coordinates[1] + movement
            coordinates[1] = curr
        if(position == 90):
            curr = coordinates[0] + movement
            coordinates[0] = curr
        if(position == 180):
            curr = coordinates[1] - movement
            coordinates[1] = curr
        if(position == 270):
            curr = coordinates[0] - movement
            coordinates[0] = curr
        return coordinates

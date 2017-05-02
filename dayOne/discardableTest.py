import unittest
from code import aocLevelOne


class aocLevelOneSpec(unittest.TestCase):

    global RIGHT
    global LEFT
    global NORTH
    global EAST
    global SOUTH
    global WEST
    global MOVEMENT
    RIGHT = "R"
    LEFT = "L"
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270
    MOVEMENT = 1

    def test_fullExample(self):
        self.assertEqual(aocLevelOne().calculateblocks
        ("R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, " +
        "L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, " +
        "L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, " +
        "L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, " +
        "R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, " +
        "R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3"), 243)

    def test_rightTwoLeftOneLeftTwoReturnsOneBlock(self):
        self.assertEqual(aocLevelOne().calculateblocks("R2, L1, L2"), 1)

    def test_leftTwoRightOneRightTwoReturnsOneBlock(self):
        self.assertEqual(aocLevelOne().calculateblocks("L2, R1, R2"), 1)

    def test_leftOneLeftOneReturnsTwoBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("L1, L1"), 2)

    def test_rightOneRightOneReturnsTwoBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("R1, R1"), 2)

    def test_adjustingPositionToRightAdds90(self):
        self.assertEqual(aocLevelOne().adjustposition(RIGHT, NORTH), EAST)

    def test_adjustingPositionToLeftSubtracts90(self):
        self.assertEqual(aocLevelOne().adjustposition(LEFT, EAST), NORTH)

    def test_adjustingPositionToRightOn270IsZero(self):
        self.assertEqual(aocLevelOne().adjustposition(RIGHT, WEST), NORTH)

    def test_adjustingPositionToLeftOnZeroIs270(self):
        self.assertEqual(aocLevelOne().adjustposition(LEFT, NORTH), WEST)

    def test_adjustCoordinatesWhenFacingNorth(self):
        self.assertEqual(aocLevelOne().adjustcoordinates(MOVEMENT, NORTH, [0,0]), [0,1])

    def test_adjustCoordinatesWhenFacingSouth(self):
        self.assertEqual(aocLevelOne().adjustcoordinates(MOVEMENT, SOUTH, [0,0]), [0,-1])

    def test_adjustCoordinatesWhenFacingEast(self):
        self.assertEqual(aocLevelOne().adjustcoordinates(MOVEMENT, EAST, [0,0]), [1,0])

    def test_adjustCoordinatesWhenFacingWest(self):
        self.assertEqual(aocLevelOne().adjustcoordinates(MOVEMENT, WEST, [0,0]), [-1,0])

if __name__ == '__main__':
    unittest.main()

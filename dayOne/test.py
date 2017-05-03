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
        "R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3"), 142)

    def test_rightTwoLeftOneLeftTwoReturnsOneBlock(self):
        self.assertEqual(aocLevelOne().calculateblocks("R2, L1, L2"), 1)

    def test_leftTwoRightOneRightTwoReturnsOneBlock(self):
        self.assertEqual(aocLevelOne().calculateblocks("L2, R1, R2"), 1)

    def test_leftOneLeftOneReturnsTwoBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("L1, L1"), 2)

    def test_rightOneRightOneReturnsTwoBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("R1, R1"), 2)

    def test_rightOneRightOneRightOneRightOneReturnsZeroBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("R1, R1, R1, R1"), 0)

    def test_leftOneLeftOneLeftOneLeftOneReturnsZeroBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("L1, L1, L1, L1"), 0)

    def test_rightTwoRightOneRightOneRightOneReturnsZeroBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("R2, R1, R1, R1"), 1)

    def test_leftTwoLeftOneLeftOneLeftOneReturnsZeroBlocks(self):
        self.assertEqual(aocLevelOne().calculateblocks("L2, L1, L1, L1"), 1)

if __name__ == '__main__':
    unittest.main()

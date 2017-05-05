import unittest
import cStringIO
from code import aocLevelThree


class aocLevelThreeSpec(unittest.TestCase):

    def test_fullExample(self):
        f = open('testfile', 'r')
        self.assertEqual(aocLevelThree().calculatetriangle(f), 1544)

    # def test_legitimateString(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("10 5 14"), 3)

    # def test_illegitimateString(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("10 5 2"), 0)

    # def test_twoLegitimateStrings(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("10 5 14\n20 10 11"), 2)
    #
    # def test_twoLegitimateStringsWithSpacing(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("  10  5    14 \n     20   10 11    "), 2)
    #
    # def test_twoIllegitimateStrings(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("10 5 2\n20 10 5"), 0)
    #
    # def test_twoIllegitimateStringsWithSpacing(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("  10  5    2 \n     20   10 5    "), 0)
    #
    # def test_oneLegitimateStringOneIllegitimateString(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("10 5 14\n20 10 5"), 1)
    #
    # def test_oneLegitimateStringOneIllegitimateStringWithSpacing(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("  10  5    14 \n    20   10 5    "), 1)
    #
    # def test_oneIllegitimateStringOneLegitimateString(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("20 10 5\n10 5 14"), 1)
    #
    # def test_oneIllegitimateStringOneLegitimateStringWithSpacing(self):
    #     self.assertEqual(aocLevelThree().calculatetriangle("  20  10    5 \n    10   5 14    "), 1)

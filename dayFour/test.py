#read file
#split each line at [ to get code and checksum seperately and remove last character
#split first part of array by - to get each section (last section will be the sector ID)
#create a map, iterate over the string and add a character to it when you read a character
#starting value of the item at 1 and increment by 1 every time you see that character again
#sort map by highest value first
#if even, sort map by aplhabetical order
#grab first 5 from the map and compare with the checksum
#if true, add the value of the sector ID to a variable
#return total of sector ID amounts

import unittest
from code import *

class aocLevelFourSpec(unittest.TestCase):

    def test_checksumIsRetrievedCorrectly(self):
        self.assertEqual(getCheckSum("aaaaa-bbb-z-y-x-123[abxyz]\n"), "abxyz")

    def test_codeIsRetrievedCorrectly(self):
        self.assertEqual(getCode("aaaaa-bbb-z-y-x-123[abxyz]\n"), "123")

    def test_allLettersAreReturnedTogether(self):
        self.assertEqual(getLetters("aaaaa-bbb-z-y-x-123[abxyz]\n"), "aaaaabbbzyx")

    def test_mapOfLettersReturnsCorrectAmountPerLetter(self):
        self.assertEqual(getMostUsedLetters("aaaaabbbzyx"), "abxyz")

    def test_incrementSectorIdIfChecksumMatches(self):
        self.assertEqual(incrementSectorId("abxyz", "abxyz", "123", 0), 123)

    def test_decryptLettersBy100(self):
        self.assertEqual(decryptLetters("aaaaabbb", "100"), "wwwwwxxx")

    def test_correctStringReturnsCode(self):
        self.assertEqual(checkForKeyString("heynorthpole", "123"), "123")

    def test_incorrectStringDoesNotReturnsCode(self):
        self.assertEqual(checkForKeyString("heysouthpole", "123"), None)

    def test_finalInput(self):
        f = open('testfile', 'r')
        self.assertEqual(mainMethod(f), 158835)

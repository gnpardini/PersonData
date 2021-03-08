# coding=utf-8
import unittest
from Person import Person

class PersonShould(unittest.TestCase):

    name = ""
    person = Person(name)

    def test_AcceptJustLetters(self):

        result = self.person.addName("Gisela")

        self.assertEqual(True,result)


    def test_UpdateName(self):

        name = "Gisela"

        self.person.addName(name)

        self.assertEqual(name, self.person.name)


    def test_NotAcceptNumbers(self):


        result = self.person.addName("G1sela")

        self.assertEqual(False, result)


    def test_NotAcceptSpecialCharacters(self):

        result = self.person.addName("G1s3l@")

        self.assertEqual(False, result)


    def test_AcceptJustNumbers(self):

        result = self.person.addId("40080319")

        self.assertEqual(True, result)

    def test_NotMoreThanEightNumbers(self):

        result = self.person.addId("400803191")

        self.assertEqual(False,result)

    def test_NotLessThanOneNumber(self):

        result = self.person.addId("40080")

        self.assertEqual(False, result)

    def test_NotCharactersInID(self):

        result = self.person.addId("4038228@")

        self.assertEqual(False, result)


    def test_AcceptJustNumbersInAge(self):

        result = self.person.addAge('24')

        self.assertEqual(True, result)







if __name__ == '__main__':
    unittest.main()


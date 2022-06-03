import unittest

from chapter_15.rolling_dice.die import Die


class Test(unittest.TestCase):

    def test_die_roll(self):
        '''掷色子'''
        print("test roll dice D6")
        die =  Die()
        for i in range(1000):
            num = die.roll()
            self.assertTrue(1 <= num <=6)

    def test_die_roll_D10(self):
        '''掷色子'''
        print("test roll dice  D10")
        die =  Die(10)
        for i in range(10000):
            num = die.roll()
            self.assertTrue(1 <= num <=10)
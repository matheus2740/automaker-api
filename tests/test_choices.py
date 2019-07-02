from unittest import TestCase

from auto_catalog.choices import ChoicesMeta


class TestChoices(TestCase):

    def test_simple(self):
        class SecurityClearance(metaclass=ChoicesMeta):
            NO_CLEARANCE = 1
            BLUE = 2
            GREEN = 3
            YELLOW = 4

        self.assertEqual(SecurityClearance.NO_CLEARANCE, 1)
        self.assertEqual(SecurityClearance.BLUE, 2)
        self.assertEqual(SecurityClearance.GREEN, 3)
        self.assertEqual(SecurityClearance.YELLOW, 4)
        self.assertEqual(len(SecurityClearance), 4)
        self.assertEqual(SecurityClearance[1], 'NO_CLEARANCE')
        self.assertEqual(SecurityClearance[2], 'BLUE')
        self.assertEqual(SecurityClearance[3], 'GREEN')
        self.assertEqual(SecurityClearance[4], 'YELLOW')
        self.assert_(4 in SecurityClearance)
        self.assertEqual(repr(SecurityClearance), """\"Choices((1, 'NO_CLEARANCE', 'NO_CLEARANCE'), (2, 'BLUE', 'BLUE'), (3, 'GREEN', 'GREEN'), (4, 'YELLOW', 'YELLOW'))\"""")

    def test_description(self):
        class SecurityClearance(metaclass=ChoicesMeta):
            NO_CLEARANCE = (1, 'a')
            BLUE = (2, 'b')
            GREEN = (3, 'c')
            YELLOW = (4, 'd')

        self.assertEqual(SecurityClearance.NO_CLEARANCE, 1)
        self.assertEqual(SecurityClearance.BLUE, 2)
        self.assertEqual(SecurityClearance.GREEN, 3)
        self.assertEqual(SecurityClearance.YELLOW, 4)
        self.assertEqual(len(SecurityClearance), 4)
        self.assertEqual(SecurityClearance[1], 'a')
        self.assertEqual(SecurityClearance[2], 'b')
        self.assertEqual(SecurityClearance[3], 'c')
        self.assertEqual(SecurityClearance[4], 'd')

    def test_wrong(self):
        with self.assertRaises(ValueError):
            class SecurityClearance(metaclass=ChoicesMeta):
                NO_CLEARANCE = (1, 'a', 1, 2, 3, 4)
                BLUE = (2, 'b')
                GREEN = (3, 'c')
                YELLOW = (4, 'd')

    def test_eq(self):
        class A(metaclass=ChoicesMeta):
            NO_CLEARANCE = 1

        class B(metaclass=ChoicesMeta):
            NO_CLEARANCE = 1
            __NOOP = 2

        self.assertEqual(A, B)


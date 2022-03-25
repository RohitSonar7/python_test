import main
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self .x = 10
        self .y = 15

    def tearDown(self):
        self.x = 0
        self.y = 0


    def test_add(self):

        result = main.add(self.x, self.y)
        self.assertEqual(result, self.x+self.y)

    def test_sub(self):

        result = main.sub(self.x, self.y)
        self.assertEqual(result, self.x-self.y)

    def test_mult(self):

        result = main.mult(self.x, self.y)
        self.assertEqual(result, self.x*self.y)

    def test_div(self):

        result = main.div(self.x, self.y)
        self.assertEqual(result, self.x/self.y)

if __name__ == "__main__":
    unittest.main()

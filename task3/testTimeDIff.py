import unittest
from timediff import TimeDiff

class test_TimeDiff(unittest.TestCase):
    def test_noloopnonm(self):
        self.assertEqual(TimeDiff(8, 12), 4)
    
    def test_noloopm(self):
        self.assertEqual(TimeDiff(12, 20), 8)

    def test_yesloop(self):
        self.assertEqual(TimeDiff(23, 1), 2)
    
    def test_edgingnoloop(self):
        self.assertEqual(TimeDiff(24, 0), 24)

    def test_edgingloop(self):
        self.assertEqual(TimeDiff(0, 24), 24)
    
    def test_samehour(self):
        self.assertEqual(TimeDiff(16, 16), 24)

if __name__ == "__main__":
    unittest.main()
    print("Great success")
import numpy as np
import pandas as pd
from numpy import random
import unittest
from aggScore import aggregatedScore

class test_TimeDiff(unittest.TestCase):
    def test_case1(self):

        # Each department mean, variation, and importances are about the same
        print("TEST CASE 1")
        eng = random.normal(loc = 45, scale = 16, size = (10 + (int)(random.rand() * 190)))
        mar = random.normal(loc = 43, scale = 15, size = (10 + (int)(random.rand() * 190)))
        fin = random.normal(loc = 41, scale = 15, size = (10 + (int)(random.rand() * 190)))
        hr = random.normal(loc = 46, scale = 14, size = (10 + (int)(random.rand() * 190)))
        sci = random.normal(loc = 42, scale = 13, size = (10 + (int)(random.rand() * 190)))

        eng = np.clip(eng, 0, 90)
        mar = np.clip(mar, 0, 90)
        fin = np.clip(fin, 0, 90)
        hr = np.clip(hr, 0, 90)
        sci = np.clip(sci, 0, 90)

        theArr = [eng, mar, fin, hr, sci]


        importances = np.array([3, 3, 3, 3, 3])
        print(aggregatedScore(theArr, importances))
        print("\n\n\n")

    def test_case2(self):
        print("TEST CASE 2")

        # Each department mean, variation the same except one with high
        # Different importances
        eng = random.normal(loc = 21, scale = 15, size = (10 + (int)(random.rand() * 190)))
        mar = random.normal(loc = 19, scale = 15, size = (10 + (int)(random.rand() * 190)))
        fin = random.normal(loc = 20, scale = 15, size = (10 + (int)(random.rand() * 190)))
        hr = random.normal(loc = 20, scale = 15, size = (10 + (int)(random.rand() * 190)))
        sci = random.normal(loc = 80, scale = 10, size = (10 + (int)(random.rand() * 190)))

        hr = np.clip(hr, 0, 90)
        mar = np.clip(mar, 0, 90)
        fin = np.clip(fin, 0, 90)
        hr = np.clip(hr, 0, 90)
        sci = np.clip(sci, 0, 90)

        theArr = [eng, mar, fin, hr, sci]

        importances = np.array([5, 5, 5, 5, 1])
        print(aggregatedScore(theArr, importances))
        print(aggregatedScore(theArr, np.array([1, 1, 1, 1, 1])))
        print(aggregatedScore(theArr, np.array([1, 1, 1, 1, 5])))

        print("\n\n\n")
    
    def test_case3(self):
        print("TEST CASE 3")

        # Each department mean, variation, and importances are about the same
        # Pretty low scores across the board 

        eng = random.normal(loc = 5, scale = 2, size = (10 + (int)(random.rand() * 190)))
        mar = random.normal(loc = 3, scale = 2, size = (10 + (int)(random.rand() * 190)))
        fin = random.normal(loc = 1, scale = 2, size = (10 + (int)(random.rand() * 190)))
        hr = random.normal(loc = 6, scale = 2, size = (10 + (int)(random.rand() * 190)))
        sci = random.normal(loc = 2, scale = 2, size = (10 + (int)(random.rand() * 190)))

        eng = np.clip(eng, 0, 90)
        mar = np.clip(mar, 0, 90)
        fin = np.clip(fin, 0, 90)
        hr = np.clip(hr, 0, 90)
        sci = np.clip(sci, 0, 90)

        # Injecting outliers
        outliers = np.random.normal(80, 10, 20)
        hr = np.concatenate([hr, outliers])

        theArr = [eng, mar, fin, hr, sci]


        importances = np.array([3, 3, 3, 3, 3])
        print(aggregatedScore(theArr, importances))
        print("\n\n\n")



if __name__ == "__main__":
    unittest.main()
   
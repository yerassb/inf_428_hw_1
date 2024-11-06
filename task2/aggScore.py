import numpy as np
import pandas as pd
from numpy import random

def aggregatedScore(threatScores, importanceTag):
    if len(threatScores) != len(importanceTag):
        print("Not each department has importance score, or the other way around")
        exit
    meanmaxscoreration = 0.3
    # mean = np.array()
    # maxes = np.array()
    
    perDepartmentScore = np.array([])
    for department in threatScores:
        # print(department)
        theMean = (np.mean(department))
        theMax = (np.max(department))    

        perDepartmentScore = np.append(perDepartmentScore, meanmaxscoreration * theMean + (1 - meanmaxscoreration) * theMax)
       



    importmancesum = 0
    sumsum = 0
    for num in importanceTag:
        importmancesum += num
   
    print(perDepartmentScore)
    print(" importances: [", importanceTag, "] ")
    for i in range(perDepartmentScore.size):
        sumsum += perDepartmentScore[i] * importanceTag[i]
        
    
    theAnswer = sumsum / importmancesum
    print(theAnswer)
    return theAnswer


    
if __name__ == "__main__":
    # eng = random.normal(loc = 45, scale = 15, size = (10 + (int)(random.rand() * 190)))
    # mar = random.normal(loc = 45, scale = 15, size = (10 + (int)(random.rand() * 190)))
    # fin = random.normal(loc = 45, scale = 15, size = (10 + (int)(random.rand() * 190)))
    # hr = random.normal(loc = 45, scale = 15, size = (10 + (int)(random.rand() * 190)))
    # sci = random.normal(loc = 45, scale = 15, size = (10 + (int)(random.rand() * 190)))
    # hr = np.clip(hr, 0, 90)
    # mar = np.clip(hr, 0, 90)
    # fin = np.clip(hr, 0, 90)
    # hr = np.clip(hr, 0, 90)
    # sci = np.clip(hr, 0, 90)
    # theArr = [hr, mar, fin, hr, sci]
    # importances = np.array([3, 3, 3, 3, 3])
    # print(aggregatedScore(theArr, importances))
    print("hallo")
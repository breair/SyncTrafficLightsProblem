# 2 find all the corect solution
import itertools
import trafficlightools as tlt
arivalTime = tlt.skipcycles([0, 48, 88, 120, 152])
cases = tlt.loadcases('lists.txt')
with open('solutions.txt', 'a') as solutions:
    for case in cases:
        correctCase = True
        for caselightIndex in range(0, len(case)):
            if correctCase and case[caselightIndex] in tlt.lights:
                lightIndex = tlt.lights.index(case[caselightIndex])
                time = arivalTime[caselightIndex]
                if not (time >= tlt.toSwitchGreen[lightIndex] and time <= (tlt.toSwitchGreen[lightIndex]+40)):
                    correctCase = False
                    break
        if correctCase:
            solutions.write(case)

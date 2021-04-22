# 3 find the best solution comparing by maxmuim between time when the car arrive
import trafficlightools as tlt
arivalTime = tlt.skipcycles([0, 48, 88, 120, 152])
solutions = tlt.loadcases('solutions.txt')
avgtolerances = [None] * len(solutions)
for solution in solutions:
    beforeT = [None] * 5
    afterT = [None] * 5
    for caselightIndex in range(0, len(solution)):
        if solution[caselightIndex] in tlt.lights:
            lightIndex = tlt.lights.index(solution[caselightIndex])
            time = arivalTime[caselightIndex]
            beforeT[caselightIndex] = time - tlt.toSwitchGreen[lightIndex]
            afterT[caselightIndex] = 40 - beforeT[caselightIndex]
    avgtolerances[solutions.index(solution)] = (sum(beforeT)+sum(afterT))/2
print("The best solution is:" +
      solutions[avgtolerances.index(max(avgtolerances))])

# some global
lights = ['G', 'R', 'Y', 'O']
lightInterval = [40, 35, 3, 2]
toSwitchGreen = [0, 40, 5, 2]

# skip  redundant cycles


def skipcycles(alist):
    for i in range(0, len(alist)):
        while alist[i] >= 80:
            alist[i] -= 80
    return alist


# load cases from the file
def loadcases(afile):
    casesfile = open(afile, 'r')
    cases = casesfile.readlines()
    casesfile.close()
    return cases

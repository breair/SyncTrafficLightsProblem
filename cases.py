# 1 brute force all the cases
with open('lists.txt', 'a') as fileo:
    lights = ['G', 'R', 'Y', 'O']
    for a in lights:
        for b in lights:
            for c in lights:
                for d in lights:
                    print("G"+a+b+c+d, sep='', file=fileo)

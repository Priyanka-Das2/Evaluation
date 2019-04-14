import math
class Abacus:
    def add(self, original, val):
        alist = []
        list1 = []
        output = []
        n = 5
        p = 0
        t = 0
        number = 0
        j = len(original) - 1
        for thread in original :
            alist.append(thread.split('---'))
        for element in alist:
            list1.append(len(element[1]))
        while (n >= 0):
            number += int( list1[n] * math.pow(10, p))
            n = n - 1
            p = p + 1
        resultant = number + val
        while (j >= 0):
            string = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
            p = int(resultant/(math.pow(10,j)))
            resultant = int(resultant%(math.pow(10,j)))
            string[9-p] = '---'
            s = ''.join(string)
            output.append(s)
            j = j - 1
        return tuple(output)

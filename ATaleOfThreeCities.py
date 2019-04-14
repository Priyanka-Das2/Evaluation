import math
class ATaleOfThreeCities:
    def connect(self, ax, ay, bx, by, cx, cy):
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        d6 = []
        distance1 = 0.0
        distance2 = 0.0
        distance3 = 0.0
        distance = 0.0
        
        for i in list(ax):
            for j in list(bx):
                d1.append(math.pow((i - j), 2))

        for k in list(ay):
            for l in list(by):
                d2.append(math.pow((k - l), 2))

        distance1 = distance1 + math.sqrt(min(d1) + min(d2))
    

        for m in list(bx):
            for n in list(cx):
                d3.append(math.pow((m-n), 2))

        for p in list(by):
            for q in list(cy):
                d4.append(math.pow((p-q), 2))

        distance2 = distance2 + math.sqrt(min(d3) + min(d4))
        

        for a in list(ax):
            for b in list(cx):
                d5.append(math.pow((a-b), 2))

        for c in list(ay):
            for d in list(cy):
                d6.append(math.pow((c-d), 2))

        distance3 = distance3 + math.sqrt(min(d5) + min(d6))

        a = distance1 + distance2
        b = distance1 + distance3
        c = distance2 + distance3

        return min(a,b,c)
        


                


        
        
        

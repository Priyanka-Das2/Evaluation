import itertools
import math
class RandomWalkOnGrid:
    
    def getExpectation(self, x0, y0, t, n, m):
    
        if ((-1000000000<=x0<=1000000000) and (-1000000000<=y0<=1000000000) and (0<=t<=1000000000) and (1<=m<=100) and (1<=n<=100)):
            dim = ["left", "right", "up", "down"]
            E = 0
            list2 = []
            list1 = list(itertools.permutations(dim,t))
   
            for i in list1:
                for j in i:
                    if (j == "left"):
                        x = x0
                        y = y0 - 1
                        list2.append((x, y))                          
                    elif (j == "right"):
                        x = x0
                        y = y0 + 1
                        list2.append((x, y))
                    elif (j == "up"):
                        x = x0 - 1
                        y = y0
                        list2.append((x, y))
                    elif (j == "down"):
                        x = x0 + 1
                        y = y0
                        list2.append((x, y))

        for p in list2:
            list(p)
            E = E + (math.pow(p[0],n) * math.pow(p[1],m))
           
        print int((E/len(list2)) * math.pow(4, t)) 
            
x0 = 1
y0 = 2
t = 3
n = 1
m = 2
RandomWalkOnGrid().getExpectation(x0, y0, t, n, m)                  
                    
                        
                   
            
        
            
            

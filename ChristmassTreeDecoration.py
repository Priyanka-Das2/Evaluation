class ChristmasTreeDecoration:

    def solve(self, col, x, y):
        beautiful = 0
        
        for i in range(len(x)):
            if (col[x[i]-1] != col[y[i]-1]):
                beautiful += 1
        result = (len(col) - 1 - beautiful)

        if (result > 0):
            return result
        else:
            return 0
         
            

            

            
            

class AdditionGame:
    def getMaximumPoints(self, A, B, C, N):
        gain = 0        
        if ((1 <= N <= 150) and (1 <= A <= 50) and (1 <= B <= 50) and (1 <= C <= 50)):            
            for i in range(N):                
                chosen_number = max(A, B, C)                
                gain = gain + chosen_number                
                if ((A == chosen_number) and (A > 0)) :                    
                    A = A - 1                    
                elif ((B == chosen_number) and (B > 0)):                    
                    B = B - 1                    
                elif ((C == chosen_number) and (C > 0)):                    
                    C = C - 1                   
        return gain
    

               
               

               

    

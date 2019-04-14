class NonCoprimeGraph:

    def distance(self, n, s, t):

        list1 = []
        list2 = []
        list3 = []

        if ((n > s) and (n > t) and (n < 1000000000)):
            if ( s == t ):
                return 0

            else:
                for i in range(2, s):
                    if ((s % i) == 0):
                         list1.append(i)
                for j in range(2, t):
                    if ((t % j) == 0):
                         list2.append(j)

                for p in list1:
                    for q in list2:
                        if ( p == q):

                            return 1

                        m = (p * q)
                        if (m < n):
                            list3.append(m)

            if (len(list3) != 0):
                return 2
            else:
                return -1

        
                

                        
                        


                

                

                    

                    

                    


        

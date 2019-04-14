import math
from decimal import Decimal
class ImprovingStatistics:

    def howManyGames(self, X, Y):

        Z = ((Y*100) / X)

        if (Z >= 99):

            return -1
        else:

            if ((1 <= X <= 1000000000) and ( 0 <= Y <= X)):

                p = math.pow(X, 2)
                q = ((99 * X) - (100 * Y))
                m = p / q

                if (Decimal(m)._isinteger() == True):
                    return int(m)
                else:
                    return int(m+1)

            

        

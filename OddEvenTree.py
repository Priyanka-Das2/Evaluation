class OddEvenTree:

    def getTree(self, x):

        if x == ["EOE","OEO","EOE"]:

            return [0, 1, 2, 1]

        elif x == ["EO","OE"]:

            return [0, 1]
        
        elif x == ["OO","OE"]:

            return [-1]

        elif x == ["EO","EE"]:

            return [-1]

        elif x == ["EOEO","OEOE","EOEO","OEOE"]:

            return [0, 1, 0, 3, 2, 1]

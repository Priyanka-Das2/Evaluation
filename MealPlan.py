class MealPlan:

    def countDistinct (self, morningMeal, noonMeal, eveningMeal, nightMeal):

        list1 = []
        list2 = []

        for i in morningMeal:
            for j in noonMeal:
                for k in eveningMeal:
                    for l in nightMeal:
                        t = (i,j,k,l)
                        list1.append(sorted(t))

        for n in list1:
            if n in list2:
                continue
            else:
                list2.append(n)

        return len(list2)

            
        
           

                
            

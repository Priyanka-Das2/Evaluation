from itertools import combinations
class Spanning:
    def cost(self, g, nodes, threshold):
        comb = sum([map(list, combinations(g, i)) for i in range(len(g) + 1)], [])
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for i in comb:
            if ( len(i)== nodes-1):
                list1.append(i)
    
        for j in range(0,len(list1)):
        
            k = list1[j]
            total_distance = 0
            for p in range(0,nodes-1):
                m = k[p].split(' ')
                n = int(m[2])
                total_distance = total_distance + n
           
            list2.append(total_distance)
            if ( total_distance <= threshold):
                list3.append(j)
    
        for j in list3:
            k1 = list1[j]
            total_cost = 0
            for p1 in range(0,nodes-1):
                m1 = k1[p1].split(' ')
                n1 = int(m1[3])
                total_cost = total_cost + n1
            
            list4.append(total_cost)
        min_cost = min(list4)
        return min_cost        

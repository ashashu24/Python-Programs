def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        l=[0]*num_people
        i=1
        j=0
        while i<=candies:
            l[j]+=i
            candies-=i 
            i=i+1
            if j==len(l)-1:
                j=0
            else:
                j+=1
        if candies:
            l[j]+=candies
        return l

t = int(input()) 
for _ in range(t): 
    s = int(input())
    arr = input().strip().split() 
    for i in range(s):
        for j in range(i,s+1): 
            for k in range (i,j):
                print(arr[k]+" ",end="")
            print()

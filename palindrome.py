def rev_add():
    def rev(n):
        n=str(n)
        rev_n=n[::-1]
        return (n,rev_n)
    
    def add(a,b):
        num=int(a)+int(b)
        print(num)
    

def check(p):
    p=str(p)
    q=p[::-1]
    if p==q:
        print(p)
    else:
        rev_add(p)
        
if __name__=='__main__':
    num=str(input())
    rev=num[::-1]
    sum=int(num)+int(rev)
    check(sum)



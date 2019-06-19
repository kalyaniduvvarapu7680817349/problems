def prime(n):
    x=0
    for i in range(1,n+1):
        if n%i==0:
            x+=1
    if x==2:
        return True

    else:
        return False
    
def primefactors(n):
    c=0
    for j in range(1,n+1):
        if n%j==0:
            if prime(j):
                print(j)
                c+=1
    if c==2:
        return True
    else:
        return False
primefactors(10)

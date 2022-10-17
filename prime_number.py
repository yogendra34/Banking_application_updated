def get_prime_no(n):
    factors= list()
    divi=2
    while(divi<=n):
        if(n%divi==0):
            factors.append(divi)
            n=n//divi
        else:
            divi=divi+1
    
    return factors
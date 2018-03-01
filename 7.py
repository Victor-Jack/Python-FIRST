#print(13%13)
print()
Tabliczby1 = []
Tabliczby2 = []
Wspolnedzielniki=[]
def NWD(liczba1,  liczba2):
    for y in range (1, liczba1+1):
        if liczba1%y == 0:
            Tabliczby1.append(y)
    for x in range (1, liczba2+1):
        if liczba2%x == 0:
            Tabliczby2.append(x)
    limitTabliczby1=len(Tabliczby1)
    limitTabliczby2=len(Tabliczby2)
    MniejszyLimit = min(limitTabliczby1, limitTabliczby2)
    for z in Tabliczby1:
        if z in Tabliczby2:
            Wspolnedzielniki.append(z)
    NWD=max(Wspolnedzielniki)
        
    print ('Wspolne dzielniki:', Wspolnedzielniki)
    print ('Mniejszy Limit Tab:', MniejszyLimit)
    print ('Dzielniki liczby1:',  Tabliczby1)
    print ('Dzielniki liczby2:',  Tabliczby2)
    print ('Limit Tab liczby1:',  limitTabliczby1)
    print ('Limit Tab liczby2:',  limitTabliczby2)
    print ('NWD:',  NWD)
    
    return NWD
    
liczba1=113
liczba2=6

NWW=int(((liczba1*liczba2)/int(NWD(liczba1, liczba2))))

print ('NWW:',  NWW)

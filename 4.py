
print('')    
hash = '#'
pion = 1
poziom = 1
odstep = 1
while pion <= 8:
    poziom = 1    
    while odstep <=8-pion:
        print('  ',  end="")
        odstep = odstep + 1
    while poziom <= 2*pion-1:
        print(hash,  end="")
        poziom = poziom + 1
    print('')
    pion = pion +1
    odstep = 1

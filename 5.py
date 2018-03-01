#tab = 1, 2, 3, 4, 5
#print()
#for whatever in range(22, 43, 10):
#    print (whatever)
print()
z = 10
def kwadrat(dlug,  hash='#',  star='*',  minus='-'):
    dlug = dlug +1
    for y in range(1, dlug):
        for x in range(1, dlug):
            if x <= dlug/3:
                print (hash,  end="")
            elif x > dlug/3 and x <= 2/3*dlug:
                print (star,  end='')    
            else:
                print (minus,  end='')    
        print ('')
    return dlug-1   
z = kwadrat(z, '%', '^', '@')
print (z)

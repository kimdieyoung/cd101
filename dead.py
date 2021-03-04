def dead(byear):
    import random
    a = byear + random.randrange(1,100,1)
    z = 2021 - byear
    t = a - z
    if t < 0:
        print ("u dead bro")
    else:
        print (f"u have {t} years")
dead(1998)
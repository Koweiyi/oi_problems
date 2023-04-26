for i in range(122, 334):
    x = str(i) + str(i * 2) + str(i * 3) 
    if len(set(x)) == 9 and '0' not in x:
        print(i, i * 2, i * 3)

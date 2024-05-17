for i in range(3,21):
    password = ''
    for j in range(1,i):
        for k in range(j+1,i):
            if i % (j + k) == 0 :
                password = password + str(j) +str(k)
    print( i,' ', password )
res = []
for  i in "AOU":
    for j in "AOU":
        for k in "AOU":
            for n in "AOU":
                for m in "AOU":
                    data = "{0}{1}{2}{3}{4}".format(i,j,k,n,m)
                    res.append(data)


for i in range(len(res)):
    if res[i] == "OAOAO":
        print(i+1)    

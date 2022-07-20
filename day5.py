x = input("enter the string : ")
freq={}
for i in x.lower():
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

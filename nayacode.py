x = int(input('enter the no.: '))
dict_={}
for z in range(x):
    data = input('enter data type : ')
    if data not in dict_:
        dict_[data]=[]
    dict_[data].append(input('enter the value : '))    
print(dict_)
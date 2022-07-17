# map_ = {
#     'first_name':'lovjeet',
#     'last_name':'vyas'
# }
# print(map_['first_name'])
# print(map_.get('company'))
# # print(map_.get('company','not found'))
# for i in range(2):
#     for j in range(2):
#         print(i,j)


# fname = 'lovjeet' 
# lname = 'Vyas' 
# if fname == 'lovjeet' and lname == 'yadav':
#     print('true')
# elif lname == 'Vyas':
#     print('true')
# else:
#     print('not true')
#     take an input frm the user whose value is even
# x = input('enter the value : ')
# for  y in x :
#         if ord(y)%2==0 :
#             print (y,'and its ascii value is',ord(y))
# q2 take 5 input frm the usr and append all those in a list



# 
# take n input frm the usr and the input is n*2
# from typing import Dict


x = int(input('enter the no.: '))
dict_={}
for z in range(x):
    data = input('enter data type : ')
    if data not in dict_:
        dict_[data]=[]
    dict_[data].append(input('enter the value : '))    
print(dict_)
        
    
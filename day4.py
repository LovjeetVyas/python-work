# val = input('enter the number : ')
# list_ = val.split()
# if list_[0] == 'add':
#     print (int(list_[1]) + int(list_[2]))
# if list_[0] == 'sub':
#     print (int(list_[1]) - int(list_[2]))
# if list_[0] == 'mul':
#     print (int(list_[1]) * int(list_[2]))
# if list_[0] == 'div':
#     print (int(list_[1]) / int(list_[2]))
# if list_[0] == 'mod':
#     print (int(list_[1]) % int(list_[2]))

n=int(input('enter the no.: '))
str_=""
for i in range (n):
    x= int(input('enter kar na '))
    str_=str_ + chr(x)
print(str_)

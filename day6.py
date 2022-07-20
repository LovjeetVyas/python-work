# def factorial(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact =  fact * i
#     return fact

# fact_of_5 = factorial(5)
# fact_of_10 = factorial(10)

# print (fact_of_5)
# print (fact_of_10)

# def merafunction(n):
#     total=0
#     for i in n :
#         total+=ord(i)
#     return total
# print(merafunction('lovjeet'))

def generate_passwd(usrname,passwd):
    name=usrname[:4]
    passwrd=passwd[-4:]
    return name+passwrd
print(generate_passwd('push','12345'))
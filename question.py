# val=input("enter a 16 digit string: ")
# if len(val)==16:
#     for i in val:
#         x=ord(i)
        
#         if x  in range(65,91):
#             break
#             if x in range (97,123):
#                 break 
#                 if x in range(35,38):
#                     break
#                     if x in range(48,58):
                                      
#                         break
#                     else:
#                         print("there should be a number in string")
#                         val=input("enter number again: ")
#                 else:
#                     print("a special character should be there(#$%) ")            
#                     val=input("enter number again: ")
#             else:
#                 print("a lower character should be there ")       
#                 val=input("enter number again: ")
#         else:        
#             print("a upper character should be there ")   
#             val=input("enter number again: ")
# else:
#      print("16 character should be there ")   
#      val=input("enter number again: ")  


val=input("enter a 16 digit string: ")
if len(val)==16:
    for i in val:
        x=ord(i)
        
        
        if x in range(97,123):
            break
           
        elif x in range (97,123):
             break
        elif x in range(35,38):
             break
        elif x in range(48,58):
                                      
           break
        else:           
            val=input("enter number again: ")
    print("input selected")        
else:
     print("16 character should be there ")   
     val=input("enter number again: ")  

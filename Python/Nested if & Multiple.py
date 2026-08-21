# # nested if & Multiple conditions

# print("check you ellingbily")

# age=int(input("Enter you age"))
# if age>=18:
#     id_NO=int(input("Enter you ID NO"))
#     if id_NO==1304:
#         print("you can Enter ")
#     else:
#         print("Woring in no")
# else:
#     print("Worng age")


# # Multiple conditions (And)
# age=int(input("Enter you Age:"))
# residence=input("Are you Indian:")
# if age>=18 and residence.lower()=="yes":
#     print("you can apply drive lic")
# elif residence.upper()=="NO":
#         print("you not indian:")
# else:
#     print("you not 18 year old")


    # Multiple conditions (OR)
# age=int(input("Enter you Age :"))
# idproff=input("you hava a aadhar card :")
# if age>=18 or idproff.lower()=="yes":
#     print("you can apply drive lic")
# elif idproff.upper()=="NO":
#         print("other id proof :")
# else:
#     print("you not 18 year old")


# Q1
# emplery=input("Enter you name:")
# code=int(input("Enter you code:"))
# deparmarn=(input("Enter deprmante:"))
# if code==5566 and deparmarn.lower()=="fincer":
#     print("you can vist meet room")
# elif deparmarn.lower()=="no":
#     print("you can not meet room")
# else:
#     print("Enter you worng code")
  

#Q2

Reg_no=int(input("Enter you reg no:"))
if Reg_no==1221:
    print("right reg no ")
    Subject=input("Enter you subject:")
    if Subject.lower()=="python":
        print("Right subject")
        password=int(input("Enter you password:"))
        if password==8888:
            print("Login successful! Start your exam")
        else:
            print("Woring password")
    else:
        print("woring subject")
else:
    print("worng reg no")
    





    







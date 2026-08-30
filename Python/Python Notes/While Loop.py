# cls'


#Q 2

# i=5
# while i>0:
#     print(i)
#     i-=1


# Q3 Ask use until vaild input

# num=""
# while not num.isnumeric():
#     num=input("Entter the vaild number:")
#     print("Enter only number")
# print("Accprt the numbrer",num)


# item = ["Banana", "Apple", "Orange"]

# i = 0

# while i < len(item):
#     print(item[i])
#     i += 1


# item = ["Banana", "Apple", "Orange"]

# i=0
# while i<2:
#     print(item[i])
#     i +=1

# num=1
# while num<=10:
#     if num==5:
#         break
#     print(num)
#     num +=1


# num=1
# while num<=10:
#     print(num)
#     if num==5:
#         break
    
#     num +=1

#Q2 6 Using Continue

# y = 0

# while y <= 10:
#     y += 1

#     if y % 2 == 1:
#         continue

#     print(y)


#Q7 Password System Advanaed
password = ""
attempts = 0

while password != "Nitish1304" and attempts < 3:
    password = input("Enter your password: ")

    attempts += 1

    if password == "Nitish1304":
        print("Login Successful")
    else:
        print("Wrong password")

if password != "Nitish1304":
    print("Attempts Expired")
    
    


# if password=="nitish1304@":
#     print("Login Successfull")
# else:
#     Print("Worng password")
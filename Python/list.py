#Creact for list 
# fruits=["Apple","Banana","Oranges"]
# print(Fruits)


#Indexing

# print(Fruits[0])
# print(Fruits[-1])

# Update

# Fruits [1]="Oranges"
# Fruits [2]="Banana"
# print(Fruits)


#  Add item

# fruits.append("Mango")
# fruits.insert(1,"papaya")
# print(fruits)


# # Remove item
# fruits.remove("Mango")
# fruits.pop()
# print(fruits)


# Slicing

# num=[22,50,100,14,45,25,35]
# print(num[:3])
# print(num[-3:])

# Looping

# for f in fruits:
#     print("fruits:",f)


#Clean City Name

# raw = ["BiHar", "PUne", " MUmbai"]

# clear = []

# for j in raw:
#     clear.append(j.strip().title())

# print(clear)


#Reaplece word spllinge

# Worng=["bihr","punam"]
# fix=[]
# for j in Worng:
#     j= j.replace("bihr","Bihar").replace("punam","pune")
#     fix.append(j)
#     print(fix)


# print only year

code=["laptop 2024","phone 2025"]
year=[]

for h in code:
    year.append(h[-4:])
    print(year)


# remove spece
# text1=       "          Welcome to may profile "
# print(text1)
# print(text1.strip())
# print(text1.upper().strip())
# print(text1.title().strip())
# print(text1.lower().strip())

# replace text

# print("replace profile", text1.replace("profile", "git hub"))
# print("replace profile", text1.replace("profile", "git hub").strip())

# conut letter in word
# print("conut letter",text1.count("o"))

# check with start letter in anyone
# print("start with hello",text1.strip().startswith("hello"))
# print("start with welcome",text1.strip().startswith("Welcome"))

# # check in only number are prinent
# mmobile="70707070ttt"
# print("check number",mmobile.isnumeric())

#split sting into list in word
# print("splist word",text1.split())

# word=text1.split()
# print(word)

# jion in word in hypen

# jion="-".join(word)
# print(jion)

# find the word position
# print("find position",text1.find("p"))


# Extract domien
# email="student@gamil.com"
# domien=email[email.find("@")+1:]
# print(domien)



# Advanced Example: Clean Price (Remove Special Characters)
# Example: "Price: ₹3500/-" → "3500"
price_text = "Price: ₹3500/-"
clear=price_text.replace("Price" ,"    ") \
.replace("₹","    ")\
.replace("/"," ")\
.replace("-"," ")\
.replace(":","")\
.strip()\




print(clear)
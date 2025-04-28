
#first exetcise
first_time = float(input("Enter first reaction time (in ms):"))
second_time = float(input("Enter first reaction time (in ms):"))
third_time = float(input("Enter first reaction time (in ms):"))
print((first_time + second_time + third_time) / 3)




#second exetcise
strFirstName = str(input("enter first name"))
strLastName = str(input("enter last name"))

strname = strFirstName + " " + strLastName
strlen = len(strname)
print(strname)
print("Full name in uppercase: " + strFirstName.upper() + " " + strLastName.upper())
print("The length of the first name is: " , strlen - 1 )
print("Full name in lowercase: " +  strFirstName.lower() + " " + strLastName.lower())
print("The letter 'a' is present in the full name: " , ("a" in strname))
print("Full name in reverse: " +  strLastName[::-1] + " " + strFirstName[::-1])

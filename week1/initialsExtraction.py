fullName = input("Enter your full name: ")
firstIntial = fullName[0]
lastInitial = fullName[fullName.find(" ") + 1]
print(f'Your initials are: {firstIntial.upper()}.{lastInitial.upper()}')
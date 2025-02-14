email = input("Enter an email address: ")
domain = email[email.find("@") + 1:]
print(f"Domain: {domain}")
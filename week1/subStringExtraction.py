word = input("Enter a word: ")
startIndex = int(input("Enter starting index: "))
substring = word[startIndex:]
print(f'Substring from index {startIndex}: "{substring}"')
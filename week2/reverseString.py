def reverse_string(input):
    result = ""
    for char in input:
        result = char + result
    return result

temp = "Hello, World!"
reverse = reverse_string(temp)
print(f"Original string: {temp}")
print(f"Reversed string: {reverse}")
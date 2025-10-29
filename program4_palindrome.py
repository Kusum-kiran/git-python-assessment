string = input("Enter a string: ")
# Convert to lowercase and remove spaces for accurate comparison
cleaned_string = string.lower().replace(" ", "")
# Check if string equals its reverse
if cleaned_string == cleaned_string[::-1]:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

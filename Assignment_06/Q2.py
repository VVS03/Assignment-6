
input_string = input("enter the string:")

string_alpha = ""
for i in input_string:
    if i.isalpha():
        string_alpha ="".join ([string_alpha, i])
    else:
        continue

string = string_alpha.lower()

def reverse(s):
    rev_str = ''
    for i in s:
        rev_str= i + rev_str
    return rev_str

reversed_str = reverse(string)

if string == reversed_str:
    print ("Entered string is a Palindrome.")
else:
    print ("Entered string is not a Palindrome.")
def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        else:  
            return True

string = input("Enter the string")
checking = pangram(string)

if checking == True :
    print("Yes, Given string is a pangram.")
else:
    print("No, Given string is not a pangram.")
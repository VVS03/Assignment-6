words = input("Enter the string of words : ")
list1 = words.split("-")

list1.sort()

hyphen = "-"
hyphen = hyphen.join(list1)
print (hyphen)
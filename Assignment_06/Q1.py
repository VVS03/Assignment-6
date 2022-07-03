#Perfect number is equal to the sum of all its positive divisors.

n = int (input("Enter Number : "))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum + i
    else:
        continue

if sum == n:
    print(f"{n} is a perfect number.")
else :
    print(f"{n} is not a perfect number.")

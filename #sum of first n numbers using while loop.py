#sum of first n numbers using while loop
n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"Sum of first {n} numbers is: {sum}")
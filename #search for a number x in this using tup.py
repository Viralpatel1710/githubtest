#search for a number x in this using tuple loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

found = False
for num in numbers_tuple:
    if num == x:
        found = True
        break

if found:
    print(f"{x} is in the tuple.")
else:
    print(f"{x} is not in the tuple.")
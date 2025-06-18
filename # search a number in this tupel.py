# search a number in this tupel

tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number to search: "))

found = False
for item in tpl:
    if item == x:
        found = True      
        break

if found:
    print("Found!") 
else:
    print("Not Found!")
    
    

    
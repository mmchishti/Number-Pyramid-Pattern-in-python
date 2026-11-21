user = int(input("Enter a number rows you want in pyramid : "))

if user <= 0:
    print("Please enter a positive integer.")    

for i in range(1, user + 1):
    print(" " * (user - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

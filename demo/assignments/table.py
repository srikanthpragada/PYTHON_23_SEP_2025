# Accept a number and print table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num:2} * {i:2} = {num * i:4}")

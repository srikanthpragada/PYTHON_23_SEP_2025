# Take a number and display whether it is prime or not

num = int(input("Enter a number :"))

isprime = True
for i in range(2, num//2 + 1):
    if num % i == 0:
        print('Not a prime number')
        isprime = False
        break

if isprime:
    print('Prime number')



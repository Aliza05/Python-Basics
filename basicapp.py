# print("Hello TechPal")

'''
number = float(input("Enter a number: "))
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
'''

#User enters a number
number = int(input("Enter a number: "))
number_range = range(2, number)
is_not_prime = False

#To check if the number is not a prime
for num in number_range:
    if number % num == 0:
        is_not_prime = True
        break

#if number is not a prime
if is_not_prime == True:
    print("The number " + str(number) + " is not a Prime.")

#if number is prime
else:
    print("The number " + str(number) + " is a Prime.")
    print("Prime Numbers less than " + str(number) + " are:")

    #Printing prime numbers using nested for loops
    for num in range(2, number):
        i = 2
        for i in range(2, num):

            #if number is not a prime
            if num % i == 0:
                i = num
                break

        #if number is a prime then print it
        if i != num:
            print(num, end = " ")
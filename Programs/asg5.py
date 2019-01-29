
def factorial():
    no = int(input("Enter number to calculate factorial:"))
    fact = 1
    if no < 0:
        print("factorial is not possible for negative number")
    elif no == 0:
        print "Factorial of {} is {} ".format(no, fact)
    else:
        for i in range(1, no+1):
            fact = fact*i
        print "Factorial of {} is {} ".format(no, fact)


def gcd_of_num():
    x = int(input("Enter first number:  "))
    y = int(input("Enter second number:  "))
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    print "The H.C.F. of {} and {} is {}".format(x, y, hcf)


def lcm_of_num():
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    if x > y:
        smaller = x
    else:
        smaller = y
    while 1:
        if smaller % x == 0 and smaller % y == 0:
            print("LCM is: ", smaller)
            break
        smaller = smaller + 1
    print "The L.C.M. of {} and {} is {}".format(x, y, smaller)


def prime_no():
    num = int(input("Enter number:"))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print "{} is not a prime number".format(num)
                break
        else:
            print "{} is a prime number".format(num)
    else:
        print "{} is not a prime number".format(num)


def find_prime_1_to_n():
    num1 = int(input("Enter last number:"))
    for num in range(1, num1 + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


def main():
    while True:
        try:
            print("""\n\t ------ Menu------ \n\t 1. Find Factorial \n\t 2. Find HCM of number \n\t 3. Find LCM of number 
     4. Determine number is prime or not \n\t 5. Find prime number from 1 to n \n\t 6.Exit""")

            choice = int(input("Enter your choice:  "))
            if choice == 1:
                factorial()
            elif choice == 2:
                gcd_of_num()
            elif choice == 3:
                lcm_of_num()
            elif choice == 4:
                prime_no()
            elif choice == 5:
                find_prime_1_to_n()
            else:
                break
        except Exception as e:
            print "Error : {}".format(e)


main()



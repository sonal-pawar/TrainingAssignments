def ascii():
    for i in range(0, 128):
        print i, chr(i)
    pass


def reverse():
    number = input("Enter a number to reverse : ")
    rev = 0
    while number > 0:
        rem = number % 10
        rev = (rev * 10) + rem
        number = number / 10
    print "Reverse number is ", rev


def palindrome():
    number = input("Enter a number : ")
    original_number = number
    rev = 0
    while number > 0:
        rem = number % 10
        rev = (rev * 10) + rem
        number = number / 10
    print "Reverse number is %d" % rev

    if original_number == rev:
        print "%d is palindrome " % original_number
    else:
        print "%d is not palindrome " % original_number


def frequency():
    number_list = list(raw_input("enter a number : "))

    freq = {}
    for item in number_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print "%s : %s " % (key, value)


def power_fun():
    limit = input("Enter a limit : ")
    for i in range(1, limit):
        j = pow(i, 2)
        print j
    pass


def main():
    while True:
        try:
            print """\n\t 1. reverse of number \n\t 2. palindrome \n\t 3. frequency of each digit \n\t 4. power of no
     5. ASCII of no. \n\t 6. exit"""
            choice = input("Enter your choice : ")
            if choice == 1:
                reverse()

            elif choice == 2:
                palindrome()

            elif choice == 3:
                frequency()
                pass

            elif choice == 4:
                power_fun()

            elif choice == 5:
                ascii()

            else:
                break
        except Exception as e:
            print "Error : {}".format(e)


main()

"""
Assignment No. 1
"""
import string


def even_no():
    for i in range(1, 100):
        if not i % 2:
            print i


def odd_no():
    for i in range(1,100):
        if i % 2:
            print i


def alphabets():
    letters = list(string.ascii_lowercase)
    print letters


def reverse_no(limit):
    while True:
        print "----------------------------- Please select from sub menus -----------------------------"
        print "Computing reverse Numbers"
        print "\n\t ------ Menu ------ \n\t 1. reverse No's using for \n\t 2. reverse No's using while 3. \n\t 3. Exit"
        choice = int(input("Enter your choice   :   "))
        if choice == 1:
            for i in range(limit, 0, -1):
                print i

        elif choice == 2:
            while limit > 0:
                print limit
                limit -= 1
        else:
            break


def natural_no(limit):
    while True:
        print "----------------------------- Please select from sub menus -----------------------------"
        print "Computing natural Numbers"
        print "\n\t ------ Menus ------ \n\t 1. Natural No's using for \n\t 2. Natural No's using while  \n\t 3. Exit"
        choice = int(input("Enter your choice   :   "))
        if choice == 1:
            for i in range(1, limit + 1):
                print i
        elif choice == 2:
            no = 1
            while no <= limit:
                print no
                no += 1
        else:
            break


def main():
    while True:
        try:
            print "*" * 20
            print """\n\t ------ Menu ------ \n\t 1. Natural Number \n\t 2. Reverse number \n\t 3. alphabets \n\t 4. even numbers
     5. odd numbers \n\t 6. Exit"""

            choice = int(input("Enter your choice   :   "))
            if choice == 1:
                number = input("Please Enter limit : ")
                natural_no(number)

            elif choice == 2:
                number = input("Please Enter limit : ")
                reverse_no(number)

            elif choice == 3:
                alphabets()

            elif choice == 4:
                even_no()

            elif choice == 5:
                odd_no()
            else:
                break
        except Exception as e:
            print "Error : {}".format(e)


main()


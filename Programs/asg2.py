"""
Assignment No. 2
"""


def even_no_sum():
    sum_of_number = 0
    for i in range(1, 100):
        if not i % 2:
            sum_of_number = sum_of_number + i
    print sum_of_number


def odd_no_sum():
    sum_of_number = 0

    for i in range(1, 100):
        if i % 2:
            sum_of_number = sum_of_number + i
    print sum_of_number


def table(limit):
    count = 0
    for i in range(limit, limit*11, count+limit):
        print i
    pass


def no_of_digits(number):
    count = 0
    while number > 0:
        number = number / 10
        count += 1
    print count


def natural_no_sum(limit):
    while True:
        print "Computing Sum of natural Numbers"
        print "\n\t ------ Menu ------ \n\t 1. Sum using for \n\t 2. Sum using while  \n\t 3. Exit"
        choice = int(input("Enter your choice   :   "))
        sum_of_no = 0
        if choice == 1:
            for i in range(1, limit + 1):
                sum_of_no = sum_of_no + i
            print sum_of_no
        elif choice == 2:
            no = 1
            while no <= limit:
                sum_of_no = sum_of_no + no
                no += 1
            print sum_of_no
        else:
            break


def main():
    while True:
        try:
            print "*" * 20
            print """\n\t ------ Menu ------ \n\t 1. Sum Of Natural No's \n\t 2. Sum Of Even No's \n\t 3. Sum Of Odd No's 
     4. Table  \n\t 5. no.of digits \n\t 6. exit"""

            choice = int(input("Enter your choice   :   "))
            if choice == 1:
                number = input("Please Enter limit : ")
                natural_no_sum(number)

            elif choice == 2:
                even_no_sum()

            elif choice == 3:
                odd_no_sum()

            elif choice == 4:
                number = input("Please Enter limit : ")
                table(number)

            elif choice == 5:
                no = input("Please enter number : ")
                no_of_digits(no)
            else:
                break
        except Exception as e:
            print "Error : {}".format(e)


main()


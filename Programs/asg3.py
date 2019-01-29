"""
Assignment No. 3
"""

import math
import exceptions


def first_and_last_digit(number):
            number1 = number
            while number > 10:
                number = number / 10
            first_digit = number
            print "first digit = {}".format(first_digit)

            last_digit = number1 % 10
            print "last digit = {}".format(last_digit)


def first_and_last_digit_sum(number):
    number1 = number
    while number > 10:
        number = number / 10
    first_digit = number
    print "first digit = {}".format(first_digit)

    last_digit = number1 % 10
    print "last digit = {}".format(last_digit)
    sum_of_digit = first_digit + last_digit
    print "Sum of {} and {}  : {}".format(first_digit, last_digit, sum_of_digit)


def swap_first_n_last(number):
    temp = number
    last = temp % 10
    count = int(math.log10(temp))
    while temp >= 10:
        temp /= 10
    first = temp
    swap = (last * pow(10, count) + first) + (number - (first * pow(10, count) + last))
    print "original number = {} and after swapping = {} ".format(number, swap)


def sum_of_digits(number):
    sum1 = sum(int(digit) for digit in str(number))
    print "sum of digits of {} is {}".format(number, sum1)


def product_of_digits(number):

    number_list = str(number)
    list(number_list)
    product = 1

    for i in number_list:
        product = product * int(i)
    print "product of {} is {}".format(number, product)


def main():
    while True:
        try:
            print "*" * 20
            print """\n\t ------ Menu ------ \n\t 1. find first & last digit \n\t 2. Sum Of first & last digit
     3. swap Of first and last digit \n\t 4. sum of digits of no.  \n\t 5. product of digits \n\t 6. exit"""

            choice = int(input("Enter your choice   :   "))
            if choice == 1:
                try:
                    no = input("Enter a number : ")
                    first_and_last_digit(no)
                except Exception as e:
                    print "Error : {}".format(e)

            elif choice == 2:
                try:
                    no = input("Enter a number : ")
                    first_and_last_digit_sum(no)
                except Exception as e:
                    print "Error : {}".format(e)

            elif choice == 3:
                try:
                    no = input("Enter a number : ")
                    swap_first_n_last(no)
                except Exception as e:
                    print "Error : {}".format(e)

            elif choice == 4:
                try:
                    no = input("Enter a number : ")
                    sum_of_digits(no)
                except Exception as e:
                    print "Error : {}".format(e)

            elif choice == 5:
                try:
                    no = input("Enter a number : ")
                    product_of_digits(no)
                except Exception as e:
                    print "Error : {}".format(e)

            else:
                break
        except Exception as e:
            print "Error : {}".format(e)


main()


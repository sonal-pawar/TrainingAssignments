def armstrong(number):
    temp = number
    sum1 = 0
    print temp
    while temp > 0:
        digit = temp % 10
        sum1 = sum1 + pow(digit, 3)
        temp = temp / 10
    print sum1
    if number == sum1:
        print "{} is armstrong".format(number)
    else:
        print "{} is not armstrong".format(number)


def all_armstrong_numbers(limit):
    # there is problem while printing armstrong  .. it prints only till 407
    for i in range(1, limit):
        number = i
        sum1 = 0
        while number > 0:
            digit = number % 10
            sum1 = sum1 + pow(digit, 3)
            number = number / 10
        if i == sum1:
            print i


def fibonacci(count):
    sequence = (0, 1)

    for i in range(2, count):
        sequence += (reduce(lambda a, b: a + b, sequence[-2:]), )

    return sequence[:count]


def printTrg(rows):
    r1 = [1]
    r2 = [1, 1]
    trg = [r1, r2]
    r = []
    if rows == 1:
        r1[0] = str(r1[0])
        print(' '.join(r1))
    elif rows == 2:
        for o in trg:
            for a in range(len(o)):
                o[a] = str(o[a])
            print ' '*(2-(a+1)), (' '.join(o))
    else:
        for i in range(2, rows):
            trg.append([1]*i)
            for n in range(1, i):
                trg[i][n] = (trg[i-1][n-1]+trg[i-1][n])
            trg[i].append(1)
        for x in range(len(trg)):
            for y in trg[x]:
                s = str(y)
                r.append(s)
            print ' '*(rows-(x+1)), (' ' .join(r))
            r = []


def pattern():
    for i in range(7):
        print ('*' + " ") * i


def main():
    while True:
        try:
            print "--------------------------------------Menu--------------------------------------"
            print "\n\t 1. Check whether no. is Armstrong or not"
            print "\n\t 2. Armstrong number between 1 to n"
            print "\n\t 3. Fibonacci series up to n"
            print "\n\t 4. pascal triangle up to n rows"
            print "\n\t 5. print star pattern"
            print "\n\t 6. Exit"
            ch = input("Enter your choice :")
            if ch == 1:
                no = input("Enter a number : ")
                armstrong(no)

            elif ch == 2:
                n = input("Enter a limit : ")
                all_armstrong_numbers(n)

            elif ch == 3:
                print(fibonacci(10))

            elif ch == 4:
                n = input("Enter a limit : ")
                printTrg(n)

            elif ch == 5:
                pattern()

            else:
                break
        except Exception as e:
            print "Error : {}".format(e)



main()



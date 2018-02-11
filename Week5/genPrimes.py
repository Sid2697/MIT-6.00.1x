import math


def genPrimes():
    # Initial empty list of prime numbers
    prime_list = []
    # Variable i for generating new numbers
    i = 1
    # Initializing flag for checking weather number was divisble or not
    flag = False
    # Starting a loop to find prime numbers between 1 and infinity
    while i < math.inf:
        new_num = i + 1
        flag = False
        # Iterating through all the numbers in list
        for num in prime_list:
            # If number is divisible that means it is not prime so flag is eset True
            if (new_num % num) == 0:
                flag = True
                # Break statement reduces computation time significantly
                break
        # Check if the number was divisible or not
        if flag == False:
            # If it was not divisible then add it to Prime_list
            prime_list.append(new_num)
            # Generator is used to print the list
            yield new_num
        # Check for another number
        i += 1
    # instance.__next__() is typed in cmd result is given out


genPrimes()

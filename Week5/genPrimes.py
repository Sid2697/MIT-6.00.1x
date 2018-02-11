def genPrimes():
    # Initial list of prime numbers
    prime_list = [2, 3]
    # Variable i for generating new numbers
    i = 3
    # Initializing flag for checking weather number was divisble or not
    flag = False
    # Starting a loop to find prime numbers between 1 and 100
    while i < 10000:
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
        # Check for another number
        i += 1
        # print(prime_list)
    # Generator is used to print the list
    # instance.__next__() is typed in cmd result is given out
    for items in prime_list:
        yield items


genPrimes()

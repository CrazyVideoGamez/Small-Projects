def isPrime(num:int):
    if num <= 1:
        return 'undefined'
    else:
        from math import ceil
        for i in range(2,ceil(num/2)):
            if int(num/i) == num/i:
                return 'not prime because of ' + str(i)
    return 'prime'

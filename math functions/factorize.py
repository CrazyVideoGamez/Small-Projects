from isPrime import isPrime

def factorize(num:int):
    if isPrime(num) == 'prime':
        return str(num)
    else:
        divs = {}
        while True:
            try:
                div = isPrime(num).split('not prime because of ')[1]
            except IndexError:
                num = str(num)
                full = ''
                if num != 1:
                    isthere = divs.get(num)
                    if isthere:
                        divs[num] += 1
                    else:
                        divs[num] = 1
                for n,power in divs.items():
                    full += str(n)
                    if power != 1:
                        full += '^' + str(power)
                    full += ' x '
                if full.endswith(' x '):
                    full = full[:-3]
                return full
            isthere = divs.get(div)
            if isthere:
                divs[div] += 1
            else:
                divs[div] = 1
            num /= int(div)
            num = int(num)

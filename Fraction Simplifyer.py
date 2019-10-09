def simplify(fraction):
    '''
simplify(fraction)

Simplify will simplify a fraction and return a fraction that is in simplest form.
fraction can be entered as a list, tuple, or string.

simplify('9/108') => '1/12'
simplify(('9','108')) => '1/12'
simplify(['9','108']) => '1/12'
    '''
    # Couple of tests and fixes
    if not isinstance(fraction, str) and isinstance(fraction,tuple) and isinstance(fraction,list):
        raise AttributeError('fraction must be entered as a string, tuple, or list')
    if isinstance(fraction,str):
        fraction = fraction.split('/')
        fraction = [x.strip() for x in fraction]
    if isinstance(fraction, tuple) or isinstance(fraction,list):
        for num in fraction:
            if not isinstance(num,str):
                raise TypeError('nums in the fraction tuple or list must be a string')
        fraction = list(fraction)

    # If len is 1
    if len(fraction) == 1 and (isinstance(fraction,list) or isinstance(fraction,tuple)):
        num = fraction[0]
        int(float(num))
        if num[-1] == '.':
            return num[:-1]
        else:
            return num
    if len(fraction) == 1:
        num = ''.join(fraction)
        try:
            int(float(num))
        except NameError:
            raise TypeError('the fraction must be a number')
        if '.' in num:
            index = num.index('.')
        try:
            num[index+1]
        except IndexError:
            return num[:-1]
        else:
            return ''.join(fraction)

    # Test for each num in frac to be an int
    for num in fraction:
        try:
            int(float(num))
        except NameError:
            raise TypeError('the 2 numbers left and right of the slash must be a number')

    # Watch out for zeros
    if fraction[1] == '0':
        num = int(fraction[0])
        num/0
    if fraction[0] == '0':
        return '0'

    counter = -1

    # Remove any decimals in the fraction
    
    for num in fraction:
        num = str(num)
        counter += 1
        if '.' in num:
            if '.5' in num:
                if num[len(num)-2] == '.5':
                    num1,num2 = float(fraction[0]),float(fraction[1])
                    num1 *= 2
                    num2 *= 2
                    fraction[0],fraction[1] = num1,num2
            elif '.2' in num:
                if num[len(num)-2:] == '.2':
                    num1,num2 = float(fraction[0]),float(fraction[1])
                    num1 *= 5
                    num2 *= 5
                    fraction[0],fraction[1] = num1,num2
            else:
                if num[-1] == '.':
                    fraction[counter] = num[:-1]
                else:
                    index = num.index('.')
                    a_len = len(num[index+1:])
                    num1,num2 = float(fraction[0]),float(fraction[1])
                    num1 *= pow(10,a_len)
                    num2 *= pow(10,a_len)
                    fraction[0],fraction[1] = num1,num2
    fraction = [int(x) for x in fraction]
    
    # The simplifying part   
    from math import gcd

    while True:
        the_gcd = gcd(int(fraction[0]), int(fraction[1]))
        if the_gcd == 1:
            if fraction[1] == 1:
                return str(fraction[0])
            else:
                end = [str(int(num)) for num in fraction]
                return '/'.join(end)
        else:
            fraction = [x/the_gcd for x in fraction]
            continue

# Tests
if __name__ == '__main__':
    import unittest

    class test(unittest.TestCase):

        def test_wrong_input_type(self):
            pass # All with passes are done
        @unittest.expectedFailure
        def test_wrong_input_2(self):
            simplify('988k')
        @unittest.expectedFailure
        def test_wrong_input_3(self):
            simplify('9i3/9')
        @unittest.expectedFailure
        def test_wrong_input_4(self):
            simplify('385/6k3.')

        @unittest.expectedFailure
        def test_div_by_zero(self):
            simplify('1/0')
        def test_with_zero_2(self):
            self.assertEqual(simplify('0/8'), '0')
        @unittest.expectedFailure
        def test_with_two_zeros(self):
            simplify('0/0')


        def test_point(self):
            self.assertEqual(simplify('4/96.'), '1/24')
        def test_point2(self):
            self.assertEqual(simplify('4./96'),'1/24')
        def test_point3(self):
            self.assertEqual(simplify('4./96.'),'1/24')
        
        def test_normal(self):
            self.assertEqual(simplify('13/'+str(13*195)),'1/195')
        def test_decimal(self):
            self.assertEqual(simplify(str(6.9*2)+'/'+str(6.9*31)),'2/31')

        def test_iter(self):
            self.assertEqual(simplify(('8','96')),'1/12')
        def test_iter(self):
            self.assertEqual(simplify(['8','96']),'1/12')
    
        def test_whitespace(self):
            self.assertEqual(simplify('  8     / 96    '),'1/12')
        def test_whitespace2(self):
            self.assertEqual(simplify('     8   / 96        '),'1/12')
        def test_whitespace3(self):
            self.assertEqual(simplify('       8     /      96  '),'1/12')
    unittest.main()

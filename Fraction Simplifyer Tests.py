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

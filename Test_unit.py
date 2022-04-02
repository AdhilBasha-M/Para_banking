import unittest
import customer
from customer import bills



class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = 0
        b= bills.b
        self.assertEquals(a,b)

    def test_2(self):
        final = bills.final
        disc = bills.disc
        ct = bills.ct

        if disc == "PI":
            self.assertEquals(final, ct - (ct / 5))

        if disc == "GD":
            self.assertEquals(final, ct - (ct / 10))

        if disc == "SI":
            self.assertEquals(final, ct - (ct / 20))



if __name__ == '__main__':
    unittest.main()

import unittest
from flask_testing import TestCase
from math import ceil
from index import app

def result(credit, first_pay, years):

    rule = ceil(credit * 0.2)
    maxi = ceil(credit * 0.7)
    note = ''
    color = "alert-success"

    if(maxi >= first_pay >= rule):
        note = 'Расчет проведен верно'
        percent = 0.0075
        k = (percent * (1 + percent) ** (years * 12)) / ((1 + percent) ** (years * 12) - 1)
        monthly_payment = ceil((credit - first_pay) * k) - 10000

        timeline = years
        summa = credit
        payment_f = first_pay

        return monthly_payment

    if(first_pay >=  maxi):
        note = ('Первоначальный платеж должен быть\nне БОЛЕЕ ') + str(maxi) + ' рублей'
        color = "alert-danger"

        timeline = years
        summa = credit
        payment_f = first_pay

        monthly_payment = -1

        return note

    else:
        note = ('Первоначальный платеж должен быть\nне МЕНЕЕ ')+str(rule)+' рублей'
        color = "alert-warning"

        timeline = years
        summa = credit
        payment_f = first_pay

        monthly_payment = -1

        return note

class MyTestCase(unittest.TestCase):

    def create_app(self):
        app.config["TEST"] = True
        return app

    def test_1_normal_data(self):
        self.assertEqual(result(6000000, 1700000, 6), 67510)

    def test_2_low_first_payment(self):
        self.assertTrue("не МЕНЕЕ" in result(6000000, -10101, 6))

    def test_3_high_first_payment(self):
        self.assertTrue("не БОЛЕЕ" in result(6000000, 99999999999, 6))



if __name__ == '__main__':
    unittest.main()

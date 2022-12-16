import unittest

class UnitTests(unittest.TestCase):

    def test_emp_name_salary(self):
        # Failure message:
        # This test has no failure messages
        emp = Employee("Javert", 38000.00)
        self.assertEqual(emp.get_name(), "Javert")
        self.assertEqual(emp.get_salary(), 38000.00)

    def test_sr_emp_name_salary(self):
        # Failure message:
        # This test has no failure messages
        emp = SeniorEmployee("Val Jean", 12000.00)
        self.assertEqual(emp.get_name(), "Val Jean")
        self.assertEqual(emp.get_salary(), 12000.00)

    def test_emp_gross(self):
        # Failure message:
        # This test has no failure messages
        emp = Employee("Javert", 38000.00)
        self.assertAlmostEqual(emp.gross_monthly_pay(), 3166.6666666666665)

    def test_sr_emp_gross(self):
        # Failure message:
        # This test has no failure messages
        emp = SeniorEmployee("Val Jean", 12000.00)
        self.assertAlmostEqual(emp.gross_monthly_pay(), 1500)
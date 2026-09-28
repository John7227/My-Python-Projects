import unittest

from multi_fuel_dispenser_system.multi_fuel_dispenser_system import Multi_fuel_dispenser_system

class TestMultiFuelDispenserSystem(unittest.TestCase):
    def setUp(self):
        self.my_dispenser_system = Multi_fuel_dispenser_system("Kerosene")


    def test_that_when_a_valid_fuel_is_entered_it_displays_the_amount_for_the_fuel(self):

        self.assertEqual(650, self.my_dispenser_system.get_price("Petrol"))
        self.assertEqual(720, self.my_dispenser_system.get_price("Diesel"))
        self.assertEqual(550, self.my_dispenser_system.get_price("Kerosene"))
        self.assertEqual(480, self.my_dispenser_system.get_price("Gas"))


    def test_that_when_a_wrong_fuel_name_is_entered_it_throws_Illegal_error(self):

        self.assertRaises(ValueError, self.my_dispenser_system.get_price, "Keroseneeee")

    def test_that_when_I_enter_liters_of_fuel_it_calculates_the_cost(self):

        self.assertEqual(1100, self.my_dispenser_system.calculate_cost("Kerosene", 2))

    def test_that_when_the_liter_is_below_1_or_above_50_it_throws_Illegal_error(self):

        self.assertRaises(ValueError, self.my_dispenser_system.calculate_cost, "Kerosene", -5)
        self.assertRaises(ValueError, self.my_dispenser_system.calculate_cost, "Kerosene", 99)

    def test_that_liters_are_calculated_based_on_price_and_budget(self):

        self.assertEqual(2, self.my_dispenser_system.calculate_liter(1100, 550))

    def test_that_invalid_amount_to_spend_and_the_amount_of_liter_throws_Illegal_error(self):

        self.assertRaises(ValueError, self.my_dispenser_system.calculate_liter, 400, 550)


if __name__ == '__main__':
    unittest.main()
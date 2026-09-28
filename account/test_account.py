import unittest

from account.account import Account

class TestAccount(unittest.TestCase):
    def test_that_account_can_be_created(self):
        acc = Account("Bolu")
        self.assertEqual(acc.balance, 0)
        self.assertEqual(acc.name, "bolu")

    def test_that_account_can_receive_deposit(self):
        acc = Account("bolu")
        acc.deposit(2500)
        self.assertEqual(acc.balance, 2500)# add assertion here

    def test_that_account_cannot_receive_negative_amount(self):
        acc = Account("bolu")
        self.assertRaises(ValueError, acc.deposit, -2500)

    def test_that_account_can_withdraw_successfully(self):
        acc = Account("bolu")
        acc.deposit(2500)
        acc.withdraw(2000)
        self.assertEqual(acc.balance, 500)

    def test_that_account_can_withdraw_and_it_does_not_allow_amount_greater_than_the_balance(self):
        acc = Account("bolu")
        acc.deposit(2500)
        self.assertRaises(ValueError, acc.withdraw, 5000)

    def test_that_account_can_withdraw_and_it_does_not_allow_negative_amount(self):
        acc = Account("bolu")
        acc.deposit(2500)
        self.assertRaises(ValueError, acc.withdraw, -5000)


if __name__ == '__main__':
    unittest.main()

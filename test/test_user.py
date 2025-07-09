import unittest, os
from faker import Faker

from src import user
from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):

    def setUp(self):
        self.faker = Faker(locale='es_ES')
        self.user = User(self.faker.name(), self.faker.email())
        
    def test_user_creation(self):
        name = self.faker.name()
        email = self.faker.email()
        user = User(name, email)
        #print(user.name, user.email)
        
        self.assertEqual(user.name, name, "El nombre del usuario no es correcto")
        self.assertEqual(user.email, email, "El email del usuario no es correcto")
        self.assertEqual(user.accounts, [], "La lista de cuentas del usuario no está vacía al crear el usuario")

    def test_user_with_multiple_accounts(self):
        for i in range(3):
            account = BankAccount(
                balance=self.faker.pyfloat(left_digits=5, right_digits=2, positive=True),
                log_file=self.faker.file_name(extension='txt'))
            self.user.add_account(account)
        
        self.assertEqual(self.user.get_total_balance(), sum(account.get_balance() for account in self.user.accounts), 
                         "El saldo total del usuario no es correcto al tener múltiples cuentas")
        
    def tearDown(self):
        for account in self.user.accounts:
            if account.log_file and os.path.exists(account.log_file):
                os.remove(account.log_file)
import unittest
from unittest.mock import patch
import os
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self):
        #Se usa siempre antes de ejecutar una prueba
        # setUp se usa para inicializar las variables necesarias para las pruebas
        # sin generar duplicidad de código
        self.account1 = BankAccount(balance=1000, log_file="test_log_cta1.txt")
        self.account2 = BankAccount(balance=2000, log_file="test_log_cta2.txt")

    def tearDown(self):
        #Se usa siempre después de ejecutar una prueba
        # tearDown se usa para limpiar las variables necesarias para las pruebas
        # sin generar duplicidad de código
        if os.path.exists(self.account1.log_file):
            os.remove(self.account1.log_file)
        if os.path.exists(self.account2.log_file):
            os.remove(self.account2.log_file)

    def _count_lines(self, file_path):
        """Helper method to count lines in a file."""
        with open(file_path, 'r') as f:
            return len(f.readlines())

    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.get_balance(), 1500, "El saldo no es correcto después del depósito")

    # def test_withdraw(self):
    #     self.account1.withdraw(200)
    #     self.assertEqual(self.account1.get_balance(), 800, "El saldo no es correcto después de la retirada")

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        self.account1.withdraw(100)
        self.assertEqual(self.account1.get_balance(), 900, "El saldo no es correcto después de la retirada durante horas permitidas")

    @patch("src.bank_account.datetime")
    def test_withdraw_disable_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account1.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disable_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account1.withdraw(100)

    # def test_withdraw_insufficient_funds(self):
    #     with self.assertRaises(ValueError):
    #         self.account1.withdraw(2000)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(-100)

    def test_get_balance(self):
        self.assertEqual(self.account1.get_balance(), 1000, "El saldo no es correcto al obtener el balance")

    # def test_transfer(self):
    #     self.account1.transfer(300, self.account2)
    #     self.assertEqual(self.account1.get_balance(), 700, "El saldo no es correcto después de realizar la transferencia")
    #     self.assertEqual(self.account2.get_balance(), 2300, "El saldo no es correcto después de recibir una transferencia")

    def test_transaction_log(self):
        # Verifica que se crea un archivo de log
        self.assertTrue(os.path.exists("test_log_cta1.txt"))
        self.assertTrue(os.path.exists("test_log_cta2.txt")) #verifica el archivo de log existe

    def test_count_transactions(self):
        # Verifica que se registran las transacciones en el archivo de log
        self.assertEqual(self._count_lines(self.account1.log_file), 1, "El número de transacciones en el log de la cuenta 1 no es correcto")
        self.assertEqual(self._count_lines(self.account2.log_file), 1, "El número de transacciones en el log de la cuenta 2 no es correcto")
        self.account1.deposit(100)
        self.assertEqual(self._count_lines(self.account1.log_file), 2, "El número de transacciones en el log de la cuenta 1 no es correcto después del depósito")
        self.assertEqual(self._count_lines(self.account2.log_file), 1, "El número de transacciones en el log de la cuenta 2 no es correcto después del depósito")

    def test_deposit_varios_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected_balance": 1100},
            {"ammount": 3000, "expected_balance": 4100},
            {"ammount": 4500, "expected_balance": 8600}
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account1.deposit(case["ammount"])
                self.assertEqual(self.account1.get_balance(), case["expected_balance"])

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.assertEqual(self.account1.deposit(-100), "El monto del depósito debe ser positivo")
    
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.assertEqual(self.account1.deposit(0), "El monto del depósito debe ser positivo")

    # def test_withdraw_negative_amount(self):
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(self.account1.withdraw(-100), "El monto de la retirada debe ser positivo")

    # def test_withdraw_amount_greater_than_balance(self):
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(self.account1.withdraw(2000), "Fondos insuficientes para la retirada")



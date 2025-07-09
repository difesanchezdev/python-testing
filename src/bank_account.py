from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance: float = 0.0, log_file: str = None) -> None:
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message: str) -> None:
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        else:
            self.balance += amount
            self._log_transaction(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed between 8 AM and 5 PM.")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        elif amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            self._log_transaction(f"Withdrew: {amount}. New balance: {self.balance}")

    def transfer(self, amount: float, target_account: "BankAccount") -> None:
        self.withdraw(amount)
        target_account.deposit(amount)
        self._log_transaction(f"Transferred: {amount} to {target_account.log_file}. New balance: {self.balance}")


    def get_balance(self) -> float:
        self._log_transaction(f"Checked balance: {self.balance}")
        return self.balance
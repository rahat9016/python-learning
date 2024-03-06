from bank_account import *

Rahat = BankAccount(1000, 'Rahat')
Minhajur = BankAccount(2000, 'Minhajur')

Rahat.getBalance()
Minhajur.getBalance()


Rahat.deposit(500)

Rahat.withdraw(465)

Rahat.transfer(1000, Minhajur)
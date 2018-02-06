balance = 3558
annualInterestRate = 0.15
monthlyInterestRate = annualInterestRate/12
a=balance
monthlyFixedPayment = 0
while balance > 0:
	balance = a
	monthlyFixedPayment += 10
	for month in range(12):
		balance -= monthlyFixedPayment
		balance += balance*monthlyInterestRate
print('Lowest Payment:',monthlyFixedPayment)

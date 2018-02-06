balance= 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
monthlyInterestRate = annualInterestRate/12.0
i=12
while i > 0:	
	min = monthlyPaymentRate*balance	
	unpaidBalance = balance - min
	interest = monthlyInterestRate*unpaidBalance
	balance = (unpaidBalance + interest)
	i-=1
print('Remaining Balance: ',round(balance,2))

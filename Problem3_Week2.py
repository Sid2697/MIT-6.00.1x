balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
a = balance
lo = balance / 12.0
hi = balance * (1 + monthlyInterestRate) ** 12 / 12.0
monthlyPayment = round((lo + hi) / 2, 2)
while True:
    monthlyPayment = round((lo + hi) / 2, 2)
    a = balance
    for month in range(12):
        a -= monthlyPayment
        a += a * monthlyInterestRate
    if abs(a - 0.01) < 0.1:
        print ('Lowest Payment:',monthlyPayment)
        break
    elif a < 0:
        hi = monthlyPayment
        monthlyPayment = round((lo + hi) / 2, 2)
    else:
        lo = monthlyPayment
        monthlyPayment = round((lo + hi) / 2, 2)

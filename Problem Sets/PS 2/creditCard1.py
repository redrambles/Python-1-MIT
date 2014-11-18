 
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for num in range(1, 13): # For 12 months

    monthlyPayment = round((balance) * (monthlyPaymentRate),2)
    newbalance = round((balance) - monthlyPayment,2)
    balanceAndinterest = round(((newbalance) + ((annualInterestRate * (newbalance))/12)),2)
    totalPaid += round(monthlyPayment, 2)

    print 'Month: ' + str(num)
    print 'Minimum monthly payment: ' + str(monthlyPayment)
    print 'Remaining balance: ' + str(balanceAndinterest)

    balance = balanceAndinterest

print 'Total paid: ' + str(totalPaid)
print 'Remaining balance: ' + str(balanceAndinterest)
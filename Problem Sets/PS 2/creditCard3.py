balance = 320000
annualInterestRate = 0.2
original = balance
monthlyInterestRate = (annualInterestRate) / 12.0
low = balance / 12
high = (balance * ((1 + monthlyInterestRate)**12)) / 12.0
ans = round((low + high)/2, 2)
epsilon = 0.01

while balance > 0:

        
    for num in range(1, 13):
            
        newbalance = balance - ans
        balanceAndinterest = newbalance + round(((annualInterestRate * (newbalance))/12),2)
        balance = balanceAndinterest
        
    if  round(balance,2) == epsilon:
        break

    elif round(balance,2) > epsilon:
        low = ans
        ans = (low + high)/2
        balance = original
        num = 1
        
    elif round(balance,2) < epsilon:
        high = ans
        ans = (low + high)/2
        balance = original
        num = 1
    
        
print 'Lowest Payment:',
print round(ans,2)
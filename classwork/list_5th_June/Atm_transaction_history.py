#program to calculate withdrawals and deposits 
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Empty lists to store deposits and withdrawals separately
deposits = []
withdrawals = []

# Variable to keep track of current balance
current_balance = 0

# Separate deposits and withdrawals
# Also calculate current balance
for i in transactions:

    # Check for deposit
    if i > 0:
        deposits.append(i)

    # Check for withdrawal
    if i < 0:
        withdrawals.append(i)

    # Add transaction amount to balance
    current_balance += i

# Assume first withdrawal is the largest withdrawal
max_withdrawals = withdrawals[0]

# Assume first deposit is the largest deposit
max_deposits = deposits[0]

# Find the largest withdrawal
# (Most negative value)
for i in range(len(withdrawals)):
    if max_withdrawals > withdrawals[i]:
        max_withdrawals = withdrawals[i]

# Find the largest deposit
for i in range(len(deposits)):
    if max_deposits < deposits[i]:
        max_deposits = deposits[i]

# Display results
print("Current Balance:", current_balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", max_deposits)
print("Largest Withdrawal:", max_withdrawals)

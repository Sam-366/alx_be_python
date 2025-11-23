# 1. User Input for Financial Details
try:
    # Use float() to allow for decimal amounts (cents)
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
except ValueError:
    print("Invalid input. Please enter numerical values for income and expenses.")
    exit()

# 2. Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# 3. Project Annual Savings Calculation
ANNUAL_INTEREST_RATE = 0.05
MONTHS_IN_YEAR = 12

# Calculate the total principal saved over a year (Monthly Savings * 12)
annual_principal = monthly_savings * MONTHS_IN_YEAR

# Calculate the interest earned on the annual principal (Annual Principal * Rate)
annual_interest_earned = annual_principal * ANNUAL_INTEREST_RATE

# Calculate the projected savings after one year with interest
# Formula: Projected Savings = Annual Principal + Annual Interest Earned
projected_savings = annual_principal + annual_interest_earned

# Format the results for currency display (2 decimal places)
monthly_savings_formatted = f"${monthly_savings:,.2f}"
projected_savings_formatted = f"${projected_savings:,.2f}"

# 4. Output Results
print(f"Your monthly savings are {monthly_savings_formatted}.")
print(f"Projected savings after one year, with interest, is: {projected_savings_formatted}.")


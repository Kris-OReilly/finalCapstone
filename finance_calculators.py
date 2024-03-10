import math

# The two options for the user to choose from are printed and then user is asked to input an option

print(" Investment - to calculate the amount of interest you will earn on your investment \n \
      Bond - to calculate the monthly amount you'll have to pay on a home loan \n")

options = input(" Enter either 'investment' or 'bond' from the menu above to proceed: ")

# If the user chooses investment they will be asked to input the deposit amount, the interest rate
# and the number of years of investment
# These will be save inside variables

if options.lower() == "investment":
    deposit = int(input(" Please enter your deposit amount (£): "))
    interest_rate = float(input(" Please enter the interest rate (%) amount: "))/100
    investment_years = int(input(" Enter number of years you will be investing for: "))

# Declaring variables defining the formulas for simple and compound interest

    simple_interest = deposit *(1 + interest_rate*investment_years)
    compound_interest = deposit * math.pow((1 + interest_rate), investment_years)

# Asking the user to input either simple or compound interest to be calculated
# Print the relevant value stating the initial deposit, the interest rate and the length of investment.
# An error message will appear if simple or compound is not entered

    interest = input(" Enter 'simple' or 'compound' for your chosen interest type: ")

    if interest.lower() == "simple":
        print(f"Your return on £{deposit} investment, at {interest_rate*100}% interest over {investment_years} years will be: £{simple_interest:.2f} ")  
    elif interest.lower() == "compound":
        print(f"Your return on £{deposit} investment, at {interest_rate*100}% interest over {investment_years} years will be: £{compound_interest:.2f} ")
    else:
        print(" ~ ERROR ~ you entered an invalid interest option")


# If the user chooses bond they will be asked to input the current house value, the interest rate
# and the number of months the plan will take to repay

elif options.lower() == "bond":
    home_value = int(input(" Please enter current home value: "))
    bond_interest = (float(input(" Enter the interest rate: "))/100)/12
    repayment_time = int(input(" Enter length of repayment plan in months: "))

# Declaring the repayment variable and defining the formula for calculation

    bond_repayment = (bond_interest * home_value) / (1 - (1 + bond_interest)**(-repayment_time))
    bond_amount = f"{bond_repayment:.2f}"    # formats the amount to 2 decimal places

# Print the monthly bond repayment amount
    print(f" Your monthly repayment amount is: £{bond_amount}")

# If the user enters an invalid option and error message will appear

else:
    print(" ~ERROR~ You entered an incorrect option.")
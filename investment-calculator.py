print("=" * 50)
print("INVESTMENT CALCULATOR")
print("Discover the Power of Compound Interest")
print("=" * 50)
print()

# STEP 1: Get user input
monthly_investment = float(input("How much can you invest per month? $"))
years = int(input("For how many years? "))
annual_return = float(input("Expected annual return rate? (e.g., 8 for 8%): "))

print(f"\nYou entered:")
print(f"Monthly: ${monthly_investment}")
print(f"Years: {years}")
print(f"Return: {annual_return}%")

monthly_return = annual_return / 100 / 12
total_months = years * 12
future_value = monthly_investment * (((1 + monthly_return) ** total_months - 1) / monthly_return)

print("\n Calculations")
print ("-" * 40)

total_investment = monthly_investment * total_months
earnings = future_value - total_investment
total_return_percentage = (earnings / total_investment) * 100

print(f"Your total investment is ${round (total_investment, 2)}")
print(f"Your profit was ${round (earnings, 2)}")
print(f"Your return percentage on your original investment was {round (total_return_percentage, 2) } %")

print("-" * 40)
print("\n ADVICE")
print("-" * 40)

if monthly_investment < 50:
    print("Be careful with your investments and put them in the right place, because if you do, you will definetely multiply your net worth and money")
elif monthly_investment < 100:
    print("Aim to grow your investment portfolio, while also investing in ETFs and Index Funds to minimize loss and maximize long term gain")
else:
    print("Keep your portfolio very diversified, so if a certain industry or company takes a loss, you can still maintain most of your portfolio. Also don't put all your money into volatile stocks")

print ("-" * 40)
print("\n WHAT IF SCENARIOS") 
print("-" * 40)

print("Scenario 1: Investing 10 extra dollars a month")
print("-" * 40)

new_future_value = (monthly_investment + 10) * (((1 + monthly_return) ** total_months - 1) / monthly_return)
potential = new_future_value - future_value
print (f"Your investment portfolio would have been worth ${round (potential, 2)} more if you had invested 10 more dollars a month.")

print("Scenario 2: Investing 25 extra dollars a month")
print("-" * 40)

super_new_future_value = (monthly_investment + 25) * (((1 + monthly_return) ** total_months - 1) / monthly_return)
super_potential = super_new_future_value - future_value
print (f"Your investment portfolio would have been worth ${round (super_potential, 2)} more if you had invested 25 more dollars a month.")


print("Scenario 3: Starting 5 years earlier")
print("-" * 40)

new_months = total_months + 60
another_future_value = monthly_investment * (((1 + monthly_return) ** new_months - 1) / monthly_return)
another_potential = another_future_value - future_value

print (f"Your investment portfolio would have been worth ${round (another_potential, 2)} more if you had started 5 years earlier.")

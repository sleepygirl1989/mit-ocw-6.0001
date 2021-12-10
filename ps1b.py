import math

annual_salary = float(input("Enter your salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost= float(input("Enter the cost of your dream home: "))
raise_salary = float(input("Enter the semi-annual raise, as a decimal: "))


portion_down_payment = 0.25 *total_cost
current_savings=0

monthly_savings = (annual_salary / 12) * portion_saved
number_of_months = 0
while current_savings < portion_down_payment:
    current_savings += monthly_savings + ((current_savings * 0.04) / 12)
    number_of_months += 1
    if (number_of_months % 6 == 0):
        annual_salary += annual_salary*raise_salary
        mmonthly_savings = (annual_salary / 12) * portion_saved

print("Number of months = " + str(number_of_months))



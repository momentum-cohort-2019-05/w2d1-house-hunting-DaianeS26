total_cost = int(input("Cost of your dream home?"))
annual_salary = int(input("Annual Salary?"))
portion_saved = float(input ("How much are you saving?"))

portion_downpayment = 0.25
total_downpayment = total_cost * portion_downpayment
current_savings = 0 
r = 0.04
monthly_salary = (annual_salary/ 12.0)
monthly_savings = ((annual_salary/12)* portion_saved) + current_savings * r/12

months= 0

while (current_savings <= total_downpayment):
    monthly_savings = ((annual_salary/12)* portion_saved) + current_savings * r/12
    current_savings = current_savings + monthly_savings
    months = months + 1
print ('It will take {} months to save!'.format(months))






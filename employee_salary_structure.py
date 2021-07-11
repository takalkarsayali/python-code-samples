#Assignment No.1: to Calculate Salary of the Employee

Basic_pay = int(input("Enter basic pay of employee: "))

h = int(input("Enter the percent of HRA of Basic pay: "))
HRA = (h/100)*Basic_pay

t = int(input("Enter the percent of TA of Basic pay: "))
TA = (t/100)*Basic_pay

total_salary = Basic_pay + HRA + TA

print("Total Salary = "+str(total_salary))
p = int(input("Enter the percent of Professional Tax of Total salary : "))

professional_tax = (p/100)*total_salary
print("Professional Tax = "+str(professional_tax))

gross_Salary = total_salary - professional_tax
print("Gross Salary = "+str(gross_Salary))


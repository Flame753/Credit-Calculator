from math import ceil

print("Enter the credit principal:")
principal = int(input())
print("What do you want to calculate:")
print('type "m" - for count fo months,')
print('type "p" - for monthly payment:')
choose = input()
if choose == "m":
    print("Enter monthly payment:")
    payment = int(input())
    print()
    months = ceil(principal / payment)
    print(f"It takes {months} month to repay the credit")
elif choose == "p":
    print("Enter count of months:")
    months = int(input())
    print()
    payment = ceil(principal / months)
    last_payment = principal - (months - 1) * payment
    print(f"Your monthly payment = {payment} with last month payment = {last_payment}.")

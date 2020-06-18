from math import ceil, log

"""
A or a = annuity payment

P or p = Credit principal.

i = nominal (monthly) interest rate.

n = Number of payments. Usually, it’s the count of months.
"""


def find_months(p, a, i):
    """ Number of payments. Usually, it's the count of months."""
    i = i / 100
    i = i/(12 * 1)  # Given credit interest is divide by 12 months and 100%
    n = log(a/(a - i * p), 1 + i)
    return ceil(n)


def find_annuity_payment(p, n, i):
    i = i / 100
    i = i / (12 * 1)
    nominator = i * pow(1 + i, n)
    denominator = pow(1 + i, n) - 1
    a = p * nominator / denominator
    return ceil(a)


def find_principal(a, n, i):
    i = i / 100
    i = i / (12 * 1)
    nominator = i * pow(1 + i, n)
    denominator = pow(1 + i, n) - 1
    a = a / (nominator / denominator)
    return a


def menu():
    print("What do you want to calculate:")
    print('type "n" - for count fo months,')
    print('type "a" - for annuity monthly payment:')
    print('type "p" - for credit principal:')
    return input()


choose = menu()
if choose == "n":
    principal = float(input("Enter the credit principal: "))
    payment = float(input("Enter monthly payment: "))
    interest = float(input("Enter credit interest: "))
    months = find_months(principal, payment, interest)
    years = months // 12
    months = months % 12
    if years == 0:
        if months == 1:
            print(f"It takes {months} month to repay the credit")
        else:
            print(f"It takes {months} months to repay the credit")
    elif months == 0:
        if years == 1:
            print(f"It takes {years} year to repay the credit")
        else:
            print(f"It takes {years} years to repay the credit")
    else:
        if years == 1 and months == 1:
            print(f"It takes {years} year and {months} month to repay the credit")
        elif years > 1 and months == 1:
            print(f"It takes {years} years and {months} month to repay the credit")
        elif years == 1 and months > 1:
            print(f"It takes {years} year and {months} months to repay the credit")
        else:
            print(f"It takes {years} years and {months} months to repay the credit")
elif choose == "a":
    principal = float(input("Enter the credit principal: "))
    months = int(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    payment = find_annuity_payment(principal, months, interest)
    print(f"Your annuity payment = {payment}!")
elif choose == "p":
    payment = float(input("Enter monthly payment: "))
    months = int(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    principal = find_principal(payment, months, interest)
    print(f"Your credit principal = {principal}!")
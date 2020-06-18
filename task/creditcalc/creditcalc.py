from math import ceil, log

"""
A = annuity payment

P = Credit principal.

i = nominal (monthly) interest rate.

n = Number of payments. Usually, it’s the count of months.
"""


def find_months(P, A, i):
    """ Number of payments. Usually, it's the count of months."""
    i = i / 100
    i = i/(12 * 1)  # Given credit interest is divide by 12 months and 100%
    n = log(A/(A - i * P), 1 + i)
    return ceil(n)


def find_annuity_payment(P, n, i):
    i = i / 100
    nominator = i * pow(1 + i, n)
    denominator = pow(1 + i, n) - 1
    A = P * nominator / denominator
    return A


def find_principal(A, n, i):
    i = i / 100
    nominator = i * pow(1 + i, n)
    denominator = pow(1 + i, n) - 1
    P = A / nominator / denominator
    return P


print("What do you want to calculate:")
print('type "n" - for count fo months,')
print('type "a" - for annuity monthly payment:')
print('type "p" - for credit principal:')
choose = input()

if choose == "n":
    print("Enter the credit principal:")
    principal = int(input())
    print("Enter monthly payment:")
    payment = int(input())
    print('Enter credit interest:')
    interest = int(input())
    months = find_months(principal, payment, interest)
    years = months // 12
    months = months % 12
    if years == 0:
        print(f"It takes {months} months to repay the credit")
    elif months == 0:
        print(f"It takes {years} years to repay the credit")
    else:
        print(f"It takes {years} years and {months} months to repay the credit")
elif choose == "a":
    pass
elif choose == "p":
    print("Enter count of months:")
    months = int(input())
    print()
    payment = ceil(principal / months)
    last_payment = principal - (months - 1) * payment
    print(f"Your monthly payment = {payment} with last month payment = {last_payment}.")

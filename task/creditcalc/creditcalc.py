# D or d = mth differentiated payment
# A or a = annuity payment
# P or p = Credit principal.
# i = nominal (monthly) interest rate.
# n = Number of payments. Usually, it's the count of months
# m = current period

from math import ceil, log
import argparse

#  Initialize the parser
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str, choices=["diff", "annuity"],
                    help="what is being calculated")
parser.add_argument("-pri", "--principal", type=float,
                    help="a sum of money lent")
parser.add_argument("-pay", "--payment", type=float,
                    help="money that is being returned")
parser.add_argument("-per", "--periods", type=int,
                    help="the monthly cycle of payments")
parser.add_argument("-i", "--interest", type=float,
                    help="nominal (monthly) interest rate")
args = parser.parse_args()


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


def find_diff_payment(p, i, n, m):
    i = i / (100 * 12)
    d = (p/n) + i * (p - (p * (m-1) / n))
    return int(ceil(d))


def print_over_payment(p, sum_diff_pay):
    print("Overpayment = {}".format(int(ceil(sum_diff_pay - p))))


def menu():
    print("What do you want to calculate:")
    print('type "n" - for count of months,')
    print('type "a" - for annuity monthly payment:')
    print('type "p" - for credit principal:')
    print('type "d" - differentiated payment')
    return input()


def print_how_long(month, year):
    if year == 0:
        if month == 1:
            print("It takes 1 month to repay the credit!")
        else:
            print("It takes {} months to repay the credit!".format(month))
    elif month == 0:
        if year == 1:
            print("It takes 1 year to repay the credit!")
        else:
            print("It takes {} years to repay the credit!".format(year))
    else:
        if year == 1 and month == 1:
            print("It takes 1 year and 1 month to repay the credit!")
        elif year > 1 and month == 1:
            print("It takes {} years and 1 month to repay the credit!".format(year))
        elif year == 1 and month > 1:
            print("It takes 1 year and {} months to repay the credit!".format(month))
        else:
            print("It takes {} years and {} months to repay the credit!".format(year, month))


total = 0
if args.interest:
    if args.type == "diff" and not args.payment:
        for month in range(1, args.periods+1):
            diff_payment = find_diff_payment(p=args.principal, i=args.interest, n=args.periods, m=month)
            print("Month {0}: paid out {1}".format(month, diff_payment))
            total += diff_payment
        print_over_payment(args.principal, total)

    elif args.type == "annuity":
        if args.principal and args.payment:
            # Finding count of months (n)
            many_months = find_months(args.principal, args.payment, args.interest)
            years = int(many_months // 12)
            months = int(many_months % 12)
            print_how_long(months, years)
            print_over_payment(args.principal, many_months * args.payment)

        elif args.principal and args.periods:
            # Find the annuity payment (a)
            payment = int(find_annuity_payment(args.principal, args.periods, args.interest))
            print("Your annuity payment = {}!".format(payment))
            print_over_payment(args.principal, args.periods * payment)
        elif args.payment and args.periods:
            # Find the principal (p)
            principal = int(find_principal(args.payment, args.periods, args.interest))
            print("Your credit principal = {}!".format(principal))
            print_over_payment(principal, args.periods * args.payment)
else:
    print("Incorrect parameters")


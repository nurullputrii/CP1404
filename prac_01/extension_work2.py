""" TARIFF_11 = 0.244618
TARIFF_31 = 0.136928 """

# price_in_cents = int(input("enter the price in cents: "))
daily_in_kwh = float(input("enter daily use in kwh: "))
billing_days = int(input("enter number of billing days: "))
tariff_input = int(input("tariff 11 or 31? "))
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
if tariff_input == 11:
    calculate = (daily_in_kwh * billing_days * TARIFF_11)/100
    print(round(calculate, 2))
elif tariff_input == 31:
    calculate = (daily_in_kwh * billing_days * TARIFF_31)/100
    print(round(calculate, 2))
else:
    print("Invalid input")

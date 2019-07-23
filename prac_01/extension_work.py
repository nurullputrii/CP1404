# electricity bill estimator
# price per kWh in cents
# daily use in Kwh
# number of days billing period
price_in_cents = int(input("enter the price in cents: "))
daily_in_kwh = float(input("enter daily use in kwh: "))
billing_days = int(input("enter number of billing days: "))
calculate = (price_in_cents * daily_in_kwh * billing_days)/100
print(round(calculate, 2))

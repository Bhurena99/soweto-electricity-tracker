# Soweto Electricity Tracker
# Day 2 - Economics + Data

import datetime

print("Soweto Small Business Impact Tracker")
print(f"Date: {datetime.date.today()}")

hours_without_power = 4.5
hourly_revenue = 150
daily_loss = hours_without_power * hourly_revenue

print(f"Hours without power: {hours_without_power}")
print(f"Estimated loss today: R{daily_loss}")
print("Next: Connect to real EskomSePush API")
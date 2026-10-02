# Soweto Electricity Tracker - Day 3
# Author: Bhurena99 | Soweto, SA

import datetime
import csv

print("=== SOWETO SMALL BUSINESS IMPACT TRACKER ===")
print(f"Date: {datetime.date.today()}")
print("Location: Soweto, Gauteng\n")

weekly_loadshedding = {
    "Monday": 4.5,
    "Tuesday": 2.5,
    "Wednesday": 6.0,
    "Thursday": 4.0,
    "Friday": 2.0,
    "Saturday": 0,
    "Sunday": 2.5
}

hourly_revenue = 150
businesses_tracked = 50

total_hours = sum(weekly_loadshedding.values())
total_loss_one = total_hours * hourly_revenue
total_loss_community = total_loss_one * businesses_tracked

print("WEEKLY BREAKDOWN:")
for day, hours in weekly_loadshedding.items():
    print(f"{day}: {hours}h off = R{hours * hourly_revenue} lost")

print(f"\nTotal hours off: {total_hours}h")
print(f"Loss per business: R{total_loss_one}")
print(f"Loss for {businesses_tracked} businesses: R{total_loss_community}")
print(f"Monthly projection: R{total_loss_community * 4}")
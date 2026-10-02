weekly_sales = {
    "North":   14200,
    "South":    9100,
    "East":    16700,
    "West":    10800,
    "Central": 12400,
}

def calculate_total(weekly_sales_dict):
    total = 0
    for sales in weekly_sales_dict.values():
        total = total + sales
    return total

def calculate_average(weekly_sales_dict):
    total = calculate_total(weekly_sales_dict)
    count = len(weekly_sales_dict)
    return total / count

highest_sales = max(weekly_sales, key=weekly_sales.get)
lowest_sales = min(weekly_sales, key=weekly_sales.get)

results = {}

for region, sales in weekly_sales.items():
    is_above_average = sales > calculate_average(weekly_sales) 
    results[region] = is_above_average

def calculate_is_above_average(region):
    if results[region]:
        return "Above Average"
    else:
        return "Below Average"


print("Weekly Sales Report")
print("---------------------")

for region, revenue in weekly_sales.items():
    print(region, ":", revenue, calculate_is_above_average(region))

print()
print("Summary")
print("-------")
print("Total:", calculate_total(weekly_sales))
print("Average:", calculate_average(weekly_sales))
print("Highest Weekly Sales:", highest_sales,  max(weekly_sales.values()))
print("Lowest Weekly Sales:", lowest_sales, min(weekly_sales.values()))


with open("weekly_sales_summary.txt", "w") as f:
    f.write("Weekly Sales Report\n")
    f.write("---------------------\n")
    for region, revenue in weekly_sales.items():
        f.write(f"{region}: {revenue} {calculate_is_above_average(region)}\n")
    f.write("\n")
    f.write(f"Total: {calculate_total(weekly_sales)}\n")
    f.write(f"Average: {calculate_average(weekly_sales)}\n")
    f.write(f"Highest Weekly Sales: {highest_sales} {max(weekly_sales.values())}\n")
    f.write(f"Lowest Weekly Sales: {lowest_sales} {min(weekly_sales.values())}\n")
"""
Working 9 to 5
Write a function that calculates overtime and pay associated with overtime.

Working 9 to 5: regular hours
After 5pm is overtime
Your function gets a list with 4 values:

Start of working day, in decimal format, (24-hour day notation)
End of working day. (Same format)
Hourly rate
Overtime multiplier
Your function should spit out:

$ + earned that day (rounded to the nearest hundreth)
Examples
over_time([9, 17, 30, 1.5]) ➞ "$240.00"

over_time([16, 18, 30, 1.8]) ➞ "$84.00"

over_time([13.25, 15, 30, 1.5]) ➞ "$52.50"
2nd example explained:

From 16 to 17 is regular, so 1 * 30 = 30
From 17 to 18 is overtime, so 1 * 30 * 1.8 = 54
30 + 54 = $84.00
"""
def over_time(lst):

    start, end, rate, overtime_rate = lst
    regular_hours = max(0, min(end, 17) - start)
    overtime_hours = max(0, end - 17)

    if start < 17:
        total_pay = regular_hours * rate + overtime_hours * rate * overtime_rate + 0.001
    else:
        total_pay = (end - start) * rate * overtime_rate
    return "${:,.2f}".format(total_pay)






    # if lst[1] - 17 > 0:
    #     overtime = lst[1] - 17
    #     work_hour = lst[1] - lst[0] - overtime
    # else:
    #     overtime = 0
    #     work_hour = lst[1] - lst[0]
    # return f"${(work_hour * lst[2]) + (overtime * lst[2] * lst[3]):.2f}"

print(over_time([9, 17, 30, 1.5]))
print(over_time([16, 18, 30, 1.8]))
print(over_time([13.25, 15, 30, 1.5]))

print(over_time([18, 20, 32.5, 2]))
print(over_time([10.5, 17, 32.25, 1.5]))
print(over_time([13, 21, 38.6, 1.8]))
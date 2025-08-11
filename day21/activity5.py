employee = "Abi"
hours_worked = 45.75
hourly_rate = 350.50
bonus = 1500
target_hours = 40


#print(f"Employee Name: {employee},Hours Worked: {hours_worked},Target Hours: {target_hours}, Overtime: {hours_worked-target_hours}, Total Pay:{hours_worked*hourly_rate+bonus} ")

print(f"{'*' * 12} Employee Report {'*' * 12}")
print(f"Employee Name:  {' '*15}{employee:}")
print(f"Hours Worked:{' '*17} {hours_worked}")
print(f"Target Hours:{' '*17} {target_hours}")
print(f"Overtime:{' '*21} {hours_worked-target_hours}")
print(f"Total Pay: {hours_worked*hourly_rate+bonus:010.2f}")
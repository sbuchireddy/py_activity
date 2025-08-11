from datetime import datetime
 
def calculate_tenure():
       while True:
        joining_date_str = input("Enter date of joining (YYYY-MM-DD): ")
        try:
            joining_date = datetime.strptime(joining_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
 
    today = datetime.now()
 
    days_completed = (today - joining_date).days
 
    approx_years = days_completed / 365.25  
    remaining_days_for_months = days_completed - (years * 365.25)
    approx_months = remaining_days_for_months / 30.44  
    months = int(approx_months)
 
    print(f"\nDays completed: {days_completed}")
    print(f"Approximate number of years and months: {years} years and {months} months")

calculate_tenure()
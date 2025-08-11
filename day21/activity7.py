import os
def report_location():
	return f"Script is running from: {os.getcwd()}"
print(report_location())

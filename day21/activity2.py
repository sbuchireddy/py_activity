import csv
total = 0.0
with open("data2.csv", newline='') as f:
	reader = csv.DictReader(f)
	for row in reader:
		total = total+float(row["Amount"])
print("total amount:", total)
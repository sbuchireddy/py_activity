invited={"Alice","Bob","Charlie"}
arrived={"Alice","Charlie","Diana"}
unexpected=arrived-invited
if unexpected:
	print(f"unexpected guests arrived,{unexpected}")
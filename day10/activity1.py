fruit_prices={"elppa":100,
"ananab":60,
"egnaro":80}
fruit_name="".join(sorted(input("enter fruit name:")))
sorted_keys=list(map("".join,map(sorted,fruit_prices.keys())))
print(fruit_prices.get(list(fruit_prices.keys())[sorted_keys.index(fruit_name)]))
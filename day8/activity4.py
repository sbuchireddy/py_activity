fruit_prices={"elppa":100,
"ananab":60,
"egnaro":80,
}

fruit=input("enter fruit name:")
print(fruit_prices.get(fruit[::-1],"invalid"))
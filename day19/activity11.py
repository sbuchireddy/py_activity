def append_quote(quote):
    with open("quote.txt", "a") as file:
        file.write(quote + "\n")
 
if __name__ == "__main__":
    quote = input("Enter an inspiring quote: ")
    append_quote(quote)
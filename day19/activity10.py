def write_quote(quote):
    with open("quote.txt", "w") as file:
        file.write(quote)
 
if __name__ == "__main__":
    quote = "the future depends on what you do today"
    write_quote(quote)
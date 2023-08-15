def count_symbols(input_string):
    symbol_count = {}

    for char in input_string:
        if char in symbol_count:
            symbol_count[char] += 1
        else:
            symbol_count[char] = 1

    return symbol_count

prompt = "Hey what is your name and family name? "
user_input = input(prompt)

if len(user_input) == 0:
    print("You need to write your full name!")
else:
    symbol_counts = count_symbols(user_input)
    print("Thank you for that information.")

    for symbol, count in symbol_counts.items():
        print(f"Symbol '{symbol}' was used  {count} times")





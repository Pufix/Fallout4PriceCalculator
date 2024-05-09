def calculate_prices(base_price, charisma):
    buying_price_modifier = max(1.2, -0.15 * charisma + 3.5)
    selling_price_modifier = min(0.8, 1 / buying_price_modifier)
    
    buying_price = base_price * buying_price_modifier
    selling_price = base_price * selling_price_modifier
    
    return buying_price, selling_price

def print_prices(base_price):
    print("Charisma\tBuying Price\tSelling Price")
    print("-----------------------------------------")
    for charisma in range(1, 21):
        buying_price, selling_price = calculate_prices(base_price, charisma)
        print(f"{charisma}\t\t{buying_price:.0f}\t\t{selling_price:.0f}")

# Scanning for base price
base_price = int(input("Enter the base price of the item: "))
print_prices(base_price)

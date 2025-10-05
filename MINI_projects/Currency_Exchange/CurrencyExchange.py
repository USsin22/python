def get_exchange_rate(currency_from, currency_to):
   
    rates = {
        ('USD', 'EUR'): 0.92,
        ('EUR', 'USD'): 1.09,
        ('USD', 'GBP'): 0.78,
        ('GBP', 'USD'): 1.28,
        ('EUR', 'GBP'): 0.85,
        ('GBP', 'EUR'): 1.18,
    }
    return rates.get((currency_from, currency_to), None)

def main():
    print("Welcome to the Currency Exchange!")
    print("Supported currencies: USD, EUR, GBP")
    currency_from = input("Enter the currency you have (e.g., USD): ").upper()
    currency_to = input("Enter the currency you want (e.g., EUR): ").upper()
    amount_str = input(f"Enter the amount in {currency_from}: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount entered.")
        return

    rate = get_exchange_rate(currency_from, currency_to)
    if rate is None:
        print("Exchange rate not available for the selected currencies.")
        return

    exchanged_amount = amount * rate
    print(f"{amount:.2f} {currency_from} is equal to {exchanged_amount:.2f} {currency_to}.")

if __name__ == "__main__":
    main()

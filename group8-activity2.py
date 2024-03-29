# Part 1: Currency Conversion Functions
# Suleiman samantar implemented these functions based on provided conversion rates.

def aed_to_other(amount, conversion_rate):
    """
    Convert AED to other currencies.

    This function was implemented by Suleiman Alnsour.
    Suleiman implemented the logic to convert AED to other currencies using the provided conversion rate.

    Args:
    amount (float): The amount of money in AED to convert.
    conversion_rate (float): The conversion rate to apply.

    Returns:
    float: The equivalent amount in the target currency.
    """
    return amount * conversion_rate


def other_to_aed(amount, conversion_rate):
    """
    Convert other currencies to AED.

    This function was implemented by Suleiman Alnsour.
    Suleiman implemented the logic to convert other currencies to AED using the provided conversion rate.

    Args:
    amount (float): The amount of money in the target currency to convert.
    conversion_rate (float): The conversion rate to apply.

    Returns:
    float: The equivalent amount in AED.
    """
    return amount / conversion_rate


# Part 2: Main Program
# Suleiman alnsour designed and implemented the main program, Maxim provided assistance with testing and optimization.

def main():
    """
    Main function to present the menu and guide users through the conversion process.

    This function was primarily designed and implemented by Suleiman Alnsour.
    Suleiman Samantar developed the main program logic to present users with a menu for currency conversion
    and guide them through the conversion process based on their selections. He also handled user input validation.

    Maxim provided assistance with testing and optimization throughout the development process.
    Maxim collaborated with Suleiman Samantar to test the program thoroughly and optimize its performance.
    """
    print("Welcome to Currency Converter")

    aed_to_other_rates = {'Euro': 0.2199, 'British Pound': 0.1913, 'US Dollar': 0.2723}
    other_to_aed_rates = {'Euro': 4.547, 'British Pound': 5.228, 'US Dollar': 3.673}

    while True:
        print("---------------------------------")
        print("1. AED to other currencies")
        print("2. Other currencies to AED")
        print("3. Exit")
        choice = input("Enter the conversion direction - choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the amount you want to convert: "))
            print("Select target currency:")
            for index, (currency, rate) in enumerate(aed_to_other_rates.items(), start=1):
                print(f"{index}. {currency}")
            target_index = int(input("Enter the number for the target currency: "))
            target_currency = list(aed_to_other_rates.keys())[target_index - 1]
            result = aed_to_other(amount, aed_to_other_rates[target_currency])
            print(f"{amount} AED is equal to {result} {target_currency}")

        elif choice == '2':
            amount = float(input("Enter the amount you want to convert: "))
            print("Select source currency:")
            for index, (currency, rate) in enumerate(other_to_aed_rates.items(), start=1):
                print(f"{index}. {currency}")
            source_index = int(input("Enter the number for the source currency: "))
            source_currency = list(other_to_aed_rates.keys())[source_index - 1]
            result = other_to_aed(amount, other_to_aed_rates[source_currency])
            print(f"{amount} {source_currency} is equal to {result} AED")

        elif choice == '3':
            print("Bye!!!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
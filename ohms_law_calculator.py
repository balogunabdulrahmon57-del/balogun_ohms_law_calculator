# Ohm's Law and Power Calculator
# Author: Abdur Rahman Balogun

def calculate_voltage():
    current = float(input("Enter current in amperes (A): "))
    resistance = float(input("Enter resistance in ohms: "))
    voltage = current * resistance
    print(f"Voltage = {voltage:.2f} V")


def calculate_current():
    voltage = float(input("Enter voltage in volts (V): "))
    resistance = float(input("Enter resistance in ohms: "))
    current = voltage / resistance
    print(f"Current = {current:.2f} A")


def calculate_resistance():
    voltage = float(input("Enter voltage in volts (V): "))
    current = float(input("Enter current in amperes (A): "))
    resistance = voltage / current
    print(f"Resistance = {resistance:.2f} Ω")


def calculate_power():
    voltage = float(input("Enter voltage in volts (V): "))
    current = float(input("Enter current in amperes (A): "))
    power = voltage * current
    print(f"Power = {power:.2f} W")


def main():
    while True:
        print("\nOhm's Law and Power Calculator")
        print("1. Calculate Voltage")
        print("2. Calculate Current")
        print("3. Calculate Resistance")
        print("4. Calculate Power")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        try:
            if choice == "1":
                calculate_voltage()
            elif choice == "2":
                calculate_current()
            elif choice == "3":
                calculate_resistance()
            elif choice == "4":
                calculate_power()
            elif choice == "5":
                print("Thank you for using the calculator.")
                break
            else:
                print("Invalid option. Please choose 1-5.")

        except ValueError:
            print("Please enter numbers only.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


if __name__ == "__main__":
    main()

import math

def show_menu():
    print("\n" + "="*35)
    print("      SMART CLI CALCULATOR      ")
    print("="*35)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√)")
    print("7. Percentage (%)")
    print("8. Exit")
    print("="*35)

def calculator():
    while True:
        show_menu()
        choice = input("Select an option (1-8): ").strip()

        if choice == '8':
            print("\nThank you for using Smart CLI Calculator. Allah Hafiz! 👋")
            break

        if choice in ['1', '2', '3', '4', '5', '7']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"➡️ Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"➡️ Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"➡️ Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("❌ Error: Division by zero is not allowed!")
                else:
                    print(f"➡️ Result: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"➡️ Result: {num1} ^ {num2} = {pow(num1, num2)}")
            elif choice == '7':
                print(f"➡️ Result: {num1}% of {num2} = {(num1 / 100) * num2}")

        elif choice == '6':
            try:
                num = float(input("Enter number for Square Root: "))
                if num < 0:
                    print("❌ Error: Cannot calculate square root of a negative number!")
                else:
                    print(f"➡️ Result: √{num} = {math.sqrt(num)}")
            except ValueError:
                print("❌ Invalid input!")
        else:
            print("❌ Invalid choice! Please select between 1 and 8.")

if __name__ == "__main__":
    calculator()
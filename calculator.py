print ("---Calculator---")
print("---Calculator---")
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero! (NEW FEATURE ADDED)"
        return a / b

# Interactive dynamic loop
calc = Calculator()

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '5':
        print("Goodbye!")
        break
        
    if choice in ['1', '2', '3', '4']:
        try:
            # Take numeric input from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {calc.divide(num1, num2)}")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please choose between 1 and 5.")

print("Testing Stacked PRs")
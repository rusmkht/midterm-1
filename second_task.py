# лямбдалар функциясын жазып аламыз
operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y,
    4: lambda x, y: x ** y
}

# Мумкин операцияларды шыгарамыз
print("Select an operation:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

# Колданушынын тандауын кабылдаймыз
choice = int(input("Enter the operation number (1/2/3/4): "))

# тандауы биздин операциялар катарында барма екенин тексеремиз
if choice in operations:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # тандалган операцияны орындаймыз
    result = operations[choice](num1, num2)
    operation = "addition" if choice == 1 else "multiplication" if choice == 2 else "division" if choice == 3 else "exponentiation"

    # жауабын шыгарамыз
    print(f"Result of {operation} is: {result}")
else:
    print("Invalid choice. Please select a valid operation.")
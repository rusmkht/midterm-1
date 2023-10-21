# Есимин енгизуди сураймыз
name = input("Enter your name please: ")

# Жалакысын енгизуди сураймыз
salary = input("Enter your desired salary level: ")

try:
    # salary-ды int ка аустрамз
    salary_int = int(salary)

    # налогын есептеймз
    tax = salary * 0.2

    # жалакы мен налогын шыгарамыз
    print(f"{name}, the tax level you will pay with the salary {salary} is {tax}")

except ValueError:
    print(f"{name}, please enter your desired salary as a digit.")

def generate_fibonacci_sequence(length):  # функция ашамыз

    fibonacci_sequence = [1, 1]  # ен биринши default сандардан куралган массив

    while len(fibonacci_sequence) < length:  # пока fibonacci_sequence-тын узындыгы length-дан кишкентай кезде келеси операциялар орындалады
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # массивтагы сонгы санмен онын алдындагы # санннын косындысы
        fibonacci_sequence.append(next_number)  # next_number-ды массивтын сонына косамыз

    return fibonacci_sequence  # массивты кайтарамыз

try:

    length = int(input("Please enter the length of Fibonacci sequence: "))  # Фибоначи дын узындыгын сураймыз

    if length <= 0:  # егер сан 0 ге тен немесе киши болса
        print("Please enter a positive integer length.")  # positive сан енгизуды сураймыз

    else:  # егер 0 ден улкен болса
        fibonacci_sequence = generate_fibonacci_sequence(length)  # функцияны шакырамыз
        print(f"The Fibonacci sequence for {length} is:")
        print(", ".join(map(str, fibonacci_sequence)))  # fibonacci_sequence массивтан каждый санды str ретинде косып шыгарамыз

except ValueError:
    print("Value error")  # кате

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 != 0:
        print(number * 3 + 1)
        return number * 3 + 1


# Allow 3 input attempts.
count = 0
while count < 3:
    try:
        number = int(input("Input number: "))
        while number != 1:
            number = collatz(number)
        break

    except ValueError:
        print("Not an integer!")
        count += 1

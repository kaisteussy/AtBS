import random

current_streak = 0
numberOfStreaks = 0
flipList = []

for experimentNumber in range(10000):
    flipList = [random.randint(0, 1) for num in range(100)]

    for i in range(100):
        if i != 0 and flipList[i] == flipList[i-1]:
            current_streak += 1
            if current_streak == 6:
                numberOfStreaks += 1
                break
        elif i == 0:
            current_streak = 1
        else:
            current_streak = 0

print(f'Chance of streak: {(numberOfStreaks / 100)}%')

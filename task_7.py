a = int(input("Введите километраж пробежки в первый день тренировок: "))
b = int(input("Введите километраж пробежки в последний тренировочный день:"))
day = 1
while a < b:
    a = a + a * 0.1
    day = day + 1
print(day)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

counter_1 = 0
counter_0 = 0
for i in range(randint(1, 10)):
    coin = randint(0, 1)
    print(coin, end=" ")
    if coin == 1: counter_1 += 1
    if coin == 0: counter_0 += 1
if counter_1 > counter_0: print("Переворачиваем 0 ", counter_0, "раз")
if counter_1 < counter_0: print("Переворачиваем 1 ", counter_1, "раз")
if counter_1 == counter_0: print("Переворачиваем 0 ", counter_0, "раз")
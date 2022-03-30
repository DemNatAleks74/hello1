# Задача 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчёте на одного сотрудника.

profit = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit - costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
mc = 0
for i in range(months):
    mc -= salary - spend * (1 + increase)**i
# округление согласно задания не допустимо т.к расходы будут больше чем бюджет  с копейками
# Что-бы получить правильный результат и остаться без задолжностей следует использовать
# import math
# а в результат вывести
# print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(mc))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(mc))
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

m = 0
while True:
    money_capital += salary - spend * ((1 + increase) ** m)
    if money_capital < 0:
        break
    m += 1

print("Количество месяцев, которое можно протянуть без долгов:", m)
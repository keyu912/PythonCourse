# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


months = 0
while money_capital >= 0:
    money_capital += salary - spend
    spend *= (1 + increase)
    if money_capital < 0:
        break
    months += 1

print('Количество месяцев, которое можно протянуть без долгов:', months)




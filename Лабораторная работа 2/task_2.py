'''
Продолжение финансового планирования

### Описание
В этом задании вы рассмотрите ситуацию с финансовой подушкой безопасности и
ежемесячными расходами.

Имеется финансовая подушка безопасности `money_capital` руб. 
Ежемесячная зарплата составляет `salary` рублей, а расходы на
проживание превышают ее и составляют `spend` руб. в месяц. 
Рост цен `increase` ежемесячно увеличивает расходы на 5%.
В первый месяц повышения цен нет.

Определить, какую подушку безопасности `money_capital` нужно иметь,
чтобы протянуть 10 месяцев без долгов, то есть, используя только зарплату
и подушку безопасности. 
Все расходы текущего месяца сначала покрываются зарплатой,
а затем нехватка средств покрывается подушкой безопасности. 
Ответ округлить до целого числа.
'''


salary = 40000  
spend = 45000   
increase = 0.05  
months = 10     
money_capital = 0  

while True:
    current_capital = money_capital
    can_survive = True  
    for month in range(months):
        
        current_capital += salary
        
        if current_capital < spend:
            
            money_need = spend - current_capital
            money_capital += money_need
            current_capital = 0  
            can_survive = False  
            
        current_capital -= spend
    
        spend *= (1 + increase)

    if can_survive:
        break

money_capital = round(money_capital)

print('Нужно иметь подушку безопасности', money_capital, 'рублей, чтобы протянуть 10 месяцев')

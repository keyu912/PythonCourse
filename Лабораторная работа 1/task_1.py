'''
Замена пропущенного элемента средним арифметическим

### Описание:
У вас есть список чисел, в котором один из элементов случайно пропущен. 
Ваша задача — найти пропущенный элемент и заменить его средним арифметическим всех остальных элементов списка. 
При расчете суммы для среднего арифметического берутся все числа, кроме пропуска. 
А для расчёта количества — все элементы, включая пропуск.
'''
num_list = [1, 2, 3, 4, 5, None, 7, 8, 9]
mis_index = num_list.index(None)
mean = (sum(num_list[0:mis_index])+sum(num_list[mis_index+1:]))/len(num_list)
num_list[mis_index] = round(mean, 3)
print(num_list)

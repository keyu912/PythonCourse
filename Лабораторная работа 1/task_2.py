'''
Расчет количества книг на дискете

### Описание
У вас имеется информационный объем дискеты, равный 1,44 Мб, а также параметры книги, такие как количество страниц, число строк на странице и количество символов в строке. 
Ваша задача — рассчитать, сколько одинаковых книг можно поместить на дискету, и вывести результат на экран.
- Информационный объем дискеты равен 1,44 Мб. 
- Количество страниц в книге - 100. 
- Число строк на странице - 50. 
- Количество символов в строке - 25. 
- Для хранения кода одного символа нужно 4 байта.
'''

disk = 1.44 * 1024 * 1024
pages = 100
strings = 50
letters = 25
one_letter = 4

books = disk//(one_letter*letters*strings*pages)
print('Количество книг, помещающихся на дискету:', int(books))

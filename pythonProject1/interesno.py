from collections import defaultdict

my_default_dict = defaultdict(int)
for letter in 'Один из моих самых любимых инструментов стандартной библиотеки. DefaultDict — словарь с дефолтным значением для любого нового ключа. Пример:':
	my_default_dict[letter] += 1
print(my_default_dict)

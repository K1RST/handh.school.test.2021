from random import randint
n = int(input()) # Кол-во подмассивов
parity = 1 # Переменная четности
main_mass = [] # Основной массив

# Функция сортировки MERGE(сортировка путем деления массива на подмассивы)
def merge_sort(sub_mass):
	# Провекра размерности массива(если в массиве всего 1 элемент, то и сортирвоать нет смысла)
	if len(sub_mass) > 1:
		
		mid = len(sub_mass)//2 # Центр массива
		L = sub_mass[:mid] # Левая часть массива
		R = sub_mass[mid:] # Правая часть массива

		merge_sort(L) # Рекурсивный вызов функции
		merge_sort(R) # Рекурсивный вызов функции

		i = j = k = 0 # Каунтеры

		# Цикл сортировки
		while i < len(L) and j < len(R):
			# Проверка четности индекса подмассива
			if not parity: # Четный
				if L[i] < R[j]:
					sub_mass[k] = L[i]
					i += 1
				else:
					sub_mass[k] = R[j]
					j += 1
				k+=1
			else: # Нечетный
				if L[i] > R[j]:
					sub_mass[k] = L[i]
					i += 1
				else:
					sub_mass[k] = R[j]
					j += 1
				k+=1
		 # -------------------------------------------------

		# Объединение массивов
		while i < len(L):
			sub_mass[k] = L[i]
			i += 1
			k += 1
		# ---------------------------

		# Объединение массивов
		while j < len(R):
			sub_mass[k] = R[j]
			j += 1
			k += 1
		# ---------------------------


# -----------------------------------------------------------------------------------------

# Рекурсивная рандомизация размера массива
def size_recursion():
	mass_size = randint(1,25) # Размер массива от 1 до 25
	for mass in main_mass:
		if mass_size == len(mass): # Проверка на уникальность длины массива
			size_recursion()
	return mass_size
# -----------------------------------------------------------------------------------------

# Основная функция для создания и вывода массива main_mass
def main():
	for count in range(n):
		sub_mass = [] # Подмассив
		mass_size = size_recursion() # Размер подмассива
		for i in range(mass_size): # Цикл для заполнения подмассива
			sub_mass.append(randint(1, 100))

		global parity # Переопределение глобальной переменной
		parity = count%2 # Переменная для определения четности
		
		print(count, "unsorted", sub_mass)
		merge_sort(sub_mass) # Вызов функции сортировки
		print(count ,"sorted", sub_mass)

		main_mass.append(sub_mass) # Заполнение массива подмассивами 
	
	print('')		
	print(main_mass)
# -----------------------------------------------------------------------------------------

main()

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Расчет суммы всех чисел в списке без None
full_sum = sum(numbers[:numbers.index(None)]) +sum(numbers[numbers.index(None)+1:])
# Расчет количества элементов в списке
full_count = len(numbers)
# Расчет среднего арифметического всех чисел
average= full_sum/full_count
# Поиск пропущенного числа
miss_num = round(average * (full_count +1) - full_sum,2)
# Замена пропущенного числа средним арифметическим
numbers[numbers.index(None)] = miss_num

print("Измененный список:", numbers)
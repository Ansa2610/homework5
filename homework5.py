immutable_var = (1, 2, True, 'mode')
print(immutable_var)
print(immutable_var[3])
#immutable_var[3] = True - попытка сменить элемент 'mode' на лог.тип данных
#immutable_var[1] = 20 - попытка сменить число 2 на 20. Т.о. кортеж сохраняет неизменными элементы для сохранности коллекции.
mutable_list = ([50, 60, 500, 600], 10, 100, 'alien')
print(mutable_list)
mutable_list[0][0] = 70
print(mutable_list)
mutable_list[0][1] = 80
print(mutable_list)
mutable_list[0][2] = 700
print(mutable_list)
mutable_list = ([50, 60, 500, 600], 10, 100, 'alien') + ([10, 20], 'species')
print(mutable_list)
mutable_list = (101, 202) * 4
print(mutable_list)
mutable_list = (True, 'alien') * 2
print(mutable_list)
import csv

user_input = input()

shop_id_array_dict = list()
shop_id_array = list()
shop_name_array = list()
order_id_array = list()
cost_array = list()


# получим названия таблиц
table_name_1 = user_input.split(" ")[0]
table_name_2 = user_input.split(" ")[1] # возможно надо будет убрать /n



# создадим словарь по первому файлу: каждой колонке сделаем массив
with open(table_name_1, encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file)
    for row in file_reader:
        shop_id_array_dict.append(row['shop_id'])
        shop_name_array.append(row['shop_name'])
del table_name_1
zipped = tuple(zip(shop_id_array_dict, shop_name_array))
del shop_id_array_dict, shop_name_array, file_reader
shop_name_array = list()

# создадим словарь по второму файлу: каждой колонке сделаем массив
with open(table_name_2, encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file)
    for row in file_reader:
        name = None
        for i in zipped:
            if i[0] == row['shop_id']:
                name = i[1]
                break
        if name:
            order_id_array.append(row['order_id'])
            cost_array.append(row['cost'])
            shop_id_array.append(row['shop_id'])
            shop_name_array.append(name)
# запишем данные в таблицу
del file_reader, table_name_2
fieldnames = ['order_id', 'shop_name', 'shop_id', 'cost']
print(",".join(fieldnames))
for i in range(len(cost_array)):
    print(f"{order_id_array[i]},{shop_name_array[i]},{shop_id_array[i]},{cost_array[i]}")


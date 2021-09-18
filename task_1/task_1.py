import json

ls = list()
while(True):
    s = input().strip()
    if s == "":
        break
    ls.append(s)
string_list = ls[1:-1]



json_string = str()
json_part_list = list()
converted_part_list = list()

for element in string_list:
    json_string = json_string + element
while json_string.find("{") != -1:
    json_part_list.append(json_string[json_string.find("{"):json_string.find("}")+1])
    json_string = json_string[json_string.find("}")+2:]

for i in range(len(json_part_list)):
    converted = json.loads(json_part_list[i])
    converted_part_list.append(converted)


sub_dict = dict()
output_dictionary = list()


def final_form_creation(input_dictionary_part):
    # приведём в нужный вид
    for i in range(len(input_dictionary_part)):
        output_dictionary_part = dict()
        sub_dict["count"] = int(input_dictionary_part[i]["count"]) - int(input_dictionary_part[i]["return_count"])
        sub_dict["id"] = int(input_dictionary_part[i]["item_id"])
        output_dictionary_part["id"] = int(input_dictionary_part[i]["order_id"])
        output_dictionary_part["items"] = [sub_dict]
        output_dictionary.append(output_dictionary_part)
    return output_dictionary


def sort_creation(input_sorted_list):
    output_list = list()
    # разбиваем входной список УЖЕ ОТСОРТИРОВАННЫЙ ПО ИВЕНТАМ по элементам, где каждый элемент - словарь
    for i in range(0, len(input_sorted_list)):
        input_part = input_sorted_list[i]
        # проверим на пригодность каждый словарь
        if input_part["status"] == "CANCEL" or int(input_part["count"] - input_part["return_count"]) == 0 \
                or input_part["count"] == 0:
            pass
        else:
            adding = input_part
            # добавляем словарь-часть в финальный список
            output_list.append(adding)
    return output_list


def event_sort(input_list):
    # создадим копию для работы с ней
    copy_list = list()
    for b in range(len(input_list)):
        copy_list.append(input_list[b])
    for k in range(0, len(input_list)):
        for m in range(k + 1, len(input_list)):
            # будем сравнивать k-ый и m-ый элементы-словари
            k_dict = input_list[k]
            m_dict = input_list[m]
            if k_dict["order_id"] == m_dict["order_id"] and k_dict["event_id"] > m_dict["event_id"]:
                copy_list.remove(m_dict)

            elif k_dict["order_id"] == m_dict["order_id"] and k_dict["event_id"] < m_dict["event_id"]:
                copy_list.remove(k_dict)

            else:
                pass
    return copy_list


print(json.dumps(final_form_creation(sort_creation(event_sort(converted_part_list)))[:],indent=4))

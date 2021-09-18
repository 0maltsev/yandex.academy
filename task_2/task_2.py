import datetime



def time_and_error_amount(text):
    time_error = list()
    time = int(text.split(" ")[0])  # промежуток времени для вычисления критического момента
    error_amount = int(text.split(" ")[1])  # минимально необходимое число ошибок на промежутке
    time_error.append(time)
    time_error.append(error_amount)
    return time_error



def get_string_list(text):
    # создадим массив из строк - чтобы работать с каждым логом
    string_list = text.split("\n")
    remove_time_error = string_list.pop(0)
    return string_list


def get_data_list(text):
    string_list = get_string_list(text)
    date_list = list()
    time_list = list()
    copy_list = list()
    full_time = list()
    for k in range(len(string_list)):
        copy_list.append(string_list[k])
    # получим массив, состоящий только из времени ошибок
    for i in range(len(string_list)):
        # убираем строки без ERROR
        if string_list[i].find("ERROR") == -1:
            copy_list.remove(string_list[i])  # понадобится на выводе в конце
        else:
            # массив времени каждого лога
            date_list.append(string_list[i].split(" ")[0][1:])
            time_list.append(string_list[i].split(" ")[1][:-1])
    full_time.append(date_list)
    full_time.append(time_list)
    full_time.append(copy_list)
    return full_time

# date_list = full_time[0]
# time_list = full_time[1]


def time_convertation(text):
    time_list = get_data_list(text)[1]
    date_list = get_data_list(text)[0]
    year_list = list()
    month_list = list()
    day_list = list()
    hour_list = list()
    minute_list = list()
    second_list = list()
    timing = list()
    # сделаем массивы по временным категориям
    for i in range(len(date_list)):
        year_list.append(date_list[i].split("-")[0])
        month_list.append(date_list[i].split("-")[1])
        day_list.append(date_list[i].split("-")[2])
    for k in range(len(time_list)):
        hour_list.append(time_list[k].split(":")[0])
        minute_list.append(time_list[k].split(":")[1])
        second_list.append(time_list[k].split(":")[2])
    timing.append(year_list)
    timing.append(month_list)
    timing.append(day_list)
    timing.append(hour_list)
    timing.append(minute_list)
    timing.append(second_list)
    return timing


def searching(text):
    timing = time_convertation(text)
    time = time_and_error_amount(text)[0]
    error_amount = time_and_error_amount(text)[1]
    copy_list = get_data_list(text)[2]
    final_list = list()
    # уберем случай, когда в логах нет ошибок:
    if len(copy_list) == 0:
        return -1
    else:
        # если достаточно одной ошибки - выводим первую
        if error_amount == 1:
            return copy_list[0][copy_list[0].find("[")+1:copy_list[0].find("]")]
        # проверим, какие случаи подходят по времени и количеству ошибок
        else:
            for i in range(0, len(timing[0])-error_amount+1):

                first_log = datetime.datetime(int(timing[0][i]),
                                              int(timing[1][i]), int(timing[2][i]),
                                              int(timing[3][i]), int(timing[4][i]), int(timing[5][i]))

                second_log = datetime.datetime(int(timing[0][i+error_amount-1]),
                                               int(timing[1][i+error_amount-1]), int(timing[2][i+error_amount-1]),
                                               int(timing[3][i+error_amount-1]), int(timing[4][i+error_amount-1]), int(timing[5][i+error_amount-1]))

                # разница между логами в секундах
                seconds = (second_log - first_log).seconds
                # сравниваем с данным таймингом
                if seconds < time:
                    final_list.append(copy_list[i+error_amount-1])
                else:
                    pass
            # проверим на существование вывода
            if len(final_list) != 0:
                return final_list[0][final_list[0].find("[")+1:final_list[0].find("]")]
            else:
                return -1

a,b = input().split(' ')
working_string = f"{a} {b} \n"
while True:
    try:
        buffer_string = input()
        working_string += buffer_string + "\n"
    except EOFError:
        break

print(searching(working_string))
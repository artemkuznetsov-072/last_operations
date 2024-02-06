import json
from datetime import datetime


def get_operations():
    """
    Загружает список операций с файла
    """
    with open('C:/Users/user/PycharmProjects/last_operations/operations.json', "r", encoding='utf-8') as file:
        operations_list = json.load(file)
    return operations_list


def get_sorted_operations():
    """
    Сортирует операции по дате
    """
    operations_dict = []
    x = get_operations()
    for operation in x:
        if operation.get('state') == "EXECUTED" and operation.get('date'):
            operations_dict.append(operation)
    sorted_operations = sorted(
        operations_dict,
        key=lambda x: x.get('date'), reverse=True)
    return sorted_operations[:5]


def check_sender(sender):
    """
    Проверяет наличие отправителя и выбирает объект для шифрования
    """
    if sender:
        data = sender.split()
        if data[0] == "Счет":
            return encode_account(data)
        else:
            return encode_card(data)
    return "Unknown"


def encode_account(data):
    """
    Шифрует счет
    """
    account_name = '**' + data[-1][-4:]
    return data[0] + ' ' + account_name


def encode_card(data):
    """
    Шифрует карту
    """
    payment_sys = ' '.join(data[:-1]) + ' '
    card_name = data[-1]
    card_number = card_name[0:4] + ' ' + card_name[4:6] + '** **** ' + card_name[12:]
    return payment_sys + card_number


def print_date(source_date):
    """
    Преобразует дату в нужный формат
    """
    try:
        datatime = datetime.fromisoformat(source_date)
        return datatime.strftime('%d.%m.%Y')
    except ValueError:
        return '<invalid date format>'

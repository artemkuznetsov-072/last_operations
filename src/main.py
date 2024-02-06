from utils import get_sorted_operations, check_sender, print_date


def print_operations():
    """
    Выводит пользователю 5 последних успешных операций
    """
    print("Для вывода пяти последних операций нажмите \"Enter\"")
    user_enter = input()
    transaction_info = get_sorted_operations()

    for trans in transaction_info:
        print(print_date(trans.get('date')), trans.get('description'))
        print(f"{check_sender(trans.get('from'))} -> {check_sender(trans.get('to'))}")
        print(trans.get('operationAmount').get('amount'), trans.get('operationAmount').get('currency').get('name'))
        print()


if __name__ == '__main__':
    print_operations()

















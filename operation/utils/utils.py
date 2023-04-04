import json
from datetime import datetime
from colorama import Fore


def last_five_executed_operations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        executed_operations = []
        for i, operation in enumerate(data):
            if operation.get('state') == 'EXECUTED':
                executed_operations.append(operation)

        sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
        last_five_operations = sorted_operations[:5]
        return print(print_info(last_five_operations))


def print_info(operations):
    for item in operations:
        operation = f'''{Fore.RED}{print_date(item['date'])} {Fore.RESET}{item['description']}''''\n' \
               f'''{encrypt_card_number(check_key(item, 'from')).strip()} -> {Fore.YELLOW}{encrypt_card_number(item['to']).strip()}''''\n' \
               f'''{Fore.GREEN}{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}''' '\n'\

        print(operation)


def print_date(data):
    date_time_obj = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
    new_date_string = date_time_obj.strftime('%m.%d.%Y %H:%M:%S')
    return new_date_string


def encrypt_card_number(card_number):
    alpha = ''.join(filter(str.isalpha, card_number))
    number = ''.join(filter(str.isdigit, card_number))
    groups = ' '.join([number[i:i + 4] for i in range(0, len(number), 4)])
    first_digits = groups[:4]
    last_digits = groups[-4:]
    mask = ''.join([" " if char == " " else "*" for char in groups])
    masked_str = f"{alpha} {first_digits}{mask[len(first_digits):-len(last_digits)]}{last_digits}"

    return masked_str


def check_key(dict_, key):
    return dict_[key] if key in dict_ else 'unknown'

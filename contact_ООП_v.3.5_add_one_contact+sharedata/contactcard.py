
class ContactCard:
    '''Формирует окно "Контакт".'''
    def __init__(self, data_str, indicator):
        if indicator == 'Добавить':
            print('Обработка события "Добавить контакт"') 
        elif indicator == 'Показать':
            print('Обработка события "Показать контакт"') 
            print(data_str)

if __name__ == '__main__':
    choice = input('Тестирование события: "Показать контакт" -1 "Добавить контакт" -2: ')
    if choice == '1':
        ContactCard('Отображение контакта', 'Показать')
    elif choice == '2': 
        ContactCard('', 'Добавить')



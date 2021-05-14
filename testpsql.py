import psycopg2

def read_contacts_psql():
    '''Получает контакты из БД contactdb.'''

    # Переменной dbn присвоена строка с параметрами 
    # соединения к БД contactdb. 
    # Вместо звёздочек **** введите свой пароль.
    dbn = 'dbname=contactdb user=postgres password=**** host=127.0.0.1'

    # Устанавливаю соединение с БД.
    connection = psycopg2.connect(dbn)

    # Получаю курсор.
    cursor = connection.cursor()

    # Получение всех строк и полей из таблицы data.
    cursor.execute('SELECT * FROM data')

    # В цикле вывожу на печать каждую строку таблицы data.
    # Строка выводится в виде кортежа.
    for row in cursor:
        print(row)
    cursor.close()     # Закрываю курсор.
    connection.close() # Закрываю соединение с БД.
    
read_contacts_psql() # Вызов функции.





import psycopg2

def read_contact_txt_gui_list(file_name):
    '''Для получения данных из текстового файла.
       Обработка данных. Функция возвращает
       список контактов.'''
    # Открытие файла для чтения данных.
    file_txt_r = open(file_name, 'r') 
    # Переменная для хранения списка контактов.
    data_list_all = []
    # Бесконечный цикл для обработки контактов построчно.
    while True: 
        # Получение строки с контактом из txt-файла.
        data_str = file_txt_r.readline()
        # Если строка пустая, то выход из цикла. 
        if data_str == '': 
            file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла.
        # С каждым проходом цикла в список добавляется контакт.
        data_list_all.append(data_str)
    # Функция возвращает список контактов.   
    return data_list_all 

def write_contacts_psql(data_list_all):
    '''Получает список контактов. Обработка данных. 
       Запись в БД.'''
    # Переменной dbn присвоена строка с параметрами 
    # соединения к БД contactdb.
    # Введите свой пароль вместо звёздочек password=****.
    dbn = 'dbname=contactdb user=postgres password=**** host=127.0.0.1'
    # Или можно так.
    #dbn = (dbname='contactdb', user='postgres', password='****', host='127.0.0.1')
    # Устанавливаю соединение с БД.
    connection = psycopg2.connect(dbn)
    # Получаю курсор.
    cursor = connection.cursor()
    # Для каждого контакта в списке контактов.
    for data_str in data_list_all:
        # Полученная строка data_str разделяется по символу &.
        data_list = data_str.split('&')
        # Получение фамилии.
        lastname = data_list[0]
        # Получение имени.       
        firstname = data_list[1]
        # Получение адреса.        
        address = data_list[2]
        # Получение номера телефона.         
        phonenumber = data_list[3]
        # Получение электронного адреса.    
        email = data_list[4] 
        # Получение дополнительной информации.          
        addinform = data_list[5]
        # Получение даты и времени записи контакта.
        dt = data_list[6]
        # Получение даты создания контакта.              
        d = dt.split(' ')[0] 
        # Получение URL (ссылки) на фотографию контакта.        
        url_photo = lastname + d
	# Из полученных элементов контакта формирую кортеж. 
        # Кортежем также называется строка в таблице БД.
        # Поле contact_id заполняется автоматически.
        dat = (lastname, firstname, address, phonenumber, email, addinform, dt, d, url_photo)
        datain = 'INSERT INTO data(lastname, firstname, address, \
                  phonenumber, email, addinform, dt, d, url_photo) \
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # Выполнение SQL-запроса. Запись данных в БД.
        cursor.execute(datain, dat)
        connection.commit()
    cursor.close()     # Закрываю курсор.
    connection.close() # Закрываю соединение с БД.

write_contacts_psql(read_contact_txt_gui_list('contact.txt'))

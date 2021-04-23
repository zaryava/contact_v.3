class ShareData:
    '''Аргументы и методы для общего использования'''
    LOGO = 'logotip.ico'          # Константа.
    FILE_NAME_TXT = 'contact.txt' # Константа.
   
    data_str = ''
    data_list_all = []
    
    @staticmethod
    def data_str_split(data_str):
        '''Разделение строки контакта на элементы
           по символу "&". Формирование
           списка элементов.'''
        data_list = data_str.split('&')
        return data_list
    
    @staticmethod
    def write_contact_txt(contact):
        '''Запись контакта в текстовый файл. 
           Отрытие файла. Запись. Закрытие файла.'''
        if contact == '': # Если пустая строка.
            file_txt = open(ShareData.FILE_NAME_TXT, 'a') # Создание txt-файла.
        else: # Если не пустая строка.
            file_txt = open(ShareData.FILE_NAME_TXT, 'a') # Открытие txt-файла.
            file_txt.write(contact) # Запись контакта в txt-файл.        
        file_txt.close() # Закрытие txt-файла.


        

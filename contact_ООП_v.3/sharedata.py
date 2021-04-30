from tkinter import *
from tkinter import messagebox, filedialog 
from PIL import ImageTk, Image
from datetime import datetime
import os
import sys

class ShareData:
    '''Переменные и методы для общего использования'''
    LOGO = 'logotip.ico'          # Константа.
    FILE_NAME_TXT = 'contact.txt' # Константа.
    NOFOTO = 'nofoto.png'         # Константа.
    TEMP = 'temp.png'             # Константа.
    

    photo_save_temp = 0 # Если значение 0 - файл 'temp.png' не существует,
                        # если значени 1 - файл 'temp.png' существует.     

    update_save_cont = 0 # Если значение 0 - не запускать функцию update_save(),
                         # если значени 1 - запускать функцию update_save().    

    open_win_show_contact_flag = 0 # Если значение 0 - окно win_show закрыто,
                                   # если значение 1 - окно win_show открыто. 
    data_str = ''
    data_list_all = []
    
    @staticmethod
    def data_str_split(data_str):
        '''Разделение строки контакта на элементы
           по символу "&". Формирование
           списка элементьов.'''
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


        

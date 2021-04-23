import os
from tkinter import *
from tkinter import messagebox, filedialog

list_for_sort = [] # Переменная для хранения несортированного списка контактов.
list_sort = [] # # Переменная для хранения сортированного списка контактов.

def read_contact_txt_gui_list(file_name):
    '''Для получения данных из текстового файла.
       Обработка данных. Функция возвращает
       список контактов.'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.        
    data_list_all = [] # Переменная для хранения списка контактов.                              
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str = file_txt_r.readline() # Получение строки с контактом.
        if data_str == '': # Если строка пустая то выход из цикла.
            file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла.
        data_list_all.append(data_str) # С каждым проходом цикла в список добавляется контакт.
    return data_list_all # Функция возвращает список контактов.     

def print_contact_gui_list(data_list_all, color='red'):
    '''Получает список контактов. Обработка данных. 
       Вывод на печать списка фамилий из контактов.'''
    listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
    for data_str in data_list_all: # Для каждого контакта в списке контактов.
        data_list = data_str.split('&')    # Полученная строка разделяется по символу &.
                                           # Формируется список data_list с элементами контакта.                                  
        contact_last_name = data_list[0]       # Получение фамилии.
        contact_first_name = data_list[1]      # Получение имени.
        contact_address = data_list[2]         # Получение адреса.   
        contact_phone_number = data_list[3]    # Получение номера телефона.
        contact_date_time_write = data_list[4] # Получение даты и времени записи контакта.
        contact_email = data_list[4]           # Получение электронного адреса.
        contact_add_inform = data_list[5]      # Получение дополнительной информации.
        contact_dt = data_list[6]              # Получение даты и времени записи контакта.
        listbox_frame_lb['fg'] = color # Задаётся цвет шрифта. 
        listbox_frame_lb.insert(END, f' {contact_last_name}') # Вывод на печать.
    
def write_contact_txt_gui(file_name, contact):
    '''Для записи контакта в текстовый файл. 
       Отрытие файла. Запись. Закрытие файла'''
    file_txt = open(file_name, 'a')
    file_txt.write(contact)
    file_txt.close()

def open_file():
    '''Функция обработчик пункта Меню <Файл-Открыть файл с контактами>'''
    global list_for_sort, file_path_open
    # Получение пути к файлу в виде строки для его открытия через диалоговое окно.
    # Пример: 'C:/Users/Downloads/contact.txt'.
    file_path_open = filedialog.askopenfilename(title='Выбор файла',
                                                filetypes=(('Текстовые документы,(*.txt)', '*.txt'),))
    if file_path_open: # Если путь получен (строка file_path_open  не пустая)
        list_for_sort = read_contact_txt_gui_list(file_path_open) # Глобальной переменной присваивается
                                                                  # список контактов для сортировки.
        print_contact_gui_list(list_for_sort) # Вывод списка фамилий из контактов для сортировки.

def sorted_list():
    '''Функция для сортировки списка контактов в алфавитном порядке.
       Формирование нового сортированного списка.
       Вывод этого списка на печать'''
    global list_sort
    if list_for_sort:
        list_sort = sorted(list_for_sort)
        print_contact_gui_list(list_sort, color='green') # Изменение цвета шрифта с красного на зелёный.
    else:
        listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
        listbox_frame_lb['fg'] = 'blue' # Изменение цвета шрифта с красного на голубой.
        listbox_frame_lb.insert(END, '---------------------------------------') # Элемент оформления.
        listbox_frame_lb.insert(END, '     ВЫБЕРИТЕ ФАЙЛ ДЛЯ СОРТИРОВКИ')       # Вывод информации.
        listbox_frame_lb.insert(END, '---------------------------------------') # Элемент оформления.

def write_list_sort():
    '''Функция для удаления файла 'contact.txt'
       с несортированными контактами. Создание
       нового файла 'contact.txt' с сортированными
       в алвафитном порядке контактами'''
    if list_sort: # Если список с сортированными контактами не пустой.
        os.remove(file_path_open) # Удаление старого 'contact.txt'.
        for data_str in list_sort: # Для строки с контактом в списке контактов.
            write_contact_txt_gui(file_path_open, data_str) # Создание файла 'contact.txt' и построчная
                                                            # запись контактов в текстовый файл.           
        listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
        listbox_frame_lb['fg'] = 'blue' # Изменение цвета шрифта с красного на голубой.
        listbox_frame_lb.insert(END, '---------------------------------------') # Элемент оформления.
        listbox_frame_lb.insert(END, "     ТЕКСТОВЫЙ ФАЙЛ 'contact.txt'")       # Вывод информации.   
        listbox_frame_lb.insert(END, '   ПЕРЕЗАПИСАН В АЛФАВИТНОМ ПОРЯДКЕ')     # Вывод информации.
        listbox_frame_lb.insert(END, '---------------------------------------') # Элемент оформления.
    else:
        listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
        listbox_frame_lb['fg'] = 'blue' # Изменение цвета шрифта с красного на голубой.
        listbox_frame_lb.insert(END, '---------------------------------------') # Элемент оформления.
        listbox_frame_lb.insert(END, '               ВНИМАНИЕ!!!')              # Вывод информации.
        listbox_frame_lb.insert(END, '        ПРЕЖДЕ ЧЕМ ПЕРЕЗАПИСАТЬ')         # Вывод информации.
        listbox_frame_lb.insert(END, '                СНАЧАЛА')                 # Вывод информации.
        listbox_frame_lb.insert(END, '     ВЫБЕРИТЕ ФАЙЛ ДЛЯ СОРТИРОВКИ')       # Вывод информации.
        listbox_frame_lb.insert(END, '                 ЗАТЕМ')                  # Вывод информации.
        listbox_frame_lb.insert(END, '         ВЫПОЛНИТЕ СОРТИРОВКУ')           # Вывод информации.
        listbox_frame_lb.insert(END, '---------------------------------------') # Элемент оформления.
    
def exit_win_root():
    '''Функция обработчик пункта Меню <Файл-Выход>'''
    # Если нажимается пункт Меню Выход, появлятся окно с вопросом.
    answer = messagebox.askokcancel(title='Выход', message='Закрыть программу?')
    if answer: # Если нажата кнопка "Ок".      
        win_root.destroy() # Закрытие окна.    
      
#-----------------------------------Формирование окна программы--------------------------------
win_root = Tk()
win_root.title('Сортировка в алфавитном порядке')
win_root.iconbitmap('logotip.ico')
win_root.geometry('440x300+500+150')
win_root.resizable(0,0)

# Создние экземпляра класса Меню с привязкой к главному окну win_root.
main_menu = Menu(win_root)
# Вызывается метод конфигурации win_root и указывается, что menu=main_menu.
win_root.config(menu=main_menu)

# Создание Меню       
file_menu = Menu(main_menu, tearoff=0)

# add_comand() - добавляет выпадающий элемент Меню "Открыть файл с контактами".
file_menu.add_command(label='Открыть файл с контактами', command=open_file)

# add_comand() - добавляет выпадающий элемент Меню "Сортировать".
file_menu.add_command(label='Сортировать', command=sorted_list)

# add_comand() - добавляет выпадающий элемент Меню "Перезаписать".
file_menu.add_command(label='Перезаписать', command=write_list_sort)

# add_separator() - добавляет линию-разделитель между пунктами Меню.
file_menu.add_separator()

# add_comand() - добавляет выпадающий элемент Меню "Выход".
file_menu.add_command(label='Выход', command=exit_win_root)

# Создаю Label - 'Файл' к которому привязываю Меню
main_menu.add_cascade(label='Меню', menu=file_menu)

frame_lb = Frame(win_root)
frame_lb.pack(fill=BOTH, expand=1)

listbox_frame_lb = Listbox(frame_lb, fg = 'red', font=('Courier New', 14, 'italic', 'bold'))
listbox_frame_lb.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_lb, command=listbox_frame_lb.yview)
scroll.pack(fill=Y, side=LEFT)
listbox_frame_lb.config(yscrollcommand=scroll.set)

win_root.mainloop()
#----------------------------------------------------------------------------------------------




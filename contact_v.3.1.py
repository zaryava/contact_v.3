from tkinter import *
from tkinter import messagebox 
import sys

LOGO = 'logotip.ico'          # Константа.
FILE_NAME_TXT = 'contact.txt' # Константа.
FIND = 'find.png'             # Константа.
UPDATE = 'update.png'         # Константа.
ADD = 'add.png'               # Константа.
EXIT = 'exit.png'             # Константа.

data_list_all = []
data_list_all_alph = []
letter = ''

def show_all_contacts():
    '''Вызывается при запуске программы "Контакты".
       Чтение контактов из txt-файла. Вывод списка
       фамилий с буквами алфавита в виджет Listbox.'''          
    read_contact_txt_list() # Вызов функции для получения списка контактов из txt-файла.
                            # В результате выполнения Функциии формируется
                            # список контактов data_list_all.                                                 
    if data_list_all: # Если список контактов не пустой продолжается действие программы.                                                   
        alphabet_order_list() # Вызов Функции для формирования списка с буквами алфавита.
                              # Контакты в списке data_list_all уже расположены в алфавитном порядке.                                                                            
        print_contacts() # Вызов функции для вывода в виджет Listbox списка фамилий с алфавитом.
    else: # Иначе, если список контактов пустой.
        # Открывается диалоговое окно.
        answer_no_contacts = messagebox.askyesno(title='Список контактов пуст!', 
                                                 message='Добавить контакт?')
        if answer_no_contacts: # Если нажата кнопка 'Да'. 
            add_one_contact() # Вызов функции для открытия окна "Новый контакт".

def read_contact_txt_list():
    '''Получение данных из текстового файла. Обработка данных. 
       Результат выполнения - список контактов data_list_all (Глобальная переменная).
       Область видимости переменной data_str функция read_contact_txt_list().'''
    global data_list_all
    sentence_1 = "Отсутствует файл 'contact.txt'."      # 
    sentence_2 = " Добавьте файл 'contact.txt' в папку" # Длинное информационное  
    sentence_3 = " с программой или создайте файл"      # сообщение разделено 
    sentence_4 = " 'contact.txt'."                      # на 5 частей.
    sentence_5 = " Создать файл 'contact.txt'?"         #
    sentence = sentence_1 + sentence_2 + sentence_3 + sentence_4 + sentence_5
    try: # Обработка исключения для случая отсутствия файла 'contact.txt'.
        file_txt_r = open(FILE_NAME_TXT, 'r') # Открытие txt-файла для чтения данных.
        data_list_all = [] # Переменной для хранения списка контактов присваивается пустой список.                              
        while True: # Бесконечный цикл для обработки контактов построчно.
            data_str = file_txt_r.readline() # Получение строки с контактом.                                             
            if data_str == '': # Если строка пустая то выход из цикла. Это значит, 
                               # что в txt-файле закончились строки с конактами.
                file_txt_r.close()  # Закрытие текстового файла.
                break               # Выход из цикла.
            data_list_all.append(data_str) # С каждым проходом цикла в список добавляется контакт.
    except Exception: # Исключение в случае возникновения ошибки.
        # Вывод инвормационного сообщения 'sentence'.
        answer_txt = messagebox.askyesno(title='Нет связи с базой данных', message=sentence)
        if answer_txt: # Если нажата кнопка "Да". Создать txt-файл 'contact.txt'.
            write_contact_txt('') # Вызывается функция для создания txt-файла. Передаётся аргумент
                                  # пустая строка для создания пустого файла 'contact.txt'.
        else: # Иначе, если нажата кнопка "Нет".
            win_root.destroy() # Закрытие окна win_root.
            sys.exit() # Выход из программы "Контакты".

def write_contact_txt(contact):
    '''Запись контакта в текстовый файл. 
       Отрытие файла. Запись. Закрытие файла.'''
    if contact == '': # Если пустая строка.
        file_txt = open(FILE_NAME_TXT, 'a') # Создание txt-файла.
    else: # Если не пустая строка.
        file_txt = open(FILE_NAME_TXT, 'a') # Открытие txt-файла.
        file_txt.write(contact) # Запись контакта в txt-файл.        
    file_txt.close() # Закрытие txt-файла.

def alphabet_order_list():
    '''Формирование списка контактов data_list_all_alph с буквами алфавита.
       Область видимости переменной data_str функция alphabet_order_list().'''
    global letter, data_list_all_alph
    print(letter)
    print(data_list_all_alph)
    print('-----')
    for data_str in data_list_all: # Для строки контакта data в списке data_list_all.
        if data_str[0] == letter: # Если первая буква фамилии в строке контакта
                                  # равна значению переменной letter.
            print(data_list_all_alph)
            data_list_all_alph.append(data_str) # В список data_list_all_alph
                                                # добавляется строка контакта data_str.
            
        else: # Иначе, если первая буква фамилии не равна значению переменной letter.
            letter = data_str[0] # Переменной letter присваивается первая буква фамилии.
            data_list_all_alph.append(data_str[0]) # В список data_list_all_alph добавляется
                                                   # первая буква фамилии контакта data_str[0].
            data_list_all_alph.append(data_str) # После буквы в список data_list_all_alph
                                                # добавляется строка контакта data_str.

def print_contacts():
    '''Вывод в виджет Listbox списка контактов в алфавитном порядке с буквами алфавита.
       Область видимости переменной data_str функция print_contacts().'''
    listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
    for data_str in data_list_all_alph: # Для строки контакта data_str в списке data_list_all_alph.
        if len(data_str) == 1: # Если длина строки контакта равна одному символу, значит это буква.
            listbox_frame_lb.insert(END, f' {data_str}') # Вывод буквы в виджет Listbox.
            listbox_frame_lb.itemconfig(END, fg='green') # Буква окрашивается в зелёный цвет.
        else: # Иначе если длина контакта больше одного символа.
              # Вывод на печать фамилии контакта. Вызывается функция data_str_split(data_str)
              # для разделения элементов контакта и выбора из списка 0-го элемента (фамилии).
            listbox_frame_lb.insert(END, f' {data_str_split(data_str)[0]}') 
            listbox_frame_lb.itemconfig(END, fg='black') # Фамилия контакта окрашивается в чёрный цвет.

def data_str_split(data_str):
    '''Разделение строки контакта на элементы по символу
       "&". Формирование списка элементьов.'''
    data_list = data_str.split('&')
    return data_list

def add_one_contact():
    pass


win_root = Tk()
win_root.title('Контакты')
win_root.iconbitmap(LOGO)
win_root.geometry('320x450+100+150')
win_root.resizable(0,0)

photo_find = PhotoImage(file=FIND) # Создаётся экземпляр класса PhotoImage(file=FIND),
                                   # в качестве параметра передаётся путь к
                                   # изображению для кнопки "Поиск".
photoimage_find = photo_find.subsample(25, 25) # Вызов метода subsample() для уменьшения
                                               # размера изображения в 25 раз по 
                                               # горизонтали и в 25 раз повертикали.

photo_update = PhotoImage(file=UPDATE) # Создаётся экземпляр класса PhotoImage(file=UPDATE),
                                       # в качестве параметра передаётся путь к
                                       # изображению для кнопки "Обновить".
photoimage_update = photo_update.subsample(20, 20) # Вызов метода subsample() для уменьшения
                                                   # размера изображения в 20 раз по 
                                                   # горизонтали и в 20 раз повертикали. 

photo_add = PhotoImage(file=ADD) # Создаётся экземпляр класса PhotoImage(file=ADD),
                                 # в качестве параметра передаётся путь к
                                 # изображению для кнопки "Добавить".
photoimage_add = photo_add.subsample(25, 25) # Вызов метода subsample() для уменьшения
                                             # размера изображения в 25 раз по 
                                             # горизонтали и в 25 раз повертикали.

photo_exit = PhotoImage(file=EXIT) # Создаётся экземпляр класса PhotoImage(file=EXIT),
                                   # в качестве параметра передаётся путь к
                                   # изображению для кнопки "Выход".
photoimage_exit = photo_exit.subsample(25, 25) # Вызов метода subsample() для уменьшения
                                               # размера изображения в 25 раз по 
                                               # горизонтали и в 25 раз повертикали.  

frame_f = Frame(win_root, relief=GROOVE, borderwidth=2)
frame_f.pack(side=TOP, fill=X, padx=5, pady=3)

frame_lb = Frame(win_root, relief=GROOVE, borderwidth=2)
frame_lb.pack(fill=X, padx=5, pady=2)

frame_b = Frame(win_root, relief=GROOVE, borderwidth=2)
frame_b.pack(side=BOTTOM, fill=X, padx=5, pady=3)

entry_frame_f = Entry(frame_f, width=26, fg='blue',
                      font=('Calibri', 14, 'italic'))
entry_frame_f.pack(side=LEFT, padx=4)

btn_frame_f = Button(frame_f, relief=FLAT,
                     image=photoimage_find)
btn_frame_f.pack(side=RIGHT, padx=2, pady=2)

scroll_listbox = Scrollbar(frame_lb)
scroll_listbox.pack(side=RIGHT, fill=Y)

listbox_frame_lb = Listbox(frame_lb, width=20, height=15,
                           selectmode=EXTENDED, fg='black',
                           font=('Courier New', 14, 'bold')) 
listbox_frame_lb.pack(fill=X, padx=2, pady=2)

scroll_listbox.config(command=listbox_frame_lb.yview)

btn_show_frame_b = Button(frame_b, relief=FLAT, width=20, height=20,
                          image=photoimage_add)
btn_show_frame_b.pack(side=LEFT, padx=40, pady=2)

btn_show_frame_b = Button(frame_b, relief=FLAT, width=20, height=20,
                          image=photoimage_update)
btn_show_frame_b.pack(side=LEFT, padx=30, pady=2)

btn_exit_frame_b = Button(frame_b, relief=FLAT, width=20, height=20,
                          image=photoimage_exit)
btn_exit_frame_b.pack(side=RIGHT, padx=40, pady=2)

show_all_contacts()

win_root.mainloop()

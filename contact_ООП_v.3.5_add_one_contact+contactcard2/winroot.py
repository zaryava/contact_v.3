from tkinter import *
from tkinter import messagebox 
import sys
from contactcard import *

class WinRoot:
    '''Создаётся корневое окно win_root.'''    
    def __init__(self):
        self.LOGO = 'logotip.ico'          # Константа.
        self.FILE_NAME_TXT = 'contact.txt' # Константа.
        self.FIND = 'find.png'             # Константа.
        self.UPDATE = 'update.png'         # Константа.
        self.ADD = 'add.png'               # Константа.
        self.EXIT = 'exit.png'             # Константа.

        self.data_str = ''
        self.data_list_all = []
        self.data_list_all_alph = []
        self.letter = ''
        self.find_list = []
        
        self.win_root = Tk()
        self.win_root.title('Контакты')
        self.win_root.iconbitmap(self.LOGO)
        self.win_root.geometry('320x450+100+150')
        self.win_root.resizable(0,0)
        
        self.frame_f_wr()
        self.frame_lb_wr()
        self.frame_b_wr()
        self.show_all_contacts()
        self.win_root.mainloop()

    def frame_f_wr(self):
        '''Создание фрейма frame_f и его компонентов.'''
        self.photo_find = PhotoImage(file = self.FIND) # Изображение для кнопки "Поиск".
        self.photoimage_find = self.photo_find.subsample(25, 25) # Уменьшение изображения.
        
        self.frame_f = Frame(self.win_root, relief=GROOVE, borderwidth=2)
        self.frame_f.pack(side=TOP, fill=X, padx=5, pady=3)
        
        self.entry_frame_f = Entry(self.frame_f, width=26, fg='blue',
                                   font=('Calibri', 14, 'italic'))
        self.entry_frame_f.pack(side=LEFT, padx=4)

        self.btn_frame_f = Button(self.frame_f, relief=FLAT,                                  
                                  image=self.photoimage_find,
                                  command=self.start_find)
        self.btn_frame_f.pack(side=RIGHT, padx=2, pady=2)

        self.entry_frame_f.bind('<Return>', self.start_find_enter)

    def frame_lb_wr(self):
        '''Создание фрейма frame_lb и его компонентов.'''
        self.frame_lb = Frame(self.win_root, relief=GROOVE, borderwidth=2)
        self.frame_lb.pack(fill=X, padx=5, pady=2)

        self.scroll_listbox = Scrollbar(self.frame_lb)
        self.scroll_listbox.pack(side=RIGHT, fill=Y)

        self.listbox_frame_lb = Listbox(self.frame_lb, width=20, height=15,
                                        selectmode=EXTENDED, fg='black',
                                        font=('Courier New', 14, 'bold'),
                                        yscrollcommand=self.scroll_listbox.set)
        self.listbox_frame_lb.pack(fill=X, padx=2, pady=2)

        self.scroll_listbox.config(command=self.listbox_frame_lb.yview)

        self.listbox_frame_lb.bind('<Double-Button-1>', self.show_one_contact)
        self.listbox_frame_lb.bind('<Return>', self.show_one_contact)


    def frame_b_wr(self):
        '''Создание фрейма frame_b и его компонентов.'''
        self.frame_b = Frame(self.win_root, relief=GROOVE, borderwidth=2)
        self.frame_b.pack(side=BOTTOM, fill=X, padx=5, pady=3)

        self.photo_update = PhotoImage(file = self.UPDATE) # Изображение для кнопки "Обновить".
        self.photoimage_update = self.photo_update.subsample(20, 20) # Уменьшение изображения.  

        self.photo_add = PhotoImage(file = self.ADD) # Изображение для кнопки "Добавить".
        self.photoimage_add = self.photo_add.subsample(25, 25) # Уменьшение изображения.  

        self.photo_exit = PhotoImage(file = self.EXIT) # Изображение для кнопки "Выход".
        self.photoimage_exit = self.photo_exit.subsample(25, 25) # Уменьшение изображения.  
        

        self.btn_show_frame_b = Button(self.frame_b, relief=FLAT, width=20, height=20,
                                       image=self.photoimage_add,
                                       command=self.add_one_contact)
        self.btn_show_frame_b.pack(side=LEFT, padx=40, pady=2)

        self.btn_show_frame_b = Button(self.frame_b, relief=FLAT, width=20, height=20,
                                       image=self.photoimage_update,
                                       command=self.update)
        self.btn_show_frame_b.pack(side=LEFT, padx=30, pady=2)

        self.btn_exit_frame_b = Button(self.frame_b, relief=FLAT, width=20, height=20,
                                       image=self.photoimage_exit,
                                       command=self.close_win_root)
        self.btn_exit_frame_b.pack(side=RIGHT, padx=40, pady=2)    
        
    def show_all_contacts(self):
        '''Вызывается при запуске программы "Контакты".
           Чтение контактов из txt-файла. Вывод списка
           фамилий с буквами алфавита в виджет Listbox.'''          
        self.read_contact_txt_list() # Вызов функции для получения списка контактов из txt-файла.
                                # В результате выполнения Функциии формируется
                                # список контактов data_list_all.                                                 
        if self.data_list_all: # Если список контактов не пустой продолжается действие программы.                                                   
            self.alphabet_order_list() # Вызов Функции для формирования списка с буквами алфавита.
                                       # Контакты в списке data_list_all уже расположены в алфавитном порядке.                                                                            
            self.print_contacts() # Вызов функции для вывода в виджет Listbox списка фамилий с алфавитом.
        else: # Иначе, если список контактов пустой.
            # Открывается диалоговое окно.
            answer_no_contacts = messagebox.askyesno(title='Список контактов пуст!', 
                                                     message='Добавить контакт?')
            if answer_no_contacts: # Если нажата кнопка 'Да'. 
                self.add_one_contact() # Вызов функции для открытия окна "Новый контакт".

    def read_contact_txt_list(self):
        '''Получение данных из текстового файла. Обработка данных. 
           Результат выполнения - список контактов data_list_all (Глобальная переменная).
           Область видимости переменной data_str функция read_contact_txt_list().'''
        sentence_1 = "Отсутствует файл 'contact.txt'."      # 
        sentence_2 = " Добавьте файл 'contact.txt' в папку" # Длинное информационное  
        sentence_3 = " с программой или создайте файл"      # сообщение разделено 
        sentence_4 = " 'contact.txt'."                      # на 5 частей.
        sentence_5 = " Создать файл 'contact.txt'?"         #
        sentence = sentence_1 + sentence_2 + sentence_3 + sentence_4 + sentence_5
        try: # Обработка исключения для случая отсутствия файла 'contact.txt'.
            file_txt_r = open(self.FILE_NAME_TXT, 'r') # Открытие txt-файла для чтения данных.
            self.data_list_all = [] # Переменной для хранения списка контактов присваивается пустой список.                              
            while True: # Бесконечный цикл для обработки контактов построчно.
                data_str = file_txt_r.readline() # Получение строки с контактом.                                             
                if data_str == '': # Если строка пустая то выход из цикла. Это значит, 
                                   # что в txt-файле закончились строки с конактами.
                    file_txt_r.close()  # Закрытие текстового файла.
                    break               # Выход из цикла.
                self.data_list_all.append(data_str) # С каждым проходом цикла в список добавляется контакт.
        except Exception: # Исключение в случае возникновения ошибки.
            # Вывод инвормационного сообщения 'sentence'.
            answer_txt = messagebox.askyesno(title='Нет связи с базой данных', message=sentence)
            if answer_txt: # Если нажата кнопка "Да". Создать txt-файл 'contact.txt'.
                self.write_contact_txt('') # Вызывается функция для создания txt-файла. Передаётся аргумент
                                      # пустая строка для создания пустого файла 'contact.txt'.
            else: # Иначе, если нажата кнопка "Нет".
                self.win_root.destroy() # Закрытие окна win_root.
                sys.exit() # Выход из программы "Контакты".

    def write_contact_txt(self, contact):
        '''Запись контакта в текстовый файл. 
           Отрытие файла. Запись. Закрытие файла.'''
        if contact == '': # Если пустая строка.
            file_txt = open(self.FILE_NAME_TXT, 'a') # Создание txt-файла.
        else: # Если не пустая строка.
            file_txt = open(self.FILE_NAME_TXT, 'a') # Открытие txt-файла.
            file_txt.write(contact) # Запись контакта в txt-файл.        
        file_txt.close() # Закрытие txt-файла.

    def alphabet_order_list(self):
        '''Формирование списка контактов data_list_all_alph с буквами алфавита.
           Область видимости переменной data_str функция alphabet_order_list().'''
        for data_str in self.data_list_all: # Для строки контакта data в списке data_list_all.
            if data_str[0] == self.letter: # Если первая буква фамилии в строке контакта
                                      # равна значению переменной letter. 
                self.data_list_all_alph.append(data_str) # В список data_list_all_alph
                                                         # добавляется строка контакта data_str.
            else: # Иначе, если первая буква фамилии не равна значению переменной letter.
                self.letter = data_str[0] # Переменной letter присваивается первая буква фамилии.
                self.data_list_all_alph.append(data_str[0]) # В список data_list_all_alph добавляется
                                                            # первая буква фамилии контакта data_str[0].
                self.data_list_all_alph.append(data_str) # После буквы в список data_list_all_alph
                                                         # добавляется строка контакта data_str.

    def print_contacts(self):
        '''Вывод в виджет Listbox списка контактов в алфавитном порядке с буквами алфавита.
           Область видимости переменной data_str функция print_contacts().'''
        self.listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
        for data_str in self.data_list_all_alph: # Для строки контакта data_str в списке data_list_all_alph.
            if len(data_str) == 1: # Если длина строки контакта равна одному символу, значит это буква.
                self.listbox_frame_lb.insert(END, f' {data_str}') # Вывод буквы в виджет Listbox.
                self.listbox_frame_lb.itemconfig(END, fg='green') # Буква окрашивается в зелёный цвет.
            else: # Иначе если длина контакта больше одного символа.
                  # Вывод на печать фамилии контакта. Вызывается функция data_str_split(data_str)
                  # для разделения элементов контакта и выбора из списка 0-го элемента (фамилии).
                self.listbox_frame_lb.insert(END, f' {self.data_str_split(data_str)[0]}') 
                self.listbox_frame_lb.itemconfig(END, fg='black') # Фамилия контакта окрашивается в чёрный цвет.

    def data_str_split(self, data_str):
        '''Разделение строки контакта на элементы по символу
           "&". Формирование списка элементов.'''
        data_list = data_str.split('&')
        return data_list

    def add_one_contact(self):
        ContactCard('', 'Добавить')

    def start_find_enter(self, event):
        '''Обрабатывает событие нажатия клавиши
          'Enter' после ввода элемента поиска.'''
        self.start_find() # Вызов функции для начала поиска.
        
    def start_find(self):
        '''Метод-обработчик события - нажатие кнопки "Поиск".'''
        self.find_list = [] # Значение переменной для хранения списка с найденными
                            # контактами - обнуляется (присваивается пустой список)
        find_str = self.entry_frame_f.get() # Переменной find_str присваивается строка
                                            # (Элемент поиска) введённая в виджет Entry.
        if find_str != '': # Если полученная из виджета Entry строка не пустая.
            find_str_lower = find_str.lower() # Переменной find_str_lower присваивается
                                              # строка элемента для поиска преобразованная
                                              # к нижнему регистру.
            for data_str in self.data_list_all: # Для строки контакта в списке контактов.
                data_str_lower = data_str.lower() # Переменной data_str_lower присваивается
                                                  # строка контакта, полученная их текстового файла,
                                                  # преобразованная к нижнему регистру.
                if data_str_lower.find(find_str_lower) != - 1: # Вызов функции find(). 
                                                               # В строке контакта data_str_lower
                                                               # осуществляется поиск совпадений
                                                               # с элементом поиска find_str_lower.
                                                               # Если функция возвращает не "- 1" 
                                                               # - выполняется тело условия.
                                                               # Если функция возвращает "- 1"
                                                               # - совпадений нет, тело условия
                                                               # пропускается.
                    self.find_list.append(data_str) # К списку find_list добавляется строка контакта
                                                    # data_str, в которой есть совпадения.                                       
            self.print_contacts_find() # Вызов функции для вывода в виджет Listbox
                                       # контактов из списка find_list.
            self.entry_frame_f.delete(0, END) # Очистка поля для ввода элемента поиска.

    def print_contacts_find(self):
        '''Выводит в виджет Listbox найденный контакты.
           Если совпадений нет открывает окно с информационным сообщением'''
        if self.find_list == []: # Если список контактов поиска пуст.
                                 # Открытие окна с информационным сообщением.
            answer = messagebox.showinfo('Сообщение', ' Совпадений нет. Измените элемент для поиска')
            self.update() # Вызов функции для обновления данных в виджете Listbox. 
        else: # Иначе, если список контактов поиска не пустой.
            self.listbox_frame_lb.delete(0, END) # Очистка виджета Listbox.
            for data_str_find in self.find_list: # Для строки контакта в списке контактов поиска.
                # Вывод в виджет Listbox фамилии из контакта.
                self.listbox_frame_lb.insert(END, f' {self.data_str_split(data_str_find)[0]}')
                # Фамилия контакта поиска окрашивается в синий цвет.
                self.listbox_frame_lb.itemconfig(END, fg='blue')

    def update(self):
        '''Обновление списка контактов'''        
        self.data_str = ''           # Обнуление.
        self.find_list = []          # Обнуление.
        self.data_list_all = []      # Обнуление.
        self.letter = ''             # Обнуление.
        self.data_list_all_alph = [] # Обнуление.    
        self.show_all_contacts() # Вызов метода для вывода в
                                 # виджет listbox списка 
                                 # фамилий контактов.

    def close_win_root(self):
        '''Функция-обработчик события - закрытие окна win_root.'''
        self.win_root.destroy() # Вызов метода для закрытия 
                                # окна win_root.

    def show_one_contact(self, event):
        '''Открытие окна win_show и отображение данных выбранного контакта'''
        number_item = self.listbox_frame_lb.curselection()[0] # Когда выбран элемент списка в виджете Listbox,
                                                              # то есть осуществлён двойной клик мышкой по
                                                              # фамилии или нажата клавиша 'Enter' вызывается
                                                              # метод curselection(). Метод возвращает кортеж.
                                                              # Нулевым элементом кортежа является номер (индекс)
                                                              # элемента в списке data_list_all_alph или find_list.
        if self.find_list != []: # Если список поиска не пустой.
            self.data_str = self.find_list[number_item] # Переменной data_str присваивается
                                                        # строка контакта из списка find_list
                                                        # с индексом number_item.
            ContactCard('find_list ---> ' + self.data_str, 'Показать') # Вызов класса ContactCard. 
        else: # Иначе, если список поиска пустой.
            data_str_alph = self.data_list_all_alph[number_item] # Переменной data_str_alph присваивается
                                                                 # строка из списка data_list_all_alph
                                                                 # с индексом number_item.                                                    
            if len(data_str_alph) > 1: # Если длина строки больше 1, значит это не буква алфавита.
                self.data_str = data_str_alph # Переменной data_str присваивается 
                                              # значение data_str_alph.
                ContactCard('data_list_all_alph ---> ' + self.data_str, 'Показать') # Вызов класса ContactCard.

    
if __name__ == '__main__':
    WinRoot()



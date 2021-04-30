from sharedata import *
from editphoto import *

class ContactCard:
    '''Формирует окно "Контакт" и отображает данные и фотографию.'''
    def __init__(self, master, btn_addcont_text):
        self.win_show = Toplevel(master)
        self.win_show.iconbitmap(ShareData.LOGO)
        self.win_show.geometry('625x380+450+150')
        self.win_show.resizable(0,0)
        self.win_show.focus_set()
#        self.list_sort = []
        self.btn_addcont_text = btn_addcont_text
        self.frame_c_ws()
        self.frame_jp_ws()
        if self.btn_addcont_text == 'Сохранить':
            self.show_contact()
        elif self.btn_addcont_text == 'Добавить':
            self.add_contact()
        self.appear_temp()
        self.win_show.protocol('WM_DELETE_WINDOW', self.close_win_show)
        
    def frame_c_ws(self):
        '''Создание фрейма frame_c_ws и его компонентов.'''
        self.frame_c = Frame(self.win_show, relief=GROOVE, borderwidth=2)
        self.frame_c.pack(side=LEFT, fill=BOTH, padx=5, pady=3)

        self.label_lastname = Label(self.frame_c, text='Фамилия:')
        self.label_lastname.pack()

        self.entry_lastname = Entry(self.frame_c, font=('Courier New', 12), justify=CENTER)
        self.entry_lastname.pack(fill=X, padx=10)

        self.entry_lastname.bind('<Key>', self.bg_change_lastname) # Для изменения цвета фона.

        self.label_firstname = Label(self.frame_c, text='Имя (Отчество):')
        self.label_firstname.pack()

        self.entry_firstname = Entry(self.frame_c, font=('Courier New', 12), justify=CENTER)
        self.entry_firstname.pack(fill=X, padx=10)

        self.entry_firstname.bind('<Key>', self.bg_change_label) # Для изменения цвета фона.

        self.label_address = Label(self.frame_c, text='Адрес:')
        self.label_address.pack()

        self.entry_address = Entry(self.frame_c, font=('Courier New', 12), justify=CENTER)
        self.entry_address.pack(fill=X, padx=10)

        self.entry_address.bind('<Key>', self.bg_change_label) # Для изменения цвета фона.

        self.label_phonenumber = Label(self.frame_c, text='Телефонный номер:')
        self.label_phonenumber.pack()

        self.entry_phonenumber = Entry(self.frame_c, font=('Courier New', 12), justify=CENTER)
        self.entry_phonenumber.pack(fill=X, padx=10)

        self.entry_phonenumber.bind('<Key>', self.bg_change_phonenumber) # Для изменения цвета фона.

        self.label_email = Label(self.frame_c, text='Электронный адрес:')
        self.label_email.pack()

        self.entry_email = Entry(self.frame_c, font=('Courier New', 12), justify=CENTER)
        self.entry_email.pack(fill=X, padx=10)

        self.entry_email.bind('<Key>', self.bg_change_label) # Для изменения цвета фона.

        self.label_addinform = Label(self.frame_c, text='Дополнительная информация:')
        self.label_addinform.pack()

        self.entry_addinform = Entry(self.frame_c, font=('Courier New', 12), justify=CENTER)
        self.entry_addinform.pack(fill=X, padx=10)

        self.entry_addinform.bind('<Key>', self.bg_change_label) # Для изменения цвета фона.

        self.label_datetime_write = Label(self.frame_c, text='')
        self.label_datetime_write.pack()
    
        self.show_datetime_write = Label(self.frame_c, fg='green', text='')
        self.show_datetime_write.pack()

        self.show_write_save = Label(self.frame_c, fg='green', text='')
        self.show_write_save.pack()
        
        # Событие нажатия кнопки "Добавить" в окне "Добавить контакт"
        # обрабатывается функцией add_contact_gui().
        self.btn_addcont = Button(self.frame_c, width=10, text='')
        self.btn_addcont.pack(side=LEFT, anchor=SW, padx=1, pady=5)
            
        self.btn_delcont = Button(self.frame_c, width=10, text='')
        self.btn_delcont.pack(side=LEFT, anchor=S, padx=1, pady=5) 

        if self.btn_addcont_text == 'Сохранить':
            self.win_show.title('Контакт')
            self.btn_addcont['text'] = self.btn_addcont_text
            self.btn_addcont.config(command=self.save_contact_change)
            self.btn_delcont['text'] = 'Удалить'
            self.btn_delcont.config(command=self.delete_contact)
            self.label_datetime_write.config(text='Дата и время записи контакта:')
        else:
            self.win_show.title('Новый контакт')
            self.btn_addcont['text'] = self.btn_addcont_text
            self.btn_addcont.config(command=self.save_contact_add)
            self.btn_delcont['text'] = 'Очистить'
            self.btn_delcont.config(command=self.clear_field)
            self.label_datetime_write.config(text='')
    
        # Событие нажатия кнопки "Закрыть" в окне "Добавить контакт"
        # обрабатывается функцией close_win_add().
        self.btn_close_addcont = Button(self.frame_c, width=10, text='Закрыть',
                                        command=self.close_win_show)
        self.btn_close_addcont.pack(side=LEFT, anchor=SE, padx=1, pady=5)

    def frame_jp_ws(self):
        '''Создание фрейма frame_jp_ws и его компонентов.'''
        self.frame_jp = Frame(self.win_show, relief=GROOVE, borderwidth=2)
        self.frame_jp.pack(side=RIGHT, fill=BOTH, expand=1, padx=5, pady=3)

        self.canvas_jp = Canvas(self.frame_jp, width=300, height=300)
        self.canvas_jp.pack(fill=BOTH, expand=1)

    def show_contact(self):
        '''Вывод данных контакта и фотографии в окно win_show.'''
        data_list = ShareData.data_str_split(ShareData.data_str) # Вызов функции data_str_split()
                                                                 # для разделения элементов контакта 
                                                                 # из глобальной переменной data_str
                                                                 # и формирования списка элементов.         
        self.d = data_list[6].split(' ')[0] # Получение даты создания контакта для поиска
                                            # фотографии в папке image.
        self.lastname = data_list[0] # Получение фамилии для поиска фотографии в папке image.

        self.entry_lastname.insert(0, data_list[0])     # Вставить фамилию в поле Entry.
        self.entry_firstname.insert(0, data_list[1])    # Вставить имя в поле Entry.
        self.entry_address.insert(0, data_list[2])      # Вставить адрес в поле Entry.
        self.entry_phonenumber.insert(0, data_list[3])  # Вставить телю номер в поле Entry.
        self.entry_email.insert(0, data_list[4])        # Вставить email в поле Entry.
        self.entry_addinform.insert(0, data_list[5])    # Вставить доп. информацию в поле Entry.
        self.show_datetime_write['text'] = data_list[6] # Вставить дату и время создания 
                                                        # контакта в поле Entry. 
        self.click_photo(self.get_photo())

    def close_win_show(self):
        '''Функция-обработчик события - закрытие окна win_show.'''
        ShareData.open_win_show_contact_flag = 0
        ShareData.data_str = ''
        try:
            os.remove(ShareData.TEMP)    
            self.win_show.destroy()
            ShareData.photo_save_temp = 0
        except Exception:
            self.win_show.destroy()
            ShareData.photo_save_temp = 0
   
    def bg_change_lastname(self, key):
        '''Изменение фона виджета Entry для ввода фамилии.'''
        if self.entry_lastname['bg'] != 'white':
            self.entry_lastname.delete(0, END)
        self.show_write_save['text'] = ''
        self.entry_lastname['bg'] = 'white'
        self.entry_lastname['fg'] = 'black'    

    def bg_change_phonenumber(self, key):
        '''Изменение фона виджета Entry для ввода телефонного номера'''
        if self.entry_phonenumber['bg'] != 'white':
            self.entry_phonenumber.delete(0, END)
        self.show_write_save['text'] = ''
        self.entry_phonenumber['bg'] = 'white'
        self.entry_phonenumber['fg'] = 'black'    

    def bg_change_label(self, key):
        ''''''
        self.show_write_save['text'] = ''

    def save_contact_share(self, change_def):
        ''''''
        self.lastname = self.get_entry_contact()[0]
        self.phonenumber = self.get_entry_contact()[3]
        self.d = self.get_entry_contact()[6]
        self.contact = self.get_entry_contact()[9]
        LN = 'Введите фамилию'
        PN = 'Введите тел.номер'
        # Если поля ввода "Введите фамилию:" и
        # "Введите телефонный номер" не пустые.
        if self.lastname != '' and self.phonenumber != '' and self.lastname != LN and self.phonenumber != PN:
            if change_def == 'cch':
                self.change_contact(self.contact) # Запись изменённого контакта вместо старого  в список контактов.
            elif change_def == 'cad':
                ShareData.data_list_all.append(self.contact)
            ShareData.data_list_all = sorted(ShareData.data_list_all)# Выполняется сортировка списка в алфавитном порядке.            
            self.write_list_txt() # Вызов функции для записи контакта в txt-файл.
            self.save_photo()
            self.show_write_save['fg'] = 'red'
            self.show_write_save['text'] = 'ЗАПИСАНО В БАЗУ ДАННЫХ'
        elif self.lastname == '' and self.phonenumber == '':
            self.entry_lastname['bg'] = '#ffd2d2'
            self.entry_lastname['fg'] = '#a0a0a0'
            self.entry_lastname.insert(0, 'Введите фамилию')
            self.entry_phonenumber['bg'] = '#ffd2d2'
            self.entry_phonenumber['fg'] = '#a0a0a0'
            self.entry_phonenumber.insert(0, 'Введите тел. номер')
        elif self.lastname == '': # Иначе если поля ввода пустые вывести информационное сообщение.
            self.entry_lastname['bg'] = '#ffd2d2'
            self.entry_lastname['fg'] = '#a0a0a0'
            self.entry_lastname.insert(0, 'Введите фамилию')
        elif self.phonenumber == '':        
            self.entry_phonenumber['bg'] = '#ffd2d2'
            self.entry_phonenumber['fg'] = '#a0a0a0'
            self.entry_phonenumber.insert(0, 'Введите тел. номер')
        ShareData.update_save_cont = 1
               
    def save_contact_change(self):
        '''Для сохранения контакта. Обработка 
           данных. Формирование строки контакта.
           Запись контакта в текстовый файл.'''
        self.delete_photo() # Пока ещё в переменных self.lastname, self.phonenumber и т.д.
                            # записаны данные контакта до изменения вызывается функция для удаления фото.
        self.save_contact_share('cch')
                    
    def change_contact(self, contact):
        ''''''
        ShareData.data_list_all[self.find_number_element()] = self.contact
     
    def delete_contact(self):
        '''Функция-обработчик события - нажатие кнопки "Удалить".'''
        answer_del_contact = messagebox.askyesno(title='Удаление контакта',
                                                 message='Вы действительно хотите удалить контакт?')
        if answer_del_contact: # Если вы действительно хотите удалить контакт.
            self.del_cont_in_list() # Вызов функции для удаления контакта из
                                    # списка контактов data_list_all.
            self.write_list_txt() # Вызов функции для записи списка контактов в txt-файл.
            self.delete_photo()
            self.close_win_show()
            answer_del_cont = messagebox.showinfo(title='Удаление контакта',
                                                  message=f'Контакт "{self.lastname}" удалён из базы данных.')
            ShareData.data_str = ''
            ShareData.update_save_cont = 1

    def del_cont_in_list(self):
        '''Удаление контакта из списка контактов по номеру (индексу).'''
        ShareData.data_list_all.pop(self.find_number_element()) # Вызов метода list.pop() для 
                                                                # удаления контакта из списка                                                                 
                                                                # контактов по номеру (индексу).

    def find_number_element(self):
        '''Определяет номер (индекс) контакта в списке контактов.
           ShareData.data_str - переменная в которой хранится
           отображаемый в окне win_show контакт. Переменная
           data_str видна только в этой функции.'''
        n = -1 # Так как первый индекс первого элемента списка 
               # равен 0, а в цикле организован счётчик элементов
               # списка ShareData.data_list_all, то начальное
               # значение счётчика равно -1.
        for data_str in ShareData.data_list_all: # Для data_str в ShareData.data_list_all.
            n += 1 # При каждой итерации цикла значение счётчика увеличивается на 1.
                   # При первой итерации цикла значение счётчика равно 0.
            if data_str == ShareData.data_str: # Если контакт в списке найден.           
                break # Выход из цикла.
        return n # Функция возвращает номер(индекс) контакта в списке контактов.

    def write_list_txt(self):
        '''Удаление старого txt-файла 'contact.txt' и
           создание нового txt-файла 'contact.txt' из
           нового списка контактов.'''
        os.remove(ShareData.FILE_NAME_TXT) # Удаление старого 'contact.txt'.
        for data_str in ShareData.data_list_all: # Для строки контакта в списке контактов.
            ShareData.write_contact_txt(data_str) # Создание нового файла 'contact.txt' и 
                                                  # построчная запись контактов в текстовый файл. 

    def delete_photo(self):
        ''''''
        try:
            os.remove(f'image\{self.lastname}{self.d}.png') # Удаление фото контакта.
        except Exception: # Исключение.
            img_show = Image.open(ShareData.NOFOTO)
        
    def get_entry_contact(self):
        '''Получение из виджетов Entry данных контакта.
           Получение текущих даты и времени.
           формирование списка get_data.'''
        lastname = self.entry_lastname.get()       # Получение "Фамилии" из окна ввода Entry.
        firstname = self.entry_firstname.get()     # Получение "Имени" из окна ввода Entry.    
        address = self.entry_address.get()         # Получение "Адреса" из окна ввода Entry.
        phonenumber = self.entry_phonenumber.get() # Получение "Тел. ном." из окна ввода Entry.
        email = self.entry_email.get()             # Получение "Эл. адреса" из окна ввода Entry.
        addinform = self.entry_addinform.get()     # Получение "Доп. инф." из окна ввода Entry.

        # Получение даты и времени из ОС и присвоение
        # в виде строки переменной dt.
        d = datetime.now().strftime('%d.%m.%Y')
        t = datetime.now().strftime(' %H:%M:%S')
        dt = d + t
    
        contact = lastname + '&' + firstname + '&' + \
                  address + '&' + phonenumber + '&' + \
                  email + '&' + addinform + '&' + dt + '\n'

        self.get_data = [lastname, firstname, address, phonenumber, email, addinform, d , t, dt, contact]
        return self.get_data

    def click_photo(self, img_show):
        ''''''
        self.canvas_jp.image = ImageTk.PhotoImage(img_show)
        ttt = self.canvas_jp.create_image(50, 50, anchor=NW, image=self.canvas_jp.image, tag='jpgg')
        self.canvas_jp.tag_bind(ttt,'<Button-1>', self.open_win_phedit)

    def appear_temp(self):
        ''''''
        if ShareData.photo_save_temp == 1:
            img_show = Image.open(ShareData.TEMP)
            self.click_photo(img_show)
        self.canvas_jp.after(100, self.appear_temp)
    
    def get_photo(self):
        ''''''
        try:
            img_show = Image.open(f'image\{self.lastname}{self.d}.png')        
        except Exception: # Исключение.
            img_show = Image.open(ShareData.NOFOTO)
        return img_show    

    def save_photo(self):
        '''Редактор фото сохранил обрезанную
           фотографию в переменной temp. Эта функция
           открывает файл temp и сохраняет фотографию
           в папке image.'''
        try: # Обработка исключения для случая отсутствия файла 'temp.png'.
            img_temp = Image.open(ShareData.TEMP) # Открытие файла 'temp.png'.
            img_temp.save(f'image\{self.lastname}{self.d}.png') # Сохранение файла с фото в папке 'image'.
            ShareData.photo_save_temp = 0
            os.remove(ShareData.TEMP) # Удаление файла 'temp.png'.            
        except Exception: # Исключение в случае возникновения ошибки. Отсутствует файл 'temp.png'.
            img_temp = Image.open(ShareData.NOFOTO) # Открытие файла 'nofoto.png'.
            img_temp.save(f'image\{self.lastname}{self.d}.png') # Сохранение файла без фото в папке 'image'.

    def clear_field(self):
        '''Функция-обработчик события - нажатие кнопки "Очистить".'''
        self.entry_lastname.delete(0, END)
        self.entry_firstname.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_phonenumber.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_addinform.delete(0, END)
        self.show_datetime_write['text'] = ''
        img_show = Image.open(ShareData.NOFOTO)
        self.canvas_jp.image = ImageTk.PhotoImage(img_show)
        ttt = self.canvas_jp.create_image(50, 50, anchor=NW, image=self.canvas_jp.image, tag='jpgg')
        self.canvas_jp.tag_bind(ttt,'<Button-1>', self.open_win_phedit)

    def add_contact(self):
        self.click_photo(Image.open(ShareData.NOFOTO))
       
    def save_contact_add(self):
        '''Сохранение нового контакта в txt-файл.'''
        self.save_contact_share('cad')
        
    def open_win_phedit(self, event):
        ''''''
        foto_path_open = self.open_file_foto()
        if foto_path_open:
            img = Image.open(foto_path_open)
            EditPhoto(self.win_show, img)
        else:
            messagebox.showinfo('Выбор фотографии', 'Фотография не выбрана')

    def open_file_foto(self):
        '''Получение пути к файлу в виде строки для его открытия через диалоговое окно.
           Возвращает строку с путём к файлу. Пример: 'C:/Users/Downloads/contact.txt'.'''
        foto_path_open = filedialog.askopenfilename(title='Выбор фотографии',
                                                    filetypes=(('Все файлы изображений','*.jpg; *.png'),
                                                               ('Все файлы', '*.*')))
        return foto_path_open   

   
if __name__ == '__main__':
    win_test = Tk()
    print('Выберите режим тестирования')
    choice = input('Тестирование события: "Показать контакт"- 1 "Добавить контакт"- 2: ')
    if choice == '1':
        ShareData.data_str = 'Тестер&Тест Тестович&г. Тестовый, пер. Тест, д.999&15-15-15&tester@russia.ru&Тестер&12.12.2020 15:15:15'
        ContactCard(win_test, 'Сохранить')
    elif choice == '2': 
        ContactCard(win_test, 'Добавить')



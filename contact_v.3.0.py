from tkinter import *

LOGO = 'logotip.ico'          # Константа.
FILE_NAME_TXT = 'contact.txt' # Константа.
FIND = 'find.png'             # Константа.
UPDATE = 'update.png'         # Константа.
ADD = 'add.png'               # Константа.
EXIT = 'exit.png'             # Константа.

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

btn_update_frame_b = Button(frame_b, relief=FLAT, width=20, height=20,
                          image=photoimage_update)
btn_update_frame_b.pack(side=LEFT, padx=30, pady=2)

btn_exit_frame_b = Button(frame_b, relief=FLAT, width=20, height=20,
                          image=photoimage_exit)
btn_exit_frame_b.pack(side=RIGHT, padx=40, pady=2)

win_root.mainloop()

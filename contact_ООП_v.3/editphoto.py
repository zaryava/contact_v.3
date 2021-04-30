from sharedata import *

class EditPhoto:
    '''Редактирование фотографии контакта.'''
    def __init__(self, master, img):
        self.win_phedit = Toplevel(master)        
        self.win_phedit.title('Редактор фото')
        self.win_phedit.iconbitmap(ShareData.LOGO)
        self.img = img
        self.win_phedit.focus_set()
        self.ph_canvas_wp()
        self.btn_wp()
                    
    def ph_canvas_wp(self):
        '''Изменение размеров фотографии, её размещение в виджете Canvas.
           Создание оранжевой рамки поверх фотографии.'''
        self.ph_canvas = Canvas(self.win_phedit, width=400, height=450, bd=0, highlightthickness=0)
        self.ph_canvas.pack()
        
        width_j = self.img.size[0]  # Получение исходного размера по горизонтали. 
        height_j = self.img.size[1] # Получение исходного размера по вертикали.
        
        if width_j == height_j: # Если фотография квадратная.
            self.i = 0 # Аргументу i присваивается значение 0.
            self.out_e = self.img.resize((250,250)) # Вызывается метод для изменения размера фото.
        elif width_j > height_j: # Если фотография вытянута по горизонтали.
            self.i = 1 # Аргументу i присваивается значение 1.
            h = height_j/250 # Определение коэффициента уменьшения.
            wh = round(width_j/h) # Определение конечного размера. 
            self.out_e = self.img.resize((wh,250)) # Вызывается метод для изменения размера фото.
        elif height_j > width_j: # Если фотография вытянута по вертикали.
            self.i = 2 # Аргументу i присваивается значение 2.
            w = width_j/250 # Определение коэффициента уменьшения.
            hw = round(height_j/w) # Определение конечного размера.
            self.out_e = self.img.resize((250,hw)) # Вызывается метод для изменения размера фото.
    
        self.width_jz = self.out_e.size[0]  # Получение конечного размера по горизонтали.
        self.height_jz = self.out_e.size[1] # Получение конечного размера по вертикали.

        # Координаты рамки определяются исходя из расположения её посередине фотографии.
        if self.i == 0 or self.i == 1:
            # Начальные координаты рамки для квадратного
            # и горизонтального изображения.
            x1 = (self.width_jz - 250)/2
            y1 = 0
            x2 = x1
            y2 = 249
            x3 = x1 + 250
            y3 = 249
            x4 = x1 + 250
            y4 = 0    
        else:
            # Начальные координаты рамки для
            # вертикального изображения.
            x1 = 0
            y1 = (self.height_jz - 250)/2
            x2 = 0
            y2 = y1 + 249
            x3 = 249
            y3 = y1 + 249
            x4 = 249
            y4 = y1
    
        self.ph_canvas.image = ImageTk.PhotoImage(self.out_e, master=self.win_phedit)
        self.ph_canvas.create_image(0, 0, image=self.ph_canvas.image, anchor=NW)

        self.ph_canvas.config(width=self.width_jz, height=self.height_jz)

        self.c_id = self.ph_canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4,
                                                  fill='', outline='orange', width=3)

        self.ph_canvas.bind_all('<KeyPress-Up>', self.move_ramka)
        self.ph_canvas.bind_all('<KeyPress-Down>', self.move_ramka)
        self.ph_canvas.bind_all('<KeyPress-Left>', self.move_ramka)
        self.ph_canvas.bind_all('<KeyPress-Right>', self.move_ramka)

    def btn_wp(self):
        '''Создание кнопок "ОК" и "Отмена".'''
        self.btn_save = Button(self.win_phedit, width=15, height=2,text='ОК', command=self.ph_ok)
        self.btn_save.pack(side=LEFT, padx=20, pady=5)

        self.btn_cancel = Button(self.win_phedit, width=15, height=2,text='Отмена', command=self.ph_cancel)
        self.btn_cancel.pack(side=RIGHT, padx=20, pady=5)
   
    def ph_cancel(self):
        '''Метод-обработчик события - нажатие кнопки "Отмена".'''
        self.win_phedit.destroy()

    def ph_ok(self):
        '''Метод-обработчик события - нажатие кнопки "ОК".'''
        xy_list = self.ph_canvas.coords(self.c_id) # Получает координаты рамки.
        cropped = self.out_e.crop((xy_list[0], xy_list[1], xy_list[4], xy_list[5])) # Обрезка фото по рамке.
        cropped.save(ShareData.TEMP) # Сохранение обрезанного фото во временный файл.
        ShareData.photo_save_temp = 1
        self.win_phedit.destroy()

    def move_ramka(self, event):
        '''Для обработки действий нажатия кнопок стрелок.
           Движение рамки в зависимости от нажатой стрелки.'''
        xy_list = self.ph_canvas.coords(self.c_id) # Получает координаты рамки.
        if event.keysym == 'Up' and self.i == 2 and xy_list[1] > 1:
            self.ph_canvas.move(self.c_id, 0, -1)
        elif event.keysym == 'Down' and self.i == 2 and xy_list[3] < self.height_jz - 2:
            self.ph_canvas.move(self.c_id, 0, 1)
        elif event.keysym == 'Left' and self.i == 1 and xy_list[0] > 1 :
            self.ph_canvas.move(self.c_id, -1, 0)
        elif event.keysym == 'Right' and self.i == 1 and xy_list[4] < self.width_jz - 3:
            self.ph_canvas.move(self.c_id, 1, 0)        














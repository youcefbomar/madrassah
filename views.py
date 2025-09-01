from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLabel, QFrame,QSizePolicy,
                              QStackedWidget, QScrollArea, QLineEdit, QTableWidget,
                              QTableWidgetItem, QHeaderView, QAbstractItemView, QDialog,
                              QComboBox, QTimeEdit, QSpinBox)
from PySide6.QtCore import Qt,QSize,QTime
from PySide6.QtGui import QIcon, QCursor
import sys

from services import *



class MainPage(QWidget):

    def set_active_button(self, index):

        for i, btn in enumerate(self.nav_buttons):
            btn.setProperty("active", i == index)
            btn.setChecked(i == index)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

            self.stacked_widget.setCurrentIndex(index)

            if i == index:
                btn.setCursor(QCursor(Qt.ArrowCursor))  
            else :
                btn.setCursor(QCursor(Qt.PointingHandCursor))


    def card_maker(self, title, content) :
        card = QWidget()
        card.setMinimumSize(200,100)
        card.setProperty("class","card")
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create title label
        title_label = QLabel(title)
        title_label.setObjectName('card_title')
        title_label.setAlignment(Qt.AlignCenter)
        
        # Create content label
        content_label = QLabel(content)
        content_label.setObjectName('card_content')
        content_label.setAlignment(Qt.AlignCenter)
        title_label.setFixedHeight(30)
        content_label.setFixedHeight(30)
        
        # Add widgets to layout
        layout.addWidget(title_label)
        layout.addWidget(content_label)

        return card

    def payment_card_maker(self, title, content, button_name, functionality= lambda:None):
        card = QWidget()
        card.setMinimumSize(300,60)
        card.setMaximumHeight(60)
        card.setProperty("class","card")

        layout = QHBoxLayout(card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        title_label = QLabel(title)
        title_label.setObjectName('card_title3')
        
        content_label = QLabel(content)
        content_label.setObjectName('card_content3')


        title_label.setFixedHeight(30)
        content_label.setFixedHeight(30)

        text = QWidget()
        text.setObjectName('payment_text')

        text_layout = QVBoxLayout(text)

        text_layout.addWidget(title_label)
        text_layout.addWidget(content_label)
        

        button = QPushButton(button_name)
        button.setObjectName('payment_button')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        button.setCursor(QCursor(Qt.PointingHandCursor)) 
        button.clicked.connect(functionality)

        
        layout.addWidget(text,3)
        layout.addWidget(button,1)

        return card
    
    def create_text_with_bar(self, text='', spacing=10):
        
        layout = QHBoxLayout()

        text = QLabel(f'{text}')
        text.setObjectName('add_windows_text1')

        bar = QLineEdit()
        bar.setPlaceholderText("")
        bar.setMaximumHeight(40)
        
        layout.addWidget(bar)
        layout.addWidget(text)

        layout.setSpacing(spacing)

        return layout, bar
    
    def create_text_with_dropdown(self, text='', dropdown_text=[''], spacing=10):
        
        layout = QHBoxLayout()

        text = QLabel(f'{text}')
        text.setObjectName('add_windows_text1')

        combo = QComboBox()

        combo.addItems(dropdown_text)
        combo.setEditable(False)
        combo.setFixedHeight(40)
        
        
        layout.addWidget(combo, stretch=1)
        layout.addWidget(text, stretch=0)

        layout.setSpacing(spacing)

        return layout, combo


    def create_text_with_button(self, text='', button_name='', functionality=None, spacing=10):
        
        layout = QHBoxLayout()

        text = QLabel(f'{text}')
        text.setObjectName('add_windows_text1')

        button = QPushButton(button_name)
        button.setObjectName('new_window_button')
        button.clicked.connect(functionality)
        button.setFixedHeight(40)
        button.setCursor(QCursor(Qt.PointingHandCursor))


        layout.addWidget(button, stretch=1)
        layout.addWidget(text, stretch=0)

        layout.setSpacing(spacing)

        return layout


    def create_text_with_time(self, text='', spacing=10):
        
        layout = QHBoxLayout()

        text = QLabel(f'{text}')
        text.setObjectName('add_windows_text1')

        time_edit = QTimeEdit()
        time_edit.setDisplayFormat("HH:mm")
        time_edit.setTime(QTime(0, 0))   
        time_edit.setFixedHeight(40)
        time_edit.setObjectName('button_with_arrows')

        layout.addWidget(time_edit, stretch=1)
        layout.addWidget(text, stretch=0)

        layout.setSpacing(spacing)

        return layout, time_edit
    

    def create_text_with_numbers(self, text='', range=(0,10000), spacing=10):
        
        layout = QHBoxLayout()

        text = QLabel(f'{text}')
        text.setObjectName('add_windows_text1')

        numbers_edit = QSpinBox()
        numbers_edit.setRange(range[0], range[1])
        numbers_edit.setFixedHeight(40)
        numbers_edit.setObjectName('button_with_arrows')

        layout.addWidget(numbers_edit, stretch=1)
        layout.addWidget(text, stretch=0)

        layout.setSpacing(spacing)

        return layout, numbers_edit



    def all_teachers_window(self, content= returning_teachers_table()):
        
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("قائمة الأساتذة")
        self.dialog.setGeometry(50, 50, 600, 450)

        self.add_teacher_id = None
        def add_teacher_id_changer(teacher_id):
                self.add_teacher_id = teacher_id
                self.dialog.close()
                

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName('red_scroll_area')

        # Create a container widget for the scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for teacher_information in content:
            
            teacher_name = teacher_information[1]
            teacher_profession = teacher_information[3]
            scroll_layout.addWidget(self.payment_card_maker(teacher_name, teacher_profession, 'إختر', lambda _, tid=teacher_information[0] : add_teacher_id_changer(tid)))

        scroll_layout.setAlignment(Qt.AlignTop)

        scroll_area.setWidget(scroll_widget)
        
        layout = QVBoxLayout(self.dialog)
        layout.addWidget(self.search_bar_maker("all_teachers", None, False))
        layout.addWidget(scroll_area)
        

        self.dialog.setModal(True)
        self.dialog.exec()


    def all_students_window(self, content= returning_students_table()):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("قائمة التلاميذ")
        self.dialog.setGeometry(50, 50, 700, 450)

        self.add_student_id = None

        def add_student_id_changer(student_id):
                self.add_student_id = student_id
                self.dialog.close()


        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName('red_scroll_area')

        # Create a container widget for the scroll area

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for student_information in content:
            student_name = student_information[1]
            student_profession = student_information[4]
            scroll_layout.addWidget(self.payment_card_maker(student_name, student_profession, 'إختر', lambda _, sid=student_information[0]: add_student_id_changer(sid)))

        scroll_layout.setAlignment(Qt.AlignTop)
        
        scroll_area.setWidget(scroll_widget)

        layout = QVBoxLayout(self.dialog)
        layout.addWidget(self.search_bar_maker("all_students", None, False))
        layout.addWidget(scroll_area)
        

        self.dialog.setModal(True)
        self.dialog.exec()



    def all_classes_window(self, content= returning_classes_table()):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("قائمة التلاميذ")
        self.dialog.setGeometry(50, 50, 600, 450)

        self.add_classe_id = None

        def add_classe_id_changer(classe_id):
                self.add_classe_id = classe_id
                print(classe_id)
                self.dialog.close()


        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName('red_scroll_area')

        # Create a container widget for the scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for classe_information in content:
            teacher_name = classe_information[1]
            classe_material = classe_information[2]
            classe_time = classe_information[3]

            scroll_layout.addWidget(self.payment_card_maker(teacher_name, f'{classe_material}   {classe_time}', 'إختر', lambda _, cid=classe_information[0]: add_classe_id_changer(cid)))

        scroll_layout.setAlignment(Qt.AlignTop)

        scroll_area.setWidget(scroll_widget)

        layout = QVBoxLayout(self.dialog)
        layout.addWidget(self.search_bar_maker("all_classes", None, False))
        layout.addWidget(scroll_area)
        

        self.dialog.setModal(True)
        self.dialog.exec()


    def add_student_window(self) :
       
        dialog = QDialog(self)
        dialog.setWindowTitle("إضافة تلميذ")
        dialog.setGeometry(50, 50, 600, 350)

        layout = QVBoxLayout(dialog)

        header = QLabel("إضافة تلميذ")
        header.setObjectName("add_student_title")

        layout.addWidget(header)

        #------------------------- Text Bars -----------------------------

        accademic_years= ["تحضيري","أولى ابتدائي", "ثاني ابتدائي", "ثالث ابتدائي",
                           "رابع ابتدائي","خامس ابتدائي","أولى متوسط", "ثاني متوسط",
                            "ثالث متوسط", "رابع متوسط","أولى ثانوي", "ثاني ثانوي", "باكالوريا" ]

        name_layout, name_widget = self.create_text_with_bar('اسم التلميذ:',10)
        age_layout, age_widget = self.create_text_with_numbers('سنة الميلاد:', (1900,2100))
        phone_layout, phone_widget = self.create_text_with_bar('رقم الهاتف:',18)
        accademic_layout, accademic_widget = self.create_text_with_dropdown('السنة الدراسية:', accademic_years,-10)
        location_layout, location_widget = self.create_text_with_bar('الإقامة:',30)
    

        layout.addLayout(name_layout)
        layout.addLayout(age_layout)
        layout.addLayout(phone_layout)
        layout.addLayout(accademic_layout)
        layout.addLayout(location_layout)
        #-----------------------------------------------------------------

        #------------------------Buttons----------------------------------

        buttons = QHBoxLayout()

        save_button = QPushButton("أضف")
        save_button.setObjectName("add_button")
        save_button.setCursor(QCursor(Qt.PointingHandCursor))
        save_button.clicked.connect(lambda: (add_row_in_tables_students(self, [name_widget.text(), age_widget.value(), phone_widget.text(), accademic_widget.currentText(), location_widget.text()]), dialog.close()))

        cancel_button = QPushButton("إلغاء")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.clicked.connect(dialog.close)

        buttons.addWidget(save_button)
        buttons.addWidget(cancel_button)

        buttons.setSpacing(15)

        layout.addLayout(buttons)

        #-------------------------------------------------------------------

        layout.setAlignment(Qt.AlignTop)

        dialog.setModal(True)
        dialog.exec()


    def add_teacher_window(self) :
       
        dialog = QDialog(self)
        dialog.setWindowTitle("إضافة معلم")
        dialog.setGeometry(50, 50, 600, 350)

        layout = QVBoxLayout(dialog)

        header = QLabel("إضافة معلم")
        header.setObjectName("add_student_title")

        layout.addWidget(header)

        #------------------------- Text Bars -----------------------------

        accademic_years= ["رياضيات", "فيزياء", "علوم طبيعية", "لغة عربية",
                          "لغة فرنسية","لغة إنجليزية", "فلسفة", "تاريخ و جغرافيا", "متعدد",
                          "أخرى"]
        
        accademic_levels= ["تحضيري","إبتدائي", "متوسط", "ثانوي","باكالوريا", "متعدد"]

        name_layout, name_widget = self.create_text_with_bar('اسم الأستاذ:',10)
        accademic_layout, accademic_widget = self.create_text_with_dropdown('المادة :', accademic_years,-10)
        accademic_level_layout, accademic_level_widget = self.create_text_with_dropdown('مرحلة التدريس :', accademic_levels,-10)
        phone_layout, phone_widget = self.create_text_with_bar('رقم الهاتف:',18)
        location_layout, location_widget = self.create_text_with_bar('الإقامة:',30)
    

        layout.addLayout(name_layout)
        layout.addLayout(phone_layout)
        layout.addLayout(accademic_layout)
        layout.addLayout(accademic_level_layout)
        layout.addLayout(location_layout)
        #-----------------------------------------------------------------

        #------------------------Buttons----------------------------------

        buttons = QHBoxLayout()

        save_button = QPushButton("أضف")
        save_button.setObjectName("add_button")
        save_button.setCursor(QCursor(Qt.PointingHandCursor))
        save_button.clicked.connect(lambda: (add_row_in_tables_teachers(self, [name_widget.text(), accademic_level_widget.currentText(), accademic_widget.currentText(), phone_widget.text(), location_widget.text()]), dialog.close()))


        cancel_button = QPushButton("إلغاء")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.clicked.connect(dialog.close)

        buttons.addWidget(save_button)
        buttons.addWidget(cancel_button)

        buttons.setSpacing(15)

        layout.addLayout(buttons)

        #-------------------------------------------------------------------

        layout.setAlignment(Qt.AlignTop)

        dialog.setModal(True)
        dialog.exec()


    def add_course_window(self) :
       
        dialog = QDialog(self)
        dialog.setWindowTitle("إضافة حصة")
        dialog.setGeometry(50, 50, 600, 350)

        layout = QVBoxLayout(dialog)

        header = QLabel("إضافة حصة")
        header.setObjectName("add_student_title")

        layout.addWidget(header)

        #------------------------- Text Bars -----------------------------

        accademic_materials= ["رياضيات", "فيزياء", "علوم طبيعية", "لغة عربية",
                          "لغة فرنسية","لغة إنجليزية", "فلسفة", "تاريخ و جغرافيا", "أخرى"]
        
        accademic_years= ["تحضيري","أولى ابتدائي", "ثاني ابتدائي", "ثالث ابتدائي",
                           "رابع ابتدائي","خامس ابتدائي","أولى متوسط", "ثاني متوسط",
                            "ثالث متوسط", "رابع متوسط","أولى ثانوي", "ثاني ثانوي", "باكالوريا" ]
    


        time_layout = QHBoxLayout()
        
        start_time_layout, start_time_widget = self.create_text_with_time('يبدأ :',10)
        end_time_layout, end_time_widget = self.create_text_with_time('ينتهي :',10)

        time_layout.addLayout(end_time_layout)
        time_layout.addLayout(start_time_layout)
        teacher_name_layout = self.create_text_with_button('الأستاذ :', 'إختر الأستاذ', lambda:self.all_teachers_window())
        accademic_subject_layout, accademic_material_widget = self.create_text_with_dropdown('المادة :', accademic_materials,10)
        accademic_level_layout, accademic_level_widget = self.create_text_with_dropdown('السنة الدراسية :', accademic_years,10)
        price_layout, price_widget = self.create_text_with_numbers('السعر :', (0,1000000))
        percentage_layout, percentage_widget = self.create_text_with_numbers('نسبة الأستاذ :', (0,100))
    

        layout.addLayout(teacher_name_layout)
        layout.addLayout(accademic_subject_layout)
        layout.addLayout(time_layout)
        layout.addLayout(accademic_level_layout)
        layout.addLayout(price_layout)
        layout.addLayout(percentage_layout)
        #-----------------------------------------------------------------

        #------------------------Buttons----------------------------------

        buttons = QHBoxLayout()

        save_button = QPushButton("أضف")
        save_button.setObjectName("add_button")
        save_button.setCursor(QCursor(Qt.PointingHandCursor))
        save_button.clicked.connect(lambda: (add_row_in_tables_classes(self, [self.add_teacher_id, accademic_material_widget.currentText(), accademic_level_widget.currentText(),
                                                                            start_time_widget.time().toString("HH:mm"), end_time_widget.time().toString("HH:mm"),
                                                                            price_widget.value(), percentage_widget.value()]), dialog.close()))


        cancel_button = QPushButton("إلغاء")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.clicked.connect(dialog.close)

        buttons.addWidget(save_button)
        buttons.addWidget(cancel_button)

        buttons.setSpacing(15)

        layout.addLayout(buttons)

        #-------------------------------------------------------------------

        layout.setAlignment(Qt.AlignTop)

        dialog.setModal(True)
        dialog.exec()


    def add_payment_window(self) :
       
        dialog = QDialog(self)
        dialog.setWindowTitle("إضافة عملية دفع")
        dialog.setGeometry(50, 50, 600, 350)

        layout = QVBoxLayout(dialog)

        header = QLabel("إضافة عملية دفع")
        header.setObjectName("add_student_title")

        layout.addWidget(header)

        

        #------------------------- Text Bars -----------------------------
        teacher_name_layout = self.create_text_with_button('الحصة :','إختر الحصة', lambda:self.all_classes_window() )
        student_name_layout = self.create_text_with_button('التلميذ :','إختر التلميذ', lambda:self.all_students_window())
        price_layout, price_widget = self.create_text_with_numbers('المبلغ:', (0,1000000))
        date_layout, date_widget = self.create_text_with_bar('التاريخ :',10)
        status_layout, status_widget = self.create_text_with_dropdown('الحالة :', ['مدفوع', 'غير مدفوع'], 10)
    

        layout.addLayout(teacher_name_layout)
        layout.addLayout(student_name_layout)
        layout.addLayout(price_layout)
        layout.addLayout(date_layout)
        layout.addLayout(status_layout)
        #-----------------------------------------------------------------

        #------------------------Buttons----------------------------------

        buttons = QHBoxLayout()

        save_button = QPushButton("أضف")
        save_button.setObjectName("add_button")
        save_button.setCursor(QCursor(Qt.PointingHandCursor))
        save_button.clicked.connect(lambda: (add_row_in_tables_payments(self, [self.add_student_id, self.add_classe_id, price_widget.value(), date_widget.text(), status_widget.currentText()]), dialog.close()))


        cancel_button = QPushButton("إلغاء")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.clicked.connect(dialog.close)

        buttons.addWidget(save_button)
        buttons.addWidget(cancel_button)

        buttons.setSpacing(15)

        layout.addLayout(buttons)

        #-------------------------------------------------------------------

        layout.setAlignment(Qt.AlignTop)

        dialog.setModal(True)
        dialog.exec()


    def add_quick_payment_window(self):
        
        dialog = QDialog(self)
        dialog.setWindowTitle("إضافة عملية دفع")
        dialog.setGeometry(50, 50, 600, 250)

        layout = QVBoxLayout(dialog)

        header = QLabel("إضافة عملية دفع")
        header.setObjectName("add_student_title")

        layout.addWidget(header)

        

        #------------------------- Text Bars -----------------------------
        price_layout, price_widget = self.create_text_with_numbers('المبلغ:', (0,1000000))
        status_layout, status_widget = self.create_text_with_dropdown('الحالة :',['مدفوع','غير مدفوع'],10)


        layout.addLayout(price_layout)
        layout.addLayout(status_layout)
        #-----------------------------------------------------------------

        #------------------------Buttons----------------------------------

        buttons = QHBoxLayout()

        save_button = QPushButton("أضف")
        save_button.setObjectName("add_button")
        save_button.setCursor(QCursor(Qt.PointingHandCursor))
        save_button.clicked.connect(lambda: (add_row_in_tables_quick_payment(self, ['بوسعيد آدم', 'حمزة غراسي', price_widget.value(), '20/11/2005', status_widget.currentText()]), dialog.close()))

        cancel_button = QPushButton("إلغاء")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.clicked.connect(dialog.close)

        buttons.addWidget(save_button)
        buttons.addWidget(cancel_button)

        buttons.setSpacing(15)

        layout.addLayout(buttons)

        #-------------------------------------------------------------------

        layout.setAlignment(Qt.AlignTop)

        dialog.setModal(True)
        dialog.exec()



    def attendance_window(self):
        
        dialog = QDialog(self)
        dialog.setWindowTitle("الحضور")
        dialog.setGeometry(50, 50, 600, 650)

        layout = QVBoxLayout(dialog)

        header = QLabel("الحضور")
        header.setObjectName("add_student_title")

        layout.addWidget(header)

        #-----------students finder and makes them into bars--------------
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName('red_scroll_area')

        # Create a container widget for the scroll area
        
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for teacher_information in returning_students_table():
            teacher_name = teacher_information[1]
            teacher_profession = teacher_information[4]
            scroll_layout.addWidget(self.payment_card_maker(teacher_name, teacher_profession, 'حضر'))

        scroll_layout.setAlignment(Qt.AlignTop)
        
        scroll_area.setWidget(scroll_widget)

        layout.addWidget(self.search_bar_maker(None, None, False))
        layout.addWidget(scroll_area)
        #------------------------- Text Bars -----------------------------
        layout.addLayout(scroll_layout)
        #-----------------------------------------------------------------

        #------------------------Buttons----------------------------------

        buttons = QHBoxLayout()

        save_button = QPushButton("أضف")
        save_button.setObjectName("add_button")
        save_button.setCursor(QCursor(Qt.PointingHandCursor))

        cancel_button = QPushButton("إلغاء")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.clicked.connect(dialog.close)

        buttons.addWidget(save_button)
        buttons.addWidget(cancel_button)

        buttons.setSpacing(15)

        layout.addLayout(buttons)

        #-------------------------------------------------------------------

        layout.setAlignment(Qt.AlignTop)

        dialog.setModal(True)
        dialog.exec()

         
    def search_bar_maker(self, what_to_search=None, add_action=None, add_button = True):

        search_bar = QWidget()
        search_bar.setMinimumSize(300,80)
        search_bar.setMaximumHeight(80)
        search_bar.setProperty("class","card")
        
        layout = QHBoxLayout(search_bar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create title label
        bar = QLineEdit()
        bar.setPlaceholderText("بحث ....")
        bar.setMaximumSize(500,40)

        layout.addWidget(bar)



        search_button = QPushButton('بحث')
        search_button.setObjectName('search_button')
        search_button.setMaximumSize(200,40)
        search_button.setCursor(QCursor(Qt.PointingHandCursor))
        search_button.clicked.connect(lambda : searching(self, bar.text(), what_to_search))


        layout.addWidget(search_button)

        if add_button == True :
            add_button = QPushButton('أضف')
            add_button.setObjectName('search_button')
            add_button.setMaximumSize(200,40)
            add_button.setCursor(QCursor(Qt.PointingHandCursor))
            add_button.clicked.connect(add_action)

            layout.addWidget(add_button)

        return search_bar


    def table_creator(self, labels, sortable, data):
        

        table = QTableWidget(len(data), len(labels))
        table.setHorizontalHeaderLabels(labels)
        
        

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data[1:]):  # skip ID
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                table.setItem(row_idx, col_idx, item)




        table.setSortingEnabled(sortable)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        #table.cellDoubleClicked.connect() keep this to make the editing windows

        
        return table


    def settings_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        page_layout.setAlignment(Qt.AlignTop)


        return container
    

    def accounting_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        page_layout.setAlignment(Qt.AlignTop)


        return container


    def payments_page(self, table_content= returning_payments_table()):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker("payments",lambda: self.add_payment_window())
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['إسم التلميذ', 'إسم الأستاذ', 'الكمية', 'التاريخ', 'الحالة']
        self.payments_page_table = self.table_creator(table_labels, True, table_content)
        page_layout.addWidget(self.payments_page_table)
        page_layout.setSpacing(25)

        page_layout.setAlignment(Qt.AlignTop)


        return container


    def courses_page(self, table_content= returning_classes_table()):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker("classes",lambda: self.add_course_window())
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['الأستاذ', 'المادة', 'السنة الدراسية', 'الفترة', 'السعر' ,'نسبة الأستاذ']
        page_layout.addWidget(self.table_creator(table_labels, True, table_content))
        page_layout.setSpacing(25)

        page_layout.setAlignment(Qt.AlignTop)


        return container



    def teachers_page(self, table_content= returning_teachers_table()):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker("teachers", lambda: self.add_teacher_window())
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['الإسم', 'سنة التدريس', 'المادة', 'رقم الهاتف', 'الاقامة']
        page_layout.addWidget(self.table_creator(table_labels, True, table_content))
        page_layout.setSpacing(25)

        page_layout.setAlignment(Qt.AlignTop)


        return container



    def students_page(self, table_content= returning_students_table()):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker("students",lambda: self.add_student_window())
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['الإسم', 'تاريخ الميلاد', 'رقم الهاتف', 'السنة الدراسية', 'الإقامة']
        page_layout.addWidget(self.table_creator(table_labels, True, table_content))
        page_layout.setSpacing(25)


        page_layout.setAlignment(Qt.AlignTop)


        return container



    def dasboard_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()
        cards_layout.setContentsMargins(10, 10, 10, 10)
        cards_layout.setSpacing(15)

        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        
        card1 = self.card_maker('المعلمين  :', get_number_of_teachers())
        card2 = self.card_maker('التلاميذ  :', get_number_of_students())
        card3 = self.card_maker('الحصص  :', get_number_of_classes())
        
        cards_layout.addWidget(card1)
        cards_layout.addWidget(card2)
        cards_layout.addWidget(card3)
        #--------------------------------------------------

        frames_layout = QHBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName('red_scroll_area')

        scroll_area2 = QScrollArea()
        scroll_area2.setWidgetResizable(True)
        scroll_area2.setObjectName('red_scroll_area')

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        scroll_content2 = QWidget()
        scroll_layout2 = QVBoxLayout(scroll_content2)
        scroll_layout2.setAlignment(Qt.AlignTop)

        # Add multiple labels to fill space
        for i in range(2):
            label = self.payment_card_maker(f'يوسف','رياضيات و فيزياء','دفع', lambda:self.add_quick_payment_window())
            label2 = self.payment_card_maker(f'رياضيات','استاذ بوسعيد','الحضور', lambda:self.attendance_window())
            scroll_layout.addWidget(label)
            scroll_layout2.addWidget(label2)


        scroll_area.setWidget(scroll_content)
        scroll_area2.setWidget(scroll_content2)

        frames_layout.addWidget(scroll_area2)
        frames_layout.addWidget(scroll_area)
        frames_layout.setSpacing(80)

        text= QLabel('يدفعون اليوم    :')
        text2= QLabel('حصص اليوم    :')
        
        text.setObjectName('card_title2')
        text2.setObjectName('card_title2')

        all_text= QHBoxLayout()
        all_text.addWidget(text2)
        all_text.addWidget(text)
        page_layout.addLayout(all_text)
        

        page_layout.addLayout(frames_layout)


        return container

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

    def __init__(self):
        super().__init__()



        dashbord_layout = QHBoxLayout(self)
        self.setMinimumSize(1200,600)

        # ---------------------------Sidebar---------------------------
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")  # For QSS styling
        sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)



        #---------------------------Buttons---------------------------
        sidebar_items = [
            ("الرئيسية", "icons/home-white.png"),
            ("التلاميذ", "icons/user-white.png"),
            ("المعلمين", "icons/graduation-cap-white.png"),
            ("الحصص", "icons/lesson-white.png"),
            ("المدفوعات", "icons/money-white.png"),
            ("المالية", "icons/file-dollar-white.png"),
            ("الإعدادات", "icons/gear-white.png")
        ]
        
        self.nav_buttons = []

        for i, (name,icon) in enumerate(sidebar_items):
            btn = QPushButton(name)
            btn.setIcon(QIcon(icon))
            btn.setObjectName(f"nav_btn_{i}")
            btn.setProperty("class", "nav_btn")
            btn.setProperty("active", i == 0)
            btn.setIconSize(QSize(20, 20))
            btn.setCursor(QCursor(Qt.PointingHandCursor)) 
            if i == 0:
                btn.setCursor(QCursor(Qt.ArrowCursor)) 

            self.nav_buttons.append(btn)
            sidebar_layout.addWidget(btn)
            btn.clicked.connect(lambda checked, index=i: self.set_active_button(index))




        sidebar_layout.addStretch()  # Pushes buttons to the top

        #---------------------------Main Content Area (Placeholder)---------------------------
        
        
        main_content = QVBoxLayout()
        main_content.setObjectName("main_content")

        self.stacked_widget = QStackedWidget()
        
        pages = [self.dasboard_page(), self.students_page(), self.teachers_page(), self.courses_page(), self.payments_page(), self.accounting_page(), self.settings_page()]

        for page in pages :
            self.stacked_widget.addWidget(page)

        main_content.addWidget(self.stacked_widget)
        main_content.setAlignment(Qt.AlignTop)

        dashbord_layout.addWidget(sidebar, 0.5) 
        dashbord_layout.addLayout(main_content, 4.5)  
        #------------------------------------------------------------------------------------
        with open("style.qss", "r") as file:
            app.setStyleSheet(file.read())
        
        
       

if __name__ == "__main__":

    creating_all_tables()
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainPage()
    window.setMinimumWidth(1000)
    window.setWindowTitle("مدرسة")
    window.show()
    sys.exit(app.exec())

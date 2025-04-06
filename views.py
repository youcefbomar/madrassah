from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLabel, QFrame,QSizePolicy,
                              QStackedWidget, QScrollArea, QLineEdit, QTableWidget,
                              QTableWidgetItem, QHeaderView)
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QIcon, QCursor
import sys





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
        card.setMinimumSize(300,100)
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

    def payment_card_maker(self, title, content, button_name):
        card = QWidget()
        card.setMinimumSize(300,80)
        card.setMaximumHeight(80)
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

        
        layout.addWidget(text,3)
        layout.addWidget(button,1)

        return card
         
    def search_bar_maker(self):

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

        layout.addWidget(search_button)


        add_button = QPushButton('أضف')
        add_button.setObjectName('search_button')
        add_button.setMaximumSize(200,40)
        add_button.setCursor(QCursor(Qt.PointingHandCursor))

        layout.addWidget(add_button)

        return search_bar


    def table_creator(self, labels, sortable):
        
        data = [
            ["بوسعيد", 30, "USA",30],
            ["آدم", 25, "Canada",30],
            ["يوسف", 35, "UK",30],
            ["يحيا", 28, "Australia",30],
            ["مات", 22, "Germany",30],
        ]
        


        table = QTableWidget(len(data), len(labels))
        table.setHorizontalHeaderLabels(labels)
        
        

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                
                item = QTableWidgetItem(str(value))
                if col_idx == 1:
                    item.setData(Qt.EditRole, int(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                table.setItem(row_idx, col_idx, item)
                
            item = QTableWidgetItem(f"ID: {row_idx+15}")
            table.setVerticalHeaderItem(row_idx, item)


        table.setSortingEnabled(sortable)


        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        return table


    def payments_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker()
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['إسم التلميذ', 'إسم الأستاذ', 'الكمية', 'التاريخ', 'الحالة']
        page_layout.addWidget(self.table_creator(table_labels, True))
        page_layout.setSpacing(25)

        page_layout.setAlignment(Qt.AlignTop)


        return container


    def courses_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker()
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        page_layout.addWidget(self.table_creator(table_labels, False))
        page_layout.setSpacing(25)

        page_layout.setAlignment(Qt.AlignTop)


        return container



    def teachers_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker()
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['الإسم', 'تاريخ الميلاد', 'المادة', 'رقم الهاتف', 'الاقامة']
        page_layout.addWidget(self.table_creator(table_labels, True))
        page_layout.setSpacing(25)

        page_layout.setAlignment(Qt.AlignTop)


        return container



    def students_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()


        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        search_bar = self.search_bar_maker()
        
        cards_layout.addWidget(search_bar)
        #--------------------------------------------------

        table_labels = ['الإسم', 'تاريخ الميلاد', 'السنة الدراسية', 'الإقامة', 'رقم الهاتف']
        page_layout.addWidget(self.table_creator(table_labels, True))
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
        card1 = self.card_maker('المعلمين  :','190')
        card2 = self.card_maker('التلاميذ  :','3000')
        card3 = self.card_maker('الحصص  :','300')
        
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
            label = self.payment_card_maker(f'يوسف','رياضيات و فيزياء','دفع')
            label2 = self.payment_card_maker(f'رياضيات','استاذ بوسعيد','الحضور')
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



    def __init__(self):
        super().__init__()


        dashbord_layout = QHBoxLayout(self)
        self.setMinimumSize(1200,800)

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
        self.stacked_widget.addWidget(self.dasboard_page())   
        self.stacked_widget.addWidget(self.students_page())
        self.stacked_widget.addWidget(self.teachers_page())  
        self.stacked_widget.addWidget(self.courses_page())
        self.stacked_widget.addWidget(self.payments_page())


        main_content.addWidget(self.stacked_widget)
        main_content.setAlignment(Qt.AlignTop)

        dashbord_layout.addWidget(sidebar, 0.5) 
        dashbord_layout.addLayout(main_content, 4.5)  
        #------------------------------------------------------------------------------------
        with open("style.qss", "r") as file:
            app.setStyleSheet(file.read())
        
        
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  
    window = MainPage()
    window.setMinimumWidth(1400)
    window.setWindowTitle("مدرسة")
    window.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLabel, QFrame, QSpacerItem,
                              QSizePolicy, QStackedWidget, QScrollArea)
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
            if i == index:
                btn.setCursor(QCursor(Qt.ArrowCursor))  
            else :
                btn.setCursor(QCursor(Qt.PointingHandCursor))

    def card_maker(self,title,content) :
        card = QWidget()
        card.setMinimumSize(300,120)
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

    def payment_card_maker(self,title,content):
        card = QWidget()
        card.setMinimumSize(300,120)
        card.setProperty("class","card")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)

        # Create title label
        title_label = QLabel(title)
        title_label.setObjectName('card_title3')
        title_label.setAlignment(Qt.AlignLeft)
        
        # Create content label
        content_label = QLabel(content)
        content_label.setObjectName('card_content3')
        content_label.setAlignment(Qt.AlignLeft)
        title_label.setFixedHeight(30)
        content_label.setFixedHeight(30)
        
        # Add widgets to layout
        layout.addWidget(title_label)
        layout.addWidget(content_label)

        return card
         

    def dasboard_page(self):

        container = QWidget()
        page_layout= QVBoxLayout(container) 

        cards_layout = QHBoxLayout()
        cards_layout.setContentsMargins(10, 10, 10, 30)
        cards_layout.setSpacing(15)

        page_layout.addLayout(cards_layout)

        #--------- cards ----------------------------------
        card1 = self.card_maker('Teachers  :','190')
        card2 = self.card_maker('Students  :','3000')
        card3 = self.card_maker('Classes  :','300')
        
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

        scroll_content2 = QWidget()
        scroll_layout2 = QVBoxLayout(scroll_content2)

        # Add multiple labels to fill space
        for i in range(50):
            label = self.payment_card_maker(f'يوسف{i}',str(i*i+i*268*i+i*657*6*i))
            label2 = self.card_maker(f'asda{i}','someshit')
            scroll_layout.addWidget(label)
            print(f'nerd{i}')
            scroll_layout2.addWidget(label2)


        scroll_area.setWidget(scroll_content)
        scroll_area2.setWidget(scroll_content2)

        frames_layout.addWidget(scroll_area)
        frames_layout.addWidget(scroll_area2)
        frames_layout.setSpacing(30)

        text=QLabel('يدفعون اليوم    :')
        text.setObjectName('card_title2')
        page_layout.addWidget(text)
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
            ("Dashboard", "icons/home-white.png"),
            ("Students", "icons/user-white.png"),
            ("Teachers", "icons/graduation-cap-white.png"),
            ("Classes", "icons/coins-white.png"),
            ("Payments", "icons/coins-white.png"),
            ("Incomes", "icons/coins-white.png"),
            ("Settings", "icons/gear-white.png")
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
        frame = QFrame()
        frame_layout = QVBoxLayout(frame)
        
        something = QHBoxLayout()
        something.addWidget(self.dasboard_page())

        frame_layout.addLayout(something)
        main_content.addWidget(frame)
        main_content.setAlignment(Qt.AlignTop)
        




        dashbord_layout.addWidget(sidebar, 0.5) 
        dashbord_layout.addLayout(main_content, 4.5)  



        with open("style.qss", "r") as file:
            app.setStyleSheet(file.read())
        
        
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  
    window = MainPage()
    window.setMinimumWidth(1400)
    window.setWindowTitle("Madrassah")
    window.show()
    sys.exit(app.exec())

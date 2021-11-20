import sys

import PyQt5.QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from prosto_reader import *
from render_pdf import *



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Counters
        self.number_page = 0
        self.current_page = 0

        # Another
        self.path_open_file = None               # Путь к открытию файла

        # Flags
        self.mouse_right_button_flag = False

        ###########################################################################
        # Скрыть стандарное окно
        ###########################################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        ###########################################################################
        # Обработка нажатия
        ###########################################################################
        self.btnMinimaze.clicked.connect(lambda: self.showMinimized())

        self.btnClose.clicked.connect(lambda: self.close())

        self.btnRestore.clicked.connect(lambda: self.restore_max_or_min_window())

        ###########################################################################
        # Настройка
        ###########################################################################
        self.btnBook.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRead))

        self.btnDounload.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageDownload))

        self.btnTelegram.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageTelegram))

        ###########################################################################
        # Настройка изменения окна, установка метки в правый нижний угол
        ###########################################################################
        size_grip = QtWidgets.QSizeGrip(self)
        self.verticalLayout_2.addWidget(size_grip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        ###########################################################################
        # Загрузить файл из Folder
        ###########################################################################
        self.btnFolder.clicked.connect(self.evt_open_folder_and_load_file)

        ###########################################################################
        # Сигнал завершения редактирования QLineEdit
        ###########################################################################
        self.liedPage.returnPressed.connect(self.evt_set_current_page)

    ###########################################################################
    # Методы обработки кнопок и колесика мыши
    ###########################################################################
        self.old_pos = None

    def mousePressEvent(self, event):
        if self.freMainHeader.underMouse():                # Проверяем находится ли курсор на freMainHeader
            if event.button() == Qt.LeftButton:
                self.old_pos = event.pos()
        elif self.lblRenderPage.underMouse():
            if event.button() == Qt.RightButton:
                self.mouse_right_button_flag = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None
        elif event.button() == Qt.RightButton:
            self.mouse_right_button_flag = False

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def wheelEvent(self, event):
        evt_mouse = event.angleDelta().y() / 8
        if self.mouse_right_button_flag and self.path_open_file:
            if evt_mouse >= 0 and self.current_page < self.number_page-1:
                self.current_page += 1
                self.show_book()
                print(self.current_page)
            elif evt_mouse < 0 and self.current_page >= 1:
                self.current_page -= 1
                self.show_book()
                print(self.current_page)

    ###########################################################################
    # Метод обработки кнопки сворачивания и разворачивания окна
    ###########################################################################
    def restore_max_or_min_window(self):
        if self.isMaximized():
            self.showNormal()
            self.btnRestore.setIcon(QtGui.QIcon("Icons/maximize.png"))
        else:
            self.showMaximized()
            self.btnRestore.setIcon(QtGui.QIcon("Icons/icons8-восстановить-окно-64.png"))

    ###########################################################################
    # Метод обработки доступа к файлу по нажатии кнопки Folder
    ###########################################################################
    def evt_open_folder_and_load_file(self):
        self.path_open_file, _ = QFileDialog.getOpenFileName(self, 'Open File', '/home/oleg/Рабочий стол',
                                                             'PDF file (*.pdf)')
        self.current_page = 0
        self.show_book()

    def evt_set_current_page(self):
        if self.path_open_file:
            self.current_page = int(self.liedPage.text())
            self.show_book()

    def show_book(self):
        if '.pdf' in self.path_open_file:
            read = ReadPDF(self.current_page, self.path_open_file)

            self.number_page = read.get_number_of_pages()
            self.lblPages.setText(str(self.number_page - 1))

            self.liedPage.setReadOnly(False)
            self.liedPage.setText(str(self.current_page))
            self.liedPage.setValidator(QIntValidator(0, self.number_page - 1))

            image = read.get_image()
            self.lblRenderPage.setPixmap(QPixmap.fromImage(image))



    def keyPressEvent(self, event):
        key_press = event.key()
        if self.lblRenderPage.underMouse() and self.path_open_file:
            if key_press == Qt.Key.Key_X and self.current_page < self.number_page-1:
                self.current_page += 1
                self.show_book()
                print(self.current_page)
            elif key_press == Qt.Key.Key_Z and self.current_page >= 1:
                self.current_page -= 1
                self.show_book()
                print(self.current_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)         # создание приложения
    mainWindow = MainWindow()            # создание окна GUI
    mainWindow.show()                    # показать GUI
    sys.exit(app.exec_())                # запускает прилоения и обработчики событий


"""pyuic5 ProstoReader.ui -o prosto_reader.py"""

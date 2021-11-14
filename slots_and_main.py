import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from prosto_reader import *
from poppler import *




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.qImg = QImage()
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
        self.horizontalLayout_5.addWidget(size_grip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        self.btnFolder.clicked.connect(self.evt_open_folder)






    ###########################################################################
    # Методы обработки нажантия на левую кнопку мыши при наведении ее на
    # freMainHeader для перемещения по экрану
    ###########################################################################
        self.old_pos = None

    def mousePressEvent(self, event):
        if self.freMainHeader.underMouse():                # Проверяем находится ли курсор на freMainHeader
            if event.button() == Qt.LeftButton:
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)



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



    def evt_open_folder(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', '/home/oleg/Рабочий стол', 'PDF file (*.pdf)')
        a, b = res
        print(a)


        pdf_document = load_from_file(a)
        page_1 = pdf_document.create_page(0)

        page_1_text = page_1.text()
        print(page_1_text)


        renderer = PageRenderer()
        image = renderer.render_page(page_1)
        #image_data = image.data
        image_data1 = image.supported_image_formats()
        print(image_data1)
        print(image.format)




        renderImg = QImage(image.data, image.width, image.height, image.bytes_per_row, QImage.Format_ARGB32)
        self.lblPage.setPixmap(QPixmap.fromImage(renderImg))


if __name__ == '__main__':
    app = QApplication(sys.argv)         # создание приложения
    mainWindow = MainWindow()            # создание окна GUI
    mainWindow.show()                    # показать GUI
    sys.exit(app.exec_())                # запускает прилоения и обработчики событий


"""pyuic5 ProstoReader.ui -o prosto_reader.py"""


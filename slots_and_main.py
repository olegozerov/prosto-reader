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
        self.path_open_file = None               # Путь к открытию файла
        self.mouse_right_button_flag = False
        self.page_counter = 0
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
    def evt_open_folder(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '/home/oleg/Рабочий стол', 'PDF file (*.pdf)')
        self.path_open_file, _ = file_path
        self.load_pdf_from_file(self.path_open_file)

    def load_pdf_from_file(self, path):
        pdf_document = load_from_file(path)
        page_render = pdf_document.create_page(self.page_counter)
        pages_in_book = pdf_document.pages
        self.lblPages.setText(str(pages_in_book))
        self.liedPage.setText(str(self.page_counter))
        self.renderer_pdf(page_render)



    def renderer_pdf(self, page_):
        renderer = PageRenderer()
        image = renderer.render_page(page_)
        render_img = QImage(image.data, image.width, image.height, image.bytes_per_row, QImage.Format_ARGB32)
        self.lblRenderPage.setPixmap(QPixmap.fromImage(render_img))

    def wheelEvent(self, event):
        self.load_pdf_from_file(self.path_open_file)
        evt_mouse = event.angleDelta().y() / 8
        if self.mouse_right_button_flag:
            if evt_mouse >= 0:
                self.page_counter += 1
            elif evt_mouse < 0 and self.page_counter >= 1:
                self.page_counter -= 1





if __name__ == '__main__':
    app = QApplication(sys.argv)         # создание приложения
    mainWindow = MainWindow()            # создание окна GUI
    mainWindow.show()                    # показать GUI
    sys.exit(app.exec_())                # запускает прилоения и обработчики событий


"""pyuic5 ProstoReader.ui -o prosto_reader.py"""


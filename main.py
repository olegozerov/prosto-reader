import sys
from ui_interface import *
from PyQt5.QtGui import QTransform, QPixmap, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt
from pdf import ReadPDF


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Counters
        self.number_page = 0
        self.current_page = 0
        self.zoom_count = 7

        # Another
        self.path_open_file = None  # Путь к открытию файла
        self.render_image = None
        self.angle = 0

        # Flags
        self.mouse_right_button_flag = False
        self.zoom_flag = False

        ######################################################################
        # Скрыть стандарное окно
        ######################################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        ######################################################################
        # Обработка сигналов кнопок работы с окном приложения
        ######################################################################
        self.btnMinimaze.clicked.connect(lambda: self.showMinimized())

        self.btnClose.clicked.connect(lambda: self.close())

        self.btnRestore.clicked.connect(lambda:
                                        self.evt_restore_max_or_min_window())

        ######################################################################
        # Обработка сигналов кнопок на левой панели
        ######################################################################
        self.btnBook.clicked.connect(self.evt_btn_page_for_read)

        self.btnInformation.clicked.connect(self.evt_btn_information)

        self.btnFolder.clicked.connect(self.evt_open_folder_and_load_file)

        ######################################################################
        # Настройка изменения окна, установка метки в правый нижний угол
        ######################################################################
        size_grip = QtWidgets.QSizeGrip(self)
        self.verticalLayout_2.addWidget(size_grip, 0,
                                        Qt.AlignBottom | Qt.AlignRight)

        ######################################################################
        # Сигнал завершения редактирования QLineEdit, переход на нужную
        # страницу на верхней панели
        ######################################################################
        self.liedPage.returnPressed.connect(self.evt_set_current_page)

        ######################################################################
        # Слоты обработки кнопок и колесика мыши
        ######################################################################
        self.old_pos = None

    def mousePressEvent(self, event):
        if self.freMainHeader.underMouse():
            if event.button() == Qt.LeftButton:
                self.old_pos = event.pos()
        elif self.lblRenderPage.underMouse():
            if event.button() == Qt.RightButton:
                self.mouse_right_button_flag = True
                self.sllArea.verticalScrollBar().setDisabled(True)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None
        elif event.button() == Qt.RightButton:
            self.mouse_right_button_flag = False
            self.sllArea.verticalScrollBar().setEnabled(True)

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def wheelEvent(self, event):
        self.angle = 0
        evt_mouse = event.angleDelta().y() / 8
        if self.mouse_right_button_flag and self.path_open_file:
            if evt_mouse >= 0 and self.current_page < self.number_page - 1:
                self.current_page += 1
                self.show_book()
            elif evt_mouse < 0 and self.current_page >= 1:
                self.current_page -= 1
                self.show_book()

        if self.zoom_flag and self.path_open_file:
            if 0 <= evt_mouse:
                self.zoom_count += 1
                self.show_book()
            elif evt_mouse < 0:
                self.zoom_count -= 1
                self.show_book()

    ##########################################################################
    # Слоты обработки нажатия клаившь на клавиатуре
    ##########################################################################
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key_press = event.key()
        if self.lblRenderPage.underMouse() and self.path_open_file:
            if key_press == Qt.Key.Key_X and \
                    self.current_page < self.number_page - 1:
                self.angle = 0
                self.current_page += 1
                self.show_book()
            elif key_press == Qt.Key.Key_Z and self.current_page >= 1:
                self.angle = 0
                self.current_page -= 1
                self.show_book()

            if key_press == Qt.Key.Key_Control:
                self.zoom_flag = True

            if key_press == Qt.Key.Key_R:
                self.evt_turn_image()

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        key_release = event.key()
        if key_release == Qt.Key.Key_Control:
            self.zoom_flag = False

    ##########################################################################
    # Слот обработки кнопки сворачивания и разворачивания окна
    ##########################################################################
    @QtCore.pyqtSlot()
    def evt_restore_max_or_min_window(self):
        if self.isMaximized():
            self.showNormal()
            self.btnRestore.setIcon(QtGui.QIcon("Icons/maximize.png"))
        else:
            self.showMaximized()
            self.btnRestore.setIcon(QtGui.QIcon
                                    ("Icons/icons8-восстановить-окно-64.png"))

    ##########################################################################
    # Слот обработки доступа к файлу по нажатии кнопки Folder
    ##########################################################################
    @QtCore.pyqtSlot()
    def evt_open_folder_and_load_file(self):
        self.path_open_file, _ = QFileDialog.getOpenFileName(
            self, 'Open File', '/home/oleg/Рабочий стол', 'PDF file (*.pdf)')
        self.current_page = 0
        self.zoom_count = 7
        self.show_book()

    ##########################################################################
    # Слот обработки доступа к файлу по нажатии кнопки Folder
    ##########################################################################
    @QtCore.pyqtSlot()
    def evt_set_current_page(self):
        if self.path_open_file:
            self.current_page = int(self.liedPage.text())
            self.show_book()

    ##########################################################################
    # Слот обработки кнопки информации о проекте
    ##########################################################################
    @QtCore.pyqtSlot()
    def evt_btn_information(self):
        self.stackedWidget.setCurrentWidget(self.pageInformation)
        if self.pageInformation.isActiveWindow():
            self.btnFolder.setDisabled(True)

    @QtCore.pyqtSlot()
    ##########################################################################
    # Слот обработки кнопки страницы чтения
    ##########################################################################
    def evt_btn_page_for_read(self):
        self.stackedWidget.setCurrentWidget(self.pageRead)
        if self.pageRead.isActiveWindow():
            self.btnFolder.setEnabled(True)

    ##########################################################################
    # Слот обработки разворта страницы
    ##########################################################################
    def evt_turn_image(self):
        self.angle += 90
        if self.angle == 360:
            self.angle = 0
        transform = QTransform()
        transform.rotate(self.angle)
        self.lblRenderPage.setPixmap(QPixmap.fromImage(self.render_image)
                                     .transformed(transform))

    ##########################################################################
    # Метод выбора необходимого файла, можно еще добавить
    ##########################################################################
    def show_book(self):
        if '.pdf' in self.path_open_file:
            self.render_pdf()

    ##########################################################################
    # Метод рендеринга pdf страниц
    ##########################################################################
    def render_pdf(self):
        read = ReadPDF(self.current_page, self.path_open_file)

        self.number_page = read.get_number_of_pages()
        self.lblPages.setText(str(self.number_page - 1))

        self.liedPage.setReadOnly(False)
        self.liedPage.setText(str(self.current_page))
        self.liedPage.setValidator(QIntValidator(0, self.number_page - 1))

        self.render_image = read.get_image()
        image_height = self.render_image.height()
        image_width = self.render_image.width()
        self.render_image = self.render_image.smoothScaled(
            round(image_width * self.zoom_count / 20),
            round(image_height * self.zoom_count / 20))
        self.lblRenderPage.setPixmap(QPixmap.fromImage(self.render_image))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание приложения
    mainWindow = MainWindow()  # создание окна GUI
    mainWindow.show()  # показать GUI
    sys.exit(app.exec_())  # запускает прилоения и обработчики событий

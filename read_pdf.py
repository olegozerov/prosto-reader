#######################################################################################################################
#
#
# Чтение pdf файлов
#
#
########################################################################################################################
from poppler import PageRenderer, load_from_file
from PyQt5 import QtGui


def format_p2q(key):
    p2q_format = \
        {
            key.invalid: QtGui.QImage.Format_Invalid,
            key.argb32: QtGui.QImage.Format_ARGB32,
            key.bgr24: QtGui.QImage.Format_BGR888,
            key.gray8: QtGui.QImage.Format_Grayscale8,
            key.mono: QtGui.QImage.Format_Mono,
            key.rgb24: QtGui.QImage.Format_RGB888,
        }
    return p2q_format[key]


class ReadPDF:
    def __init__(self, path: str):
        self.path_open_file = None               # Путь к открытию файла
        self.path = path
        self.load_file(self.path)

    @staticmethod
    def load_file(path_file):
        pdf_document = load_from_file(path_file)
        pages = pdf_document.pages
        index_page = pdf_document.page

        return pages, index_page

    @staticmethod
    def render_pdf_to_img(page, ima):
        renderer = PageRenderer()
        image = renderer.render_page(page_1)
        rendered_img = QtGui.QImage(page.data, page.width, page.height, page.bytes_per_row, QtGui.QImage.Format_ARGB32)
        return rendered_img

    @staticmethod
    def create_page(page):
        img_page = pdf_document.create_page(page)
"""
    def open_render_pdf(self):
        pdf_document = load_from_file(self.path_open_file)
        pages = pdf_document.pages
        print(pages)
        index_page = pdf_document.page
        print(index_page)

        page_1_text = page_1.text()
        print(page_1_text)

        renderer = PageRenderer()
        image = renderer.render_page(page_1)
        # image_data = image.data
        image_data1 = image.supported_image_formats()
        print(image_data1)
        print(image.format)

        renderImg = QImage(image.data, image.width, image.height, image.bytes_per_row, QImage.Format_ARGB32)
        self.lblPage.setPixmap(QPixmap.fromImage(renderImg))
"""
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
    def __init__(self, file: str):
        self.rendered_img = None
        self.file = file
        self.open_file()

    def open_file(self):
        pdf_document = load_from_file(self.file)
        pages = pdf_document.pages

        for page in range(int(pages) + 1):
            renderer = PageRenderer()
            pdf_image = renderer.render_page(page)
            return pdf_image

    def render_pdf_to_img(self, page):
        self.rendered_img = QtGui.QImage(page.data, page.width, page.height, page.bytes_per_row, QImage.Format_ARGB32)
        return self.rendered_img


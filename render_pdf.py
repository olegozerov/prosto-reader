########################################################################################################################
# Чтение pdf файлов
########################################################################################################################
from poppler import PageRenderer, load_from_file
from PyQt5 import QtGui


class ReadPDF:
    def __init__(self, current, path):
        self._path = path
        self._current = current
        self._pdf_document = None
        self._create_page = None
        self._load_file(self._current, self._path)

    def _load_file(self, current_page, path=None):
        self._pdf_document = load_from_file(path)
        self._create_page = self._pdf_document.create_page(current_page)

    def get_image(self):
        renderer = PageRenderer()
        render_image = renderer.render_page(self._create_page)
        image = QtGui.QImage(render_image.data, render_image.width, render_image.height,
                             render_image.bytes_per_row, QtGui.QImage.Format_ARGB32)
        return image

    def get_number_of_pages(self):
        number_of_pages = self._pdf_document.pages
        return number_of_pages

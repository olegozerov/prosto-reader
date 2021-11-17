########################################################################################################################
# Чтение pdf файлов
########################################################################################################################
from poppler import PageRenderer, load_from_file
from PyQt5 import QtGui


class ReadPDF:
    def __init__(self, path: str):
        self._path = path
        self._pdf_document = None
        self._create_page = None
        self._rendered_img = None
        self._current_page = 0
        self._load_file(self._path)

    def _load_file(self, path=None):
        self._pdf_document = load_from_file(path)

    def get_number_of_pages(self):
        number_of_pages = self._pdf_document.pages
        return number_of_pages

    def get_create_page(self):
        self._create_page = self._pdf_document.create_page(self._current_page)
        return self._create_page

    def get_image(self):
        renderer = PageRenderer()
        image = renderer.render_page(self._create_page)
        self._rendered_img = QtGui.QImage(image.data, image.width, image.height,
                                          image.bytes_per_row, QtGui.QImage.Format_ARGB32)
        return self._rendered_img

    def set_current_page(self, page):
        self._current_page = page
        return self._current_page

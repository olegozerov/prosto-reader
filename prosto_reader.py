# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProstoReader.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 880)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 870))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(224, 224, 209);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setStyleSheet("background-color: rgb(224, 224, 209);")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.freMainHeader = QtWidgets.QFrame(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freMainHeader.sizePolicy().hasHeightForWidth())
        self.freMainHeader.setSizePolicy(sizePolicy)
        self.freMainHeader.setMouseTracking(True)
        self.freMainHeader.setFocusPolicy(QtCore.Qt.NoFocus)
        self.freMainHeader.setStyleSheet("background-color: rgb(118, 194, 175);")
        self.freMainHeader.setObjectName("freMainHeader")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.freMainHeader)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.freLHeader = QtWidgets.QFrame(self.freMainHeader)
        self.freLHeader.setStyleSheet("")
        self.freLHeader.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freLHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freLHeader.setObjectName("freLHeader")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.freLHeader)
        self.horizontalLayout_2.setContentsMargins(9, 9, 0, 9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblTitle = QtWidgets.QLabel(self.freLHeader)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.horizontalLayout_2.addWidget(self.lblTitle)
        self.horizontalLayout.addWidget(self.freLHeader, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.freRHeader = QtWidgets.QFrame(self.freMainHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freRHeader.sizePolicy().hasHeightForWidth())
        self.freRHeader.setSizePolicy(sizePolicy)
        self.freRHeader.setMinimumSize(QtCore.QSize(200, 0))
        self.freRHeader.setStyleSheet("")
        self.freRHeader.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freRHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freRHeader.setObjectName("freRHeader")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.freRHeader)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.liedPage = QtWidgets.QLineEdit(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liedPage.sizePolicy().hasHeightForWidth())
        self.liedPage.setSizePolicy(sizePolicy)
        self.liedPage.setMinimumSize(QtCore.QSize(20, 19))
        self.liedPage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.liedPage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.liedPage.setStyleSheet("border: none")
        self.liedPage.setMaxLength(4)
        self.liedPage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.liedPage.setReadOnly(True)
        self.liedPage.setObjectName("liedPage")
        self.horizontalLayout_3.addWidget(self.liedPage)
        self.lblSlash = QtWidgets.QLabel(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSlash.sizePolicy().hasHeightForWidth())
        self.lblSlash.setSizePolicy(sizePolicy)
        self.lblSlash.setMinimumSize(QtCore.QSize(15, 0))
        self.lblSlash.setMaximumSize(QtCore.QSize(0, 16777215))
        self.lblSlash.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblSlash.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblSlash.setLineWidth(0)
        self.lblSlash.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSlash.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblSlash.setObjectName("lblSlash")
        self.horizontalLayout_3.addWidget(self.lblSlash)
        self.lblPages = QtWidgets.QLabel(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPages.sizePolicy().hasHeightForWidth())
        self.lblPages.setSizePolicy(sizePolicy)
        self.lblPages.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lblPages.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPages.setObjectName("lblPages")
        self.horizontalLayout_3.addWidget(self.lblPages)
        self.spbSizePage = QtWidgets.QSpinBox(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spbSizePage.sizePolicy().hasHeightForWidth())
        self.spbSizePage.setSizePolicy(sizePolicy)
        self.spbSizePage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spbSizePage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spbSizePage.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spbSizePage.setWrapping(False)
        self.spbSizePage.setFrame(True)
        self.spbSizePage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spbSizePage.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spbSizePage.setSingleStep(1)
        self.spbSizePage.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spbSizePage.setProperty("value", 0)
        self.spbSizePage.setDisplayIntegerBase(11)
        self.spbSizePage.setObjectName("spbSizePage")
        self.horizontalLayout_3.addWidget(self.spbSizePage)
        self.btnMinimaze = QtWidgets.QPushButton(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMinimaze.sizePolicy().hasHeightForWidth())
        self.btnMinimaze.setSizePolicy(sizePolicy)
        self.btnMinimaze.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icons8-свернуть-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimaze.setIcon(icon)
        self.btnMinimaze.setIconSize(QtCore.QSize(24, 24))
        self.btnMinimaze.setFlat(True)
        self.btnMinimaze.setObjectName("btnMinimaze")
        self.horizontalLayout_3.addWidget(self.btnMinimaze)
        self.btnRestore = QtWidgets.QPushButton(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRestore.sizePolicy().hasHeightForWidth())
        self.btnRestore.setSizePolicy(sizePolicy)
        self.btnRestore.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRestore.setIcon(icon1)
        self.btnRestore.setIconSize(QtCore.QSize(24, 24))
        self.btnRestore.setFlat(True)
        self.btnRestore.setObjectName("btnRestore")
        self.horizontalLayout_3.addWidget(self.btnRestore)
        self.btnClose = QtWidgets.QPushButton(self.freRHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMouseTracking(False)
        self.btnClose.setStyleSheet("")
        self.btnClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/icons8-закрыть-окно-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setIconSize(QtCore.QSize(24, 24))
        self.btnClose.setFlat(True)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose)
        self.horizontalLayout.addWidget(self.freRHeader, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.freMainHeader)
        self.freMainWorkspace = QtWidgets.QFrame(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freMainWorkspace.sizePolicy().hasHeightForWidth())
        self.freMainWorkspace.setSizePolicy(sizePolicy)
        self.freMainWorkspace.setStyleSheet("")
        self.freMainWorkspace.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freMainWorkspace.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freMainWorkspace.setObjectName("freMainWorkspace")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.freMainWorkspace)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.freMainTaskbar = QtWidgets.QFrame(self.freMainWorkspace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freMainTaskbar.sizePolicy().hasHeightForWidth())
        self.freMainTaskbar.setSizePolicy(sizePolicy)
        self.freMainTaskbar.setStyleSheet("background-color: rgb(224, 153, 94);")
        self.freMainTaskbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freMainTaskbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freMainTaskbar.setObjectName("freMainTaskbar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.freMainTaskbar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.freTopTaskBar = QtWidgets.QFrame(self.freMainTaskbar)
        self.freTopTaskBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freTopTaskBar.sizePolicy().hasHeightForWidth())
        self.freTopTaskBar.setSizePolicy(sizePolicy)
        self.freTopTaskBar.setStyleSheet("")
        self.freTopTaskBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freTopTaskBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freTopTaskBar.setObjectName("freTopTaskBar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.freTopTaskBar)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnFolder = QtWidgets.QPushButton(self.freTopTaskBar)
        self.btnFolder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFolder.setIcon(icon3)
        self.btnFolder.setIconSize(QtCore.QSize(32, 32))
        self.btnFolder.setFlat(True)
        self.btnFolder.setObjectName("btnFolder")
        self.verticalLayout_4.addWidget(self.btnFolder)
        self.btnBook = QtWidgets.QPushButton(self.freTopTaskBar)
        self.btnBook.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/booklet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBook.setIcon(icon4)
        self.btnBook.setIconSize(QtCore.QSize(32, 32))
        self.btnBook.setFlat(True)
        self.btnBook.setObjectName("btnBook")
        self.verticalLayout_4.addWidget(self.btnBook)
        self.btnDounload = QtWidgets.QPushButton(self.freTopTaskBar)
        self.btnDounload.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/download.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnDounload.setIcon(icon5)
        self.btnDounload.setIconSize(QtCore.QSize(32, 32))
        self.btnDounload.setFlat(True)
        self.btnDounload.setObjectName("btnDounload")
        self.verticalLayout_4.addWidget(self.btnDounload, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.btnTelegram = QtWidgets.QPushButton(self.freTopTaskBar)
        self.btnTelegram.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/telegram-64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTelegram.setIcon(icon6)
        self.btnTelegram.setIconSize(QtCore.QSize(32, 32))
        self.btnTelegram.setFlat(True)
        self.btnTelegram.setObjectName("btnTelegram")
        self.verticalLayout_4.addWidget(self.btnTelegram)
        self.btnContrast = QtWidgets.QPushButton(self.freTopTaskBar)
        self.btnContrast.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/contrast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnContrast.setIcon(icon7)
        self.btnContrast.setIconSize(QtCore.QSize(32, 32))
        self.btnContrast.setCheckable(False)
        self.btnContrast.setFlat(True)
        self.btnContrast.setObjectName("btnContrast")
        self.verticalLayout_4.addWidget(self.btnContrast, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.btnSearch = QtWidgets.QPushButton(self.freTopTaskBar)
        self.btnSearch.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/magnifyingglass.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnSearch.setIcon(icon8)
        self.btnSearch.setIconSize(QtCore.QSize(32, 32))
        self.btnSearch.setFlat(True)
        self.btnSearch.setObjectName("btnSearch")
        self.verticalLayout_4.addWidget(self.btnSearch, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.freTopTaskBar, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.freBottomTaskBar = QtWidgets.QFrame(self.freMainTaskbar)
        self.freBottomTaskBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freBottomTaskBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freBottomTaskBar.setObjectName("freBottomTaskBar")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.freBottomTaskBar)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnProfile = QtWidgets.QPushButton(self.freBottomTaskBar)
        self.btnProfile.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/profle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProfile.setIcon(icon9)
        self.btnProfile.setIconSize(QtCore.QSize(32, 32))
        self.btnProfile.setFlat(True)
        self.btnProfile.setObjectName("btnProfile")
        self.verticalLayout_5.addWidget(self.btnProfile, 0, QtCore.Qt.AlignBottom)
        self.btnInformation = QtWidgets.QPushButton(self.freBottomTaskBar)
        self.btnInformation.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInformation.setIcon(icon10)
        self.btnInformation.setIconSize(QtCore.QSize(32, 32))
        self.btnInformation.setFlat(True)
        self.btnInformation.setObjectName("btnInformation")
        self.verticalLayout_5.addWidget(self.btnInformation, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_3.addWidget(self.freBottomTaskBar, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.freMainTaskbar, 0, QtCore.Qt.AlignLeft)
        self.freWorkspace = QtWidgets.QFrame(self.freMainWorkspace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freWorkspace.sizePolicy().hasHeightForWidth())
        self.freWorkspace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.freWorkspace.setFont(font)
        self.freWorkspace.setStyleSheet("border-bottom-color: rgb(118, 194, 175);")
        self.freWorkspace.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.freWorkspace.setFrameShadow(QtWidgets.QFrame.Raised)
        self.freWorkspace.setObjectName("freWorkspace")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.freWorkspace)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.freWorkspace)
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageTelegram = QtWidgets.QWidget()
        self.pageTelegram.setStyleSheet("")
        self.pageTelegram.setObjectName("pageTelegram")
        self.stackedWidget.addWidget(self.pageTelegram)
        self.pageDownload = QtWidgets.QWidget()
        self.pageDownload.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pageDownload.setMouseTracking(False)
        self.pageDownload.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pageDownload.setObjectName("pageDownload")
        self.stackedWidget.addWidget(self.pageDownload)
        self.pageRead = QtWidgets.QWidget()
        self.pageRead.setStyleSheet("background-color: rgb(224, 224, 209);")
        self.pageRead.setObjectName("pageRead")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pageRead)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sllArea = QtWidgets.QScrollArea(self.pageRead)
        self.sllArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sllArea.setWidgetResizable(True)
        self.sllArea.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.sllArea.setObjectName("sllArea")
        self.sllAreaPage = QtWidgets.QWidget()
        self.sllAreaPage.setGeometry(QtCore.QRect(0, 0, 709, 845))
        self.sllAreaPage.setObjectName("sllAreaPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.sllAreaPage)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblRenderPage = QtWidgets.QLabel(self.sllAreaPage)
        self.lblRenderPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblRenderPage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRenderPage.setObjectName("lblRenderPage")
        self.verticalLayout_7.addWidget(self.lblRenderPage)
        self.sllArea.setWidget(self.sllAreaPage)
        self.verticalLayout_6.addWidget(self.sllArea)
        self.stackedWidget.addWidget(self.pageRead)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.freWorkspace)
        self.verticalLayout.addWidget(self.freMainWorkspace)
        self.freMainWorkspace.raise_()
        self.freMainHeader.raise_()
        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ProstoReader"))
        self.lblTitle.setText(_translate("MainWindow", "ProstoReader"))
        self.liedPage.setText(_translate("MainWindow", "0"))
        self.lblSlash.setText(_translate("MainWindow", "/"))
        self.lblPages.setText(_translate("MainWindow", "0"))
        self.spbSizePage.setSuffix(_translate("MainWindow", " %"))
        self.btnFolder.setToolTip(_translate("MainWindow", "Folder"))
        self.btnBook.setToolTip(_translate("MainWindow", "Read"))
        self.btnDounload.setToolTip(_translate("MainWindow", "Download"))
        self.btnTelegram.setToolTip(_translate("MainWindow", "Telegramm"))
        self.btnContrast.setToolTip(_translate("MainWindow", "Contrast"))
        self.btnSearch.setToolTip(_translate("MainWindow", "Search"))
        self.btnProfile.setToolTip(_translate("MainWindow", "Login"))
        self.btnInformation.setToolTip(_translate("MainWindow", "Information"))
        self.lblRenderPage.setText(_translate("MainWindow", "Откройте файл"))

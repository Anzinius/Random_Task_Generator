# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 580)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbl_preview = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_preview.setGeometry(QtCore.QRect(510, 70, 441, 411))
        self.tbl_preview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_preview.setObjectName("tbl_preview")
        self.tbl_preview.setColumnCount(2)
        self.tbl_preview.setRowCount(25)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_preview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_preview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_preview.setItem(18, 1, item)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(220, 490, 131, 31))
        self.btn_clear.setObjectName("btn_clear")
        self.box_search = QtWidgets.QGroupBox(self.centralwidget)
        self.box_search.setGeometry(QtCore.QRect(40, 30, 451, 451))
        self.box_search.setObjectName("box_search")
        self.label_date = QtWidgets.QLabel(self.box_search)
        self.label_date.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.label_date.setObjectName("label_date")
        self.label_xlsx = QtWidgets.QLabel(self.box_search)
        self.label_xlsx.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label_xlsx.setObjectName("label_xlsx")
        self.input_upload_xlsx = QtWidgets.QLineEdit(self.box_search)
        self.input_upload_xlsx.setGeometry(QtCore.QRect(90, 50, 231, 21))
        self.input_upload_xlsx.setObjectName("input_upload_xlsx")
        self.btn_open_xlsx = QtWidgets.QPushButton(self.box_search)
        self.btn_open_xlsx.setGeometry(QtCore.QRect(330, 50, 101, 23))
        self.btn_open_xlsx.setObjectName("btn_open_xlsx")
        self.groupBox = QtWidgets.QGroupBox(self.box_search)
        self.groupBox.setGeometry(QtCore.QRect(90, 90, 231, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.input_qut_first = QtWidgets.QRadioButton(self.groupBox)
        self.input_qut_first.setGeometry(QtCore.QRect(10, 10, 90, 16))
        self.input_qut_first.setObjectName("input_qut_first")
        self.input_qut_second = QtWidgets.QRadioButton(self.groupBox)
        self.input_qut_second.setGeometry(QtCore.QRect(10, 30, 90, 16))
        self.input_qut_second.setObjectName("input_qut_second")
        self.input_qut_third = QtWidgets.QRadioButton(self.groupBox)
        self.input_qut_third.setGeometry(QtCore.QRect(10, 50, 90, 16))
        self.input_qut_third.setObjectName("input_qut_third")
        self.input_qut_fourth = QtWidgets.QRadioButton(self.groupBox)
        self.input_qut_fourth.setGeometry(QtCore.QRect(10, 70, 90, 16))
        self.input_qut_fourth.setObjectName("input_qut_fourth")
        self.progressBar = QtWidgets.QProgressBar(self.box_search)
        self.progressBar.setGeometry(QtCore.QRect(0, 430, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(760, 30, 191, 31))
        self.btn_download.setObjectName("btn_download")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(360, 490, 131, 31))
        self.btn_search.setObjectName("btn_search")
        self.label_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_preview.setGeometry(QtCore.QRect(520, 40, 141, 21))
        self.label_preview.setObjectName("label_preview")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(60, 490, 61, 21))
        self.label_result.setObjectName("label_result")
        self.label_result_value = QtWidgets.QLabel(self.centralwidget)
        self.label_result_value.setGeometry(QtCore.QRect(120, 490, 41, 21))
        self.label_result_value.setText("")
        self.label_result_value.setObjectName("label_result_value")
        self.btn_print = QtWidgets.QPushButton(self.centralwidget)
        self.btn_print.setGeometry(QtCore.QRect(770, 490, 181, 31))
        self.btn_print.setObjectName("btn_print")
        self.label_result_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_result_2.setGeometry(QtCore.QRect(400, 540, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Light")
        font.setPointSize(6)
        self.label_result_2.setFont(font)
        self.label_result_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_result_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_result_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result_2.setObjectName("label_result_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "야근대장 자동생성 프로그램"))
        item = self.tbl_preview.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "         연구원명          "))
        item = self.tbl_preview.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "업무"))
        __sortingEnabled = self.tbl_preview.isSortingEnabled()
        self.tbl_preview.setSortingEnabled(False)
        self.tbl_preview.setSortingEnabled(__sortingEnabled)
        self.btn_clear.setText(_translate("MainWindow", "초기화"))
        self.box_search.setTitle(_translate("MainWindow", "조건 입력하기"))
        self.label_date.setText(_translate("MainWindow", " 날짜 입력"))
        self.label_xlsx.setText(_translate("MainWindow", " 통합 파일"))
        self.input_upload_xlsx.setText(_translate("MainWindow", "*.xlsx 업로드"))
        self.btn_open_xlsx.setText(_translate("MainWindow", "열기"))
        self.input_qut_first.setText(_translate("MainWindow", "1분기"))
        self.input_qut_second.setText(_translate("MainWindow", "2분기"))
        self.input_qut_third.setText(_translate("MainWindow", "3분기"))
        self.input_qut_fourth.setText(_translate("MainWindow", "4분기"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.btn_download.setText(_translate("MainWindow", "전체결과 다운로드(엑셀)"))
        self.btn_search.setText(_translate("MainWindow", "생성"))
        self.label_preview.setText(_translate("MainWindow", "<미리보기>"))
        self.label_result.setText(_translate("MainWindow", "결과(개) : "))
        self.btn_print.setText(_translate("MainWindow", "샘플 (재)출력하기"))
        self.label_result_2.setText(_translate("MainWindow", "Copyright 2020. Anzinius all rights reserved."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import uic
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from openpyxl.utils import datetime

ui_path = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(os.path.join(ui_path, "main.ui"))[0]

class MyWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__(),
        self.setupUi(self)

        self.btn_open_keyword.clicked.connect(self.btnUploadClicked1)
        self.btn_open_member.clicked.connect(self.btnUploadClicked2)
        self.btn_open_xlsx.clicked.connect(self.btnUploadClicked3)
        self.btn_search.clicked.connect(self.btnGenerateClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)
        self.btn_download.clicked.connect(self.btnDownloadClicked)

        self.xlsx = str()
        self.keyword = []
        self.member = []
        self.works = []
        self.result = []

    def setTaskByKeyword(self, file):
        allTasks = []
        sheetKeyword = file['keyword']
        sheetWork = file['work']
        keywords = []
        works = []
        for row in range(1,sheetKeyword.max_row):
            keywords.append(sheetKeyword.cell(row, 1).value)
        for row in range(1,sheetWork.max_row):
            works.append(sheetWork.cell(row,1).value)
 
        for a in keywords:
            for b in works:
                allTasks.append([a+" "+b, b])
                print([a+" "+b, b])
       # self.result = allTasks #TEMP

    def setTaskByPosition(self):
        pass

    def filterTaskByDate(self):
        pass

    def printPreview(self):
        pass

    def btnClearClicked(self):
        self.input_date.setText('')
        self.input_upload_keyword.setText('')
        self.input_upload_member.setText('')
        self.input_upload_xlsx.setText('')

    def btnGenerateClicked(self):
        # read
        load_file = load_workbook(self.xlsx, data_only=True)
        load_result = load_file['result']
        print(type(load_file))
        print(type(load_result))
        print(load_result.cell(row=1, column=1).value)
        try:
            pass
        except OSError:
            pass
        except TypeError:
            pass

        self.setTaskByPosition()
        self.setTaskByKeyword(load_file)
        self.filterTaskByDate()
        self.printPreview()

    def btnDownloadClicked(self):
        result_file = Workbook()
        result_sheet = result_file.create_sheet('result')
        #for cell in self.result:
        #    for row in len(self.result):
       #         result_sheet[row].append(cell)
        #result_file.save('./result' + datetime.today().strftime("%Y%m%d%H%M%S") + '.xlsx')
        result_file.save('./result' + '.xlsx')
        
        pass
    
    def btnUploadClicked1(self):
        pass

    def btnUploadClicked2(self):
        pass

    def btnUploadClicked3(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self)
        self.input_upload_xlsx.setText(fname[0])
        self.xlsx = fname[0]
        print(self.xlsx)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

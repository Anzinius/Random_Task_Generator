import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import uic
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from datetime import datetime

# path to ui file
ui_path = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(os.path.join(ui_path, "main.ui"))[0]

# Make window not to shut down when exception occurs
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)
# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook
# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

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
        self.work = []
        self.result = []
        self.task = []

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
                #print([a+" "+b, b])
        #self.result = allTasks #TEMP
        self.task = allTasks #TEMP

    def setTaskByPosition(self, file):
        sheetMember = file['member']
        sheetPosition = file['position']
        members = []
        positions = []
        for row in range(2, sheetMember.max_row + 1):
            members.append([sheetMember.cell(row, 1).value, sheetMember.cell(row, 2).value])
        for row in range(2, sheetPosition.max_row + 1):
            positions.append([sheetPosition.cell(row, 1).value, sheetPosition.cell(row, 2).value])
        for a, b in members:
            for x, y in positions:
                if b == y:
                    self.member.append([a, b, x])

        for a, b, c in self.member:
            for x, y in self.task:
                for m, n in self.work:
                    if m == y and int(n) == 0:
                        self.result.append([x, y, a, b, c])
                    elif m == y and int(n) > 0:
                        if c >= n:
                            self.result.append([x, y, a, b, c])
                    elif m == y and int(n) < 0:
                        if -c <= n :
                            self.result.append([x, y, a, b, c])

    def filterTaskByDate(self, file):
        sheetWork = file['work']
        month = self.input_date.date().month()
        if month in [1, 2, 3, 4, 5, 6]:
            workFrom = 2
            workTo = 12
        elif month in [7, 8, 9, 10, 11, 12]:
            workFrom = 6
            workTo = 25

        #filter
        for row in range(workFrom, workTo):
            self.work.append([sheetWork.cell(row, 1).value, sheetWork.cell(row, 2).value])

    def printPreview(self):
        pass

    def btnClearClicked(self):
        self.input_date.setText('')
        self.input_upload_keyword.setText('')
        self.input_upload_member.setText('')
        self.input_upload_xlsx.setText('')
        self.label_result_value.setText('')

    def btnGenerateClicked(self):
        # initialize

        # error
        if len(self.xlsx) == 0:
            QtWidgets.QMessageBox.warning(self, "주의", "파일을 먼저 선택해주세요.    ")
            return

        # read
        load_file = load_workbook(self.xlsx, data_only=True)
 
        try:
            self.filterTaskByDate(load_file)
            self.setTaskByKeyword(load_file)
            self.setTaskByPosition(load_file)
            self.printPreview()
        except OSError:
            pass
        except TypeError:
            pass
        self.label_result_value.setText(str(len(self.result)))

    def btnDownloadClicked(self):
        result_file = Workbook()
        result_sheet = result_file.create_sheet('result')
        result_sheet['A1'] = "업무(결과값)"
        result_sheet['B1'] = "수행 내용"
        result_sheet['C1'] = "이름"
        result_sheet['D1'] = "직급"
        result_sheet['E1'] = "직급 NO."
        for cell in self.result:
            result_sheet.append(cell)
        result_file.save('./result' + datetime.today().strftime("%Y%m%d%H%M%S") + '.xlsx') 
        QtWidgets.QMessageBox.about(self, "저장완료", "파일이 저장되었습니다.")  

    def btnUploadClicked1(self):
        pass

    def btnUploadClicked2(self):
        pass
    
    def btnUploadClicked3(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self)
        self.input_upload_xlsx.setText(fname[0])
        self.xlsx = fname[0]
        #print(self.xlsx)
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

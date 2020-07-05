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

        self.btn_open_xlsx.clicked.connect(self.btnUploadClicked)
        self.btn_search.clicked.connect(self.btnGenerateClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)
        self.btn_download.clicked.connect(self.btnDownloadClicked)
        
        self.xlsx = str()
        self.quarter = int()
        self.keyword = []
        self.member = []
        self.work = []
        self.result = []
        self.task = []
        self.allTasks = []

    def setTaskByKeyword(self, file):
        allTasks = []
        sheetKeyword = file['keyword']
        keywords = []
        works = []
        for row in range(1,sheetKeyword.max_row+1):
            keywords.append(sheetKeyword.cell(row, 1).value)
        for i in range(len(self.work)):
            works.append(self.work[i][0])
        
        for a in keywords:
            A = []
            A.append(a)
            for b in works:
                allTasks.append([A[0]+" "+b, b])
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

        cnt = 0
        for a, b, c in self.member:
            for x, y in self.task:
                for m, n in self.work:
                    cnt += 1
                    if m == y and int(n) == 0:
                        self.result.append([x, y, a, b, c])
                        print("1 : ", self.result)
                    elif m == y and int(n) > 0:
                        if c >= n:
                            self.result.append([x, y, a, b, c])
                    elif m == y and int(n) < 0:
                        if -c <= n :
                            self.result.append([x, y, a, b, c])

#        cnt = 0
#        for a, b, c in self.member:
#            for x, y in self.task:
#                for m, n in self.work:
#                    cnt += 1
#                    if int(n) == 0:
#                        if m == y:
#                            self.result.append([x, y, a, b, c])
#                            print("1 : ", self.result)
#                    elif int(n) > 0:
#                        if c >= n and m == y:
#                            self.result.append([x, y, a, b, c])
#                    elif int(n) < 0:
#                        if -c <= n and m == y:
#                            self.result.append([x, y, a, b, c])

        print("result : ", self.result)
        print(cnt)

    def filterTaskByDate(self, file):
        sheetWork = file['work']
        for row in range(2, sheetWork.max_row + 1):
            if sheetWork.cell(row, self.quarter + 4).value == True:
                self.work.append([sheetWork.cell(row, 2).value, sheetWork.cell(row, 3).value])

    def printPreview(self):
        pass

    def btnClearClicked(self):
        self.input_date.setText('')
        self.input_upload_keyword.setText('')
        self.input_upload_member.setText('')
        self.input_upload_xlsx.setText('')
        self.label_result_value.setText('')

    def quarterisChecked(self):
        if self.box_search_input_qut_first.isChecked(): self.quarter = 1
        elif self.box_search_input_qut_second.isChecked(): self.quarter = 2
        elif self.box_search_input_qut_third.isChecked(): self.quarter = 3
        elif self.box_search_input_qut_fourth.isChecked(): self.quarter = 4
        else:
            pass
        
    def btnGenerateClicked(self):
        # initialize

        # error
        if len(self.xlsx) == 0:
            QtWidgets.QMessageBox.warning(self, "주의", "파일을 먼저 선택해주세요.    ")
            return

        try :
            self.quarterisChecked()
        except :
            pass

        # read
        load_file = load_workbook(self.xlsx, data_only=True)

        try:
            self.filterTaskByDate(load_file)
            self.setTaskByKeyword(load_file)
            self.setTaskByPosition(load_file)
            self.printPreview()
        except OSError:
            print("err1")
        except TypeError:
            print("err2")
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

    def btnUploadClicked(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self)
        self.input_upload_xlsx.setText(fname[0])
        self.xlsx = fname[0]
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

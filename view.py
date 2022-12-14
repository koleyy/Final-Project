# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.button_calculate.setGeometry(QtCore.QRect(30, 160, 161, 41))
        self.button_calculate.setObjectName("button_calculate")
        self.label_credits = QtWidgets.QLabel(self.centralwidget)
        self.label_credits.setGeometry(QtCore.QRect(30, 50, 101, 21))
        self.label_credits.setObjectName("label_credits")
        self.label_grade = QtWidgets.QLabel(self.centralwidget)
        self.label_grade.setGeometry(QtCore.QRect(30, 110, 161, 16))
        self.label_grade.setObjectName("label_grade")
        self.text_credits = QtWidgets.QTextEdit(self.centralwidget)
        self.text_credits.setGeometry(QtCore.QRect(190, 40, 161, 41))
        self.text_credits.setObjectName("text_credits")
        self.text_grade = QtWidgets.QTextEdit(self.centralwidget)
        self.text_grade.setGeometry(QtCore.QRect(190, 100, 161, 41))
        self.text_grade.setObjectName("text_grade")
        self.label_gpa_text = QtWidgets.QLabel(self.centralwidget)
        self.label_gpa_text.setGeometry(QtCore.QRect(200, 170, 101, 16))
        self.label_gpa_text.setObjectName("label_gpa_text")
        self.label_gpa_value = QtWidgets.QLabel(self.centralwidget)
        self.label_gpa_value.setGeometry(QtCore.QRect(290, 170, 111, 16))
        self.label_gpa_value.setObjectName("label_gpa_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        self.menuGPA_CALCULATOR = QtWidgets.QMenu(self.menubar)
        self.menuGPA_CALCULATOR.setObjectName("menuGPA_CALCULATOR")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGPA_CALCULATOR.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_calculate.setText(_translate("MainWindow", "CALCULATE"))
        self.label_credits.setText(_translate("MainWindow", "CREDITS"))
        self.label_grade.setText(_translate("MainWindow", "LETTER GRADE"))
        self.label_gpa_text.setText(_translate("MainWindow", "YOUR GPA IS: "))
        self.label_gpa_value.setText(_translate("MainWindow", "0"))
        self.menuGPA_CALCULATOR.setTitle(_translate("MainWindow", "GPA CALCULATOR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

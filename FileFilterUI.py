# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\filefilter.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.m_date = QtWidgets.QLineEdit(self.centralwidget)
        self.m_date.setGeometry(QtCore.QRect(210, 10, 81, 20))
        self.m_date.setObjectName("m_date")
        self.m_ext = QtWidgets.QLineEdit(self.centralwidget)
        self.m_ext.setGeometry(QtCore.QRect(150, 10, 51, 20))
        self.m_ext.setObjectName("m_ext")
        self.m_input_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.m_input_folder.setGeometry(QtCore.QRect(11, 10, 133, 20))
        self.m_input_folder.setObjectName("m_input_folder")
        self.m_btn_process = QtWidgets.QPushButton(self.centralwidget)
        self.m_btn_process.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.m_btn_process.setObjectName("m_btn_process")
        self.m_input_exel_path = QtWidgets.QLineEdit(self.centralwidget)
        self.m_input_exel_path.setGeometry(QtCore.QRect(10, 60, 281, 20))
        self.m_input_exel_path.setObjectName("m_input_exel_path")
        self.m_btn_import = QtWidgets.QPushButton(self.centralwidget)
        self.m_btn_import.setGeometry(QtCore.QRect(310, 60, 75, 23))
        self.m_btn_import.setObjectName("m_btn_import")
        self.m_output_excel_path = QtWidgets.QLineEdit(self.centralwidget)
        self.m_output_excel_path.setGeometry(QtCore.QRect(10, 110, 281, 20))
        self.m_output_excel_path.setObjectName("m_output_excel_path")
        self.m_btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.m_btn_export.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.m_btn_export.setObjectName("m_btn_export")
        self.m_table = QtWidgets.QTableWidget(self.centralwidget)
        self.m_table.setGeometry(QtCore.QRect(420, 10, 411, 301))
        self.m_table.setMaximumSize(QtCore.QSize(411, 16777215))
        self.m_table.setObjectName("m_table")
        self.m_table.setColumnCount(2)
        self.m_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.m_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.m_table.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.m_btn_process.setText(_translate("MainWindow", "Process"))
        self.m_btn_import.setText(_translate("MainWindow", "Import"))
        self.m_btn_export.setText(_translate("MainWindow", "Export"))
        item = self.m_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File name"))
        item = self.m_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

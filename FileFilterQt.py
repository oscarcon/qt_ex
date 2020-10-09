import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from FileFilter import FileHandler
from FileFilterUI import Ui_MainWindow
from AWindowsUI import Ui_Dialog


class AWindows(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class FileFilterQt(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.m_btn_process.clicked.connect(self.on_clicked_btn_process)
        self.ui.m_btn_import.clicked.connect(self.on_clicked_btn_import)
        self.ui.m_btn_export.clicked.connect(self.on_clicked_btn_export)

        self.file_handler = FileHandler()

    def _show_data_on_table(self):
        self.ui.m_table.setRowCount(0)
        row_count = 0
        for file, folders in self.found_files_dict.items():
            for folder in folders:
                self.ui.m_table.insertRow(row_count)
                self.ui.m_table.setItem(
                    row_count, 0, QtWidgets.QTableWidgetItem(file))
                self.ui.m_table.setItem(
                    row_count, 1, QtWidgets.QTableWidgetItem(folder))
                row_count += 1

    def on_clicked_btn_process(self):
        # print('Process button clicked')
        # folder = str(self.ui.m_input_folder.text())
        # ext = str(self.ui.m_ext.text())
        # date = str(self.ui.m_date.text())
        # print(folder, ext, date)
        # self.found_files_dict = self.file_handler.file_filter(
        #     folder, ext, date)
        # self._show_data_on_table()
        self.w = AWindows()
        self.w.exec()

    def on_clicked_btn_import(self):
        input_path = str(self.ui.m_input_exel_path.text())
        self.found_files_dict = self.file_handler.import_from_excel(input_path)
        self._show_data_on_table()

    def on_clicked_btn_export(self):
        output_path = str(self.ui.m_output_excel_path.text())
        self.file_handler.export_to_excel(self.found_files_dict, output_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt = FileFilterQt()
    qt.show()
    sys.exit(app.exec_())

import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QAbstractScrollArea, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox, QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Schedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="timetable_db",
                                     user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_schedule_tab(self):
        self.schedule_tab = QWidget()
        self.tabs.addTab(self.schedule_tab, "Schedule")

        self.monday_gbox = QGroupBox("Monday")
        self.tuesday_gbox = QGroupBox("Tuesday")
        self.wednesday_gbox = QGroupBox("Wednesday")
        self.thursday_gbox = QGroupBox("Thursday")
        self.friday_gbox = QGroupBox("Friday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)
        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)

        self.shbox1.addWidget(self.monday_gbox)
        self.shbox2.addWidget(self.tuesday_gbox)
        self.shbox3.addWidget(self.wednesday_gbox)
        self.shbox4.addWidget(self.thursday_gbox)
        self.shbox5.addWidget(self.friday_gbox)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()

        self.update_schedule_button = QPushButton("Update")
        self.shbox6.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(4)
        self.monday_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "Teacher"])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='monday'")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.monday_table.resizeRowsToContents()

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(4)
        self.tuesday_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "Teacher"])

        self._update_tuesday_table()

        self.tuvbox = QVBoxLayout()
        self.tuvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.tuvbox)

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='tuesday'")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.tuesday_table.resizeRowsToContents()

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(4)
        self.wednesday_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "Teacher"])

        self._update_wednesday_table()

        self.wvbox = QVBoxLayout()
        self.wvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.wvbox)

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='wednesday'")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.wednesday_table.resizeRowsToContents()

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(4)
        self.thursday_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "Teacher"])

        self._update_thursday_table()

        self.thvbox = QVBoxLayout()
        self.thvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.thvbox)

    def _update_thursday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='thursday'")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.thursday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.thursay_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.thursday_table.resizeRowsToContents()

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(4)
        self.friday_table.setHorizontalHeaderLabels(["Subject", "Time", "Room", "Teacher"])

        self._update_friday_table()

        self.fvbox = QVBoxLayout()
        self.fvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.fvbox)

    def _update_friday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='friday'")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.friday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.friday_table.resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _update_schedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thuersday_table()
        self._update_friday_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

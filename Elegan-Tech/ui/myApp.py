from PySide2 import QtWidgets, QtCore
from Elegan import Ui_MainWindow
import connection
import serial


class MyApp(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("MyApp 3.7")
        self.progressBar.setValue(0)
        self.set_spinbox()
        self.fill_comboxes()
        connection_object.get_comport()
        self.comboBox_Port.addItem(connection_object.com_port)
        if connection_object.com_port != "No device":
            connection_object.serial_connection = serial.Serial(
                baudrate=115200,
                port=connection_object.com_port)
            print("open")
            connection_object.serial_connection.close()
            connection_object.serial_connection.setDTR(False)
        self.checkBox_Lam.stateChanged.connect(lambda: self.lam_checkbox())
        self.checkBox_Yayma.stateChanged.connect(lambda: self.yayma_checkbox())
        self.set_button_clicks()
        self.doubleSpinBox_Lam.setDisabled(1)
        self.spinBox_Aci.setDisabled(1)
        self.spinBox_Rampa.setDisabled(1)
        self.spinBox_Yayma_hizi.setDisabled(1)
        timer.timeout.connect(lambda: self.update_bar())
        times.timeout.connect(lambda: self.handle_time())

    def button_action(self, file_path, button, pressed_text, time_takes):
        if connection_object.check_connection():
            self.progressBar.setValue(0)
            son = self.load_file(file_path)
            if button is self.pushButton_Yayma:
                code = self.code_replace_yayma(son)
            elif button is self.pushButton_Lam_Al:
                code = self.code_replace_lam_birak(son)
            elif button is self.pushButton_Yikama:
                code = self.code_replace_yikama(son)
            else:
                code = son
            timer.start(time_takes)
            button.setText(pressed_text)
            self.disable_buttons(1)
            self.parse_code(code)
            times.start(100)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Device is not connected!")

    def yayma_checkbox(self):
        if self.checkBox_Yayma.isChecked():
            self.spinBox_Yayma_hizi.setEnabled(1)
            self.spinBox_Rampa.setEnabled(1)
            self.spinBox_Aci.setEnabled(1)
        else:
            self.spinBox_Yayma_hizi.setDisabled(1)
            self.spinBox_Rampa.setDisabled(1)
            self.spinBox_Aci.setDisabled(1)

    def lam_checkbox(self):
        if self.checkBox_Lam.isChecked():
            self.doubleSpinBox_Lam.setEnabled(1)
        else:
            self.doubleSpinBox_Lam.setDisabled(1)

    def code_replace_yikama(self, code):
        pump = self.comboBox_Pump.currentText()
        if pump == "Pump 1":
            son = code
        elif pump == "Pump 2":
            son = code.replace("= 1 :", "= 2 :")
        elif pump == "Pump 3":
            son = code.replace("= 1 :", "= 2 :").replace("T0", "T1")
        elif pump == "Pump 4":
            son = code.replace("= 1 :", "= 3 :").replace("T0", "T1")
        elif pump == "Pump 5":
            son = code.replace("= 1 :", "= 4 :")
        else:
            son = code.replace("= 1 :", "= 4 :").replace("T0", "T1")
        return son

    def code_replace_lam_birak(self, code):
        if self.checkBox_Lam.isChecked():
            lam = self.doubleSpinBox_Lam.value()
            son = code.replace("LAM", "Y" + str(lam))
        else:
            sale = self.comboBox_Lam.currentText()
            if sale == "Şale 1":
                son = code.replace("LAM", "Y46")
            elif sale == "Şale 2":
                son = code.replace("LAM", "Y41")
            elif sale == "Şale 3":
                son = code.replace("LAM", "Y34.5")
            elif sale == "Şale 4":
                son = code.replace("LAM", "Y28")
            elif sale == "Şale 5":
                son = code.replace("LAM", "Y22.5")
            else:
                son = code.replace("LAM", "Y16.5")
        return son

    def code_replace_yayma(self, code):
        miktar = self.comboBox_Miktar.currentText()
        tup = self.comboBox_Tup.currentText()
        if self.checkBox_Yayma.isChecked():
            yayma_hizi = self.spinBox_Yayma_hizi.text()
            rampa = self.spinBox_Rampa.text()
            yayma_aci = self.spinBox_Aci.text()
            x = code.replace("HIZ", "F" + yayma_hizi).replace("AÇI", "Z" + yayma_aci).replace("RAMPA_X", "X" + rampa)
        else:
            x = code.replace("HIZ", "F10000").replace("AÇI", "Z5").replace("RAMPA_X", "X1000")
        if tup == "Tüp 1":
            y = x.replace("TÜP", "Y198.5")
        elif tup == "Tüp 2":
            y = x.replace("TÜP", "Y180.5")
        elif tup == "Tüp 3":
            y = x.replace("TÜP", "Y162.5")
        elif tup == "Tüp 4":
            y = x.replace("TÜP", "Y144.5")
        elif tup == "Tüp 5":
            y = x.replace("TÜP", "Y126.5")
        elif tup == "Tüp 6":
            y = x.replace("TÜP", "Y108.5")
        elif tup == "Tüp 7":
            y = x.replace("TÜP", "Y90.5")
        elif tup == "Tüp 8":
            y = x.replace("TÜP", "Y72.5")
        elif tup == "Tüp 9":
            y = x.replace("TÜP", "Y54.5")
        else:
            y = x.replace("TÜP", "Y36.5")

        if miktar == "3 UL":
            son = y.replace("X_MIKTAR", "X32.5").replace("MİKTAR", "X168")
        elif miktar == "4 UL":
            son = y.replace("X_MIKTAR", "X30").replace("MİKTAR", "X168")
        elif miktar == "5 UL":
            son = y.replace("X_MIKTAR", "X27.5").replace("MİKTAR", "X168")
        elif miktar == "6 UL":
            son = y.replace("X_MIKTAR", "X25").replace("MİKTAR", "X168")
        elif miktar == "7 UL":
            son = y.replace("X_MIKTAR", "X20").replace("MİKTAR", "X169")
        elif miktar == "8 UL":
            son = y.replace("X_MIKTAR", "X19").replace("MİKTAR", "X169")
        elif miktar == "9 UL":
            son = y.replace("X_MIKTAR", "X18").replace("MİKTAR", "X169")
        else:
            son = y.replace("X_MIKTAR", "X17").replace("MİKTAR", "X169")
        return son

    def update_bar(self):
        val = self.progressBar.value()
        self.progressBar.setValue(val + 1)
        if val == 100:
            # self.pushButton_Yayma.setText(button_text)
            self.pushButton_Reset.setText("Reset")
            self.pushButton_Yikama.setText("Yıkama")
            self.pushButton_Lam_Al.setText("Lam Bırak")
            self.pushButton_Yayma.setText("Kanı Yay")
            self.pushButton_4_Methanol.setText("Methanol")
            self.pushButton_May_G.setText("May Grunwald")
            self.pushButton_Kurutma.setText("Kurutma")
            self.pushButton_Yikama_after_May_G.setText("Yıkama 1")
            self.pushButton_May_G_Cozelti.setText("May Grunwald\n Çözeltisi")
            self.pushButton_Yikama_After_Cozelti.setText("Yıkama 2")
            self.pushButton_Giemsa.setText("Giemsa")
            self.pushButton_yikama_after_giemsa.setText("Yıkama 3")
            self.pushButton_Birakma.setText("Bırakma")
            self.pushButton_Igne_Yikama.setText("İğne Yıkama")
            self.pushButton_start.setText("START")
            self.disable_buttons(0)

    def set_spinbox(self):
        self.spinBox_Aci.setMinimum(0)
        self.spinBox_Aci.setMaximum(130)
        self.spinBox_Aci.setSingleStep(1)
        self.spinBox_Aci.setValue(0)
        self.spinBox_Rampa.setMinimum(0)
        self.spinBox_Rampa.setMaximum(25000)
        self.spinBox_Rampa.setSingleStep(1)
        self.spinBox_Rampa.setValue(0)
        self.spinBox_Yayma_hizi.setMinimum(0)
        self.spinBox_Yayma_hizi.setMaximum(25000)
        self.spinBox_Yayma_hizi.setSingleStep(1)
        self.spinBox_Yayma_hizi.setValue(0)

    def load_file(self, path):
        file = QtCore.QFile(path)
        if not file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            QtWidgets.QMessageBox.warning(self, "Error!", file.errorString())
            return
        stream = QtCore.QTextStream(file)
        code = stream.readAll()
        file.close()
        return code

    def parse_code(self, code):
        rows = code.splitlines()
        for lines in rows:
            if lines:
                a = lines.split()
                while len(parsed_code) - 1 < int(a[0]):
                    parsed_code.append("")
                parsed_code[int(a[0])] += str(' '.join(a[2:])) + "\n"
        return parsed_code

    def initiliaze_variables(self):
        global code_index
        global time_counter
        del parsed_code[:]
        times.stop()
        time_counter = 0
        code_index = 0

    def handle_time(self):
        global code_index
        global time_counter
        if code_index < len(parsed_code):
            while parsed_code[code_index] == '':
                code_index += 1
            if time_counter == code_index:
                exact_time = QtCore.QTime.currentTime()
                connection_object.write_data_to_port(parsed_code[time_counter])
                self.textBrowser.append("**************" + exact_time.toString("hh : mm : ss : ms") +
                                        "**************\n\n" + parsed_code[time_counter])
                code_index += 1
            time_counter += 1
            times.start(1000)
        else:
            self.initiliaze_variables()

    def fill_comboxes(self):
        for i in range(1, 11):
            self.comboBox_Tup.addItem("Tüp " + str(i))
        for k in range(3, 11):
            self.comboBox_Miktar.addItem(str(k) + " UL")
        for m in range(1, 7):
            self.comboBox_Lam.addItem("Şale " + str(m))
            self.comboBox_Pump.addItem("Pump " + str(m))

    def disable_buttons(self, val):
        buttons = {self.pushButton_Yikama, self.pushButton_Connect, self.pushButton_Yayma,
                   self.pushButton_Lam_Al, self.pushButton_Reset, self.pushButton_4_Methanol,
                   self.pushButton_Disconnect, self.pushButton_May_G, self.pushButton_start,
                   self.pushButton_Kurutma, self.pushButton_Yikama_after_May_G, self.pushButton_May_G_Cozelti,
                   self.pushButton_Yikama_After_Cozelti, self.pushButton_Giemsa,
                   self.pushButton_yikama_after_giemsa, self.pushButton_Birakma, self.pushButton_Igne_Yikama}
        for button in buttons:
            if val == 1:
                button.setDisabled(True)
            else:
                button.setEnabled(True)

    def set_button_clicks(self):
        self.pushButton_Disconnect.clicked.connect(lambda: connection_object.dis_connect(parsed_code, qt_app))
        self.pushButton_Connect.clicked.connect(lambda: connection_object.connect(parsed_code, qt_app))
        self.pushButton_start.clicked.connect(
            lambda: self.button_action("resources/G_code/Start.txt", self.pushButton_start, "STARTED", 100))
        self.pushButton_May_G.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Kurutma Al May.G Koy.txt",
                                       self.pushButton_May_G,
                                       "May Grunwald İşlemi\n Yapılıyor", 100))
        self.pushButton_4_Methanol.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Şale Alma Methanol Koy.txt",
                                       self.pushButton_4_Methanol, "Methanol İşlemi\n Yapılıyor", 100))
        self.pushButton_Yayma.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Yayma.txt",
                                       self.pushButton_Yayma, "Yayma Devam Ediyor",
                                       100))
        self.pushButton_Reset.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Başlangıç Home.txt",
                                       self.pushButton_Reset, "Resetleniyor", 100))
        self.pushButton_Lam_Al.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Lam Alma 1.txt",
                                       self.pushButton_Lam_Al, "Lam Bırakılıyor",
                                       100))
        self.pushButton_Yikama.clicked.connect(
            lambda: self.button_action(":G_code/G_code/1. Pump yıkama.txt",
                                       self.pushButton_Yikama, "Yıkanıyor", 100))
        self.pushButton_Kurutma.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Metanol Al Kurutma İçin Beklet.txt",
                                       self.pushButton_Kurutma, "Kurutma İşlemi\n Yapılıyor", 100))
        self.pushButton_Yikama_after_May_G.clicked.connect(
            lambda: self.button_action(":G_code/G_code/May G. Al Yıkama Git.txt",
                                       self.pushButton_Yikama_after_May_G, "Yıkama 1 İşlemi\n Yapılıyor", 100))
        self.pushButton_May_G_Cozelti.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Yıkama Al May G. Çözelti Git.txt",
                                       self.pushButton_May_G_Cozelti, "May Grunwald Çözeltisi\n İşlemi Yapılıyor", 100))
        self.pushButton_Yikama_After_Cozelti.clicked.connect(
            lambda: self.button_action(":G_code/G_code/May G. Çözeltisi  Al Yıkama Git.txt",
                                       self.pushButton_Yikama_After_Cozelti, "Yıkama 2 İşlemi\nYapılıyor", 100))
        self.pushButton_Giemsa.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Yıkama Al Geimsa Gİt.txt",
                                       self.pushButton_Giemsa, "Giemsa İşlemi\nYapılıyor", 100))
        self.pushButton_yikama_after_giemsa.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Giemsa Al Yıkama Git.txt",
                                       self.pushButton_yikama_after_giemsa, "Yikama 3 İşlemi\nYapılıyor", 100))
        self.pushButton_Birakma.clicked.connect(
            lambda: self.button_action(":G_code/G_code/Yıkama Al Finish.txt",
                                       self.pushButton_Birakma, "Bırakma İşlemi\nYapılıyor", 100))
        self.pushButton_Igne_Yikama.clicked.connect(
            lambda: self.button_action(":G_code/G_code/İğne Yıkama.txt",
                                       self.pushButton_Igne_Yikama, "İğne Yıkama\n İşlemi Yapılıyor", 100))
        self.pushButton_Stop.clicked.connect(lambda: self.disable_motors_and_stop("1 : M112\n2 : M112\n3 : M112\n4 : M112"))
        self.pushButton_disable_motors.clicked.connect(lambda: self.disable_motors_and_stop("1 : M18\n2 : M18\n3 : M18\n4 : M18"))

    def disable_motors_and_stop(self, code):
        if connection_object.check_connection():
            connection_object.write_data_to_port(code)
            self.initiliaze_variables()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Device is not connected!")


if __name__ == '__main__':
    timer = QtCore.QTimer()
    times = QtCore.QTimer()
    parsed_code = []
    code_index = 0
    time_counter = 0
    connection_object = connection.Arduino()
    app = QtWidgets.QApplication()
    qt_app = MyApp()
    qt_app.show()
    app.exec_()

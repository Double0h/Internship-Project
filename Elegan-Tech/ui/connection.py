from serial.tools import list_ports
from PySide2 import QtWidgets


class Singleton:
    def __init__(self, arduino_klass):
        self.decorated_klass = arduino_klass
        self.arduino_instance = None

    def __call__(self):
        if self.arduino_instance is None:
            self.arduino_instance = self.decorated_klass()
        return self.arduino_instance


@Singleton
class Arduino:
    def __init__(self):
        self.com_port = "No device"
        self.serial_connection = None

    def get_comport(self):
        comports = list(list_ports.comports())
        for port in comports:
            if "wch.cn" in port.manufacturer:
                self.com_port = port.device

    def connect(self, code, app):
        try:
            if not self.serial_connection.isOpen():
                self.serial_connection.open()
                app.textBrowser.append("Connected")
                del code[:]
        except:
            QtWidgets.QMessageBox.warning(app, "Error", "No device to connect!")

    def write_data_to_port(self, data):
        print(data)
        self.serial_connection.flushInput()
        self.serial_connection.flushOutput()
        inp_bytes = str.encode(data)
        self.serial_connection.write(inp_bytes + b'\r\n')
        out = b''
        while self.serial_connection.inWaiting() > 0:
            out += self.serial_connection.read(1)
        if out != b'':
            print(">>", out)

    def dis_connect(self, code, app):
        try:
            if self.serial_connection.isOpen():
                self.serial_connection.close()
                app.textBrowser.append("Disconnected")
                del code[:]
        except:
            QtWidgets.QMessageBox.warning(app, "Error", "No device to disconnect!")

    def check_connection(self):
        try:
            if self.serial_connection.isOpen():
                return True
            else:
                return False
        except:
            return False

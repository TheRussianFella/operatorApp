from PyQt5.QtCore import QObject, pyqtSignal
from enumFunction import enum
from Printer import Printer
import sys, glob, serial, time


class Machine(QObject):


    completedSignal = pyqtSignal(name = "completedSignal")
    achtungSignal = pyqtSignal(name = "achtungSignal")
    newElement = pyqtSignal(name = "newElement")

    errorCodes = enum(ACHTUNG = b'0')
    goodCodes = enum(ACHTUNG_GONE = b'1', NEW_SHEET = b'2', NEW_SLIDE = b'3',
                     MACHINE_ASK = b'?', MACHINE_ANSWER = b'+')

    def __init__(self):

        QObject.__init__(self)

        if sys.platform.startswith("win"):
            self.ports = ["COM%s" % (i + 1) for i in range(256)]
        elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            self.ports = glob.glob("/dev/tty[A-Za-z]*")
        elif sys.platform.startswith("darvin"):
            self.ports = glob.glob("/dev/tty.*")
        else:
            print("error")

        self.workingPorts = []

        for port in self.ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.workingPorts.append(port)
            except (OSError, serial.SerialException):
                continue

        for port in self.workingPorts:
            ser = serial.Serial(port, 9600, timeout = 3.0)
            time.sleep(2)

            ser.write(self.goodCodes.MACHINE_ASK)

            time.sleep(1)

            rcv = b""
            while rcv == b"":
                rcv = ser.read()

            self.machinePortName = ''
            if rcv == self.goodCodes.MACHINE_ANSWER:
                self.machinePortName = port
            print(self.machinePortName)
            
            ser.close()

        self.hasWork = True

    def waitForSignal(self):
        machinePort = serial.Serial(self.machinePortName, 9600, timeout = 3.0)

        ans = b''
        errorIndex = 0

        while ans == b'':
            ans = machinePort.read()
            errorIndex += 1
            if errorIndex >= 10:
                ans = self.errorCodes.ACHTUNG

        machinePort.close()

        return ans

    def work(self):

        while self.hasWork:
            code = self.waitForSignal()

            if code == self.errorCodes.ACHTUNG:
                self.achtungSignal.emit()
            elif code == self.goodCodes.ACHTUNG_GONE:
                print("achtung gone")
            elif code == self.goodCodes.NEW_SHEET:
                print("new sheet needed")
            elif code == self.goodCodes.NEW_SLIDE:
                print("new slide needed")

    #def stopWork(self):

    def giveNewElement(self, element):
        print('1')

    def startPrinting(self, frontPick, backPick):
        printer = Printer()
        printer.startPrinting()

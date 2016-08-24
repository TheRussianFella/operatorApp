import sys, glob, serial, time

class Machine:

    def __init__(self):
        self.ports = scanPorts()

        for port in self.ports:
            ser = serial.Serial(port, timeout = 3.0)
            ser.write("\r\n?")

            rcv = ser.read(3)

            if rcv == "+":
                self.machinePort = port

    def scanPorts(self):
        if sys.platform.startswith("win"):
            self.ports = ["COM%s" % (i + 1) for i in range(256)]
        elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            self.ports = glob.glob("/dev/tty[A-Za-z0-9]*")
        elif sys.platform.startswith("darvin"):
            self.ports = glob.glob("/dev/tty.*")
        else:
            print("error")

        result = []
        for port in self.ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result

    def startPrinting(self, frontPick, backPick):
        print(test)

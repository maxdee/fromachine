import serial
import psutil
from collections import deque

titles = "CPU Xaxi Yaxi"

class displayor:
    def __init__(self, dev, br):
        self.duinodev = dev
        self.baud = br
        self.dat = 0
        self.pstring = 'haha'
        self.inc = 0
        try:
            self.ser = serial.Serial(self.duinodev, self.baud)
            print 'talkin to duino'
        except serial.SerialException:
            print 'this shit ' + duinodev + ' is not plugged in'
            time.sleep(3)        
    
    def update(self, x, y):
        self.inc += 1
        if self.inc > 10:
            self.inc = 0;
            cpu = '%0*d ' % (3, self.cpuer())
            valers = '                           ' + cpu + '%0*d ' % (4,abs(x)) + '%0*d ' % (4,abs(y)) 
            outer = titles + valers
            if outer != self.pstring:
                self.ser.write(outer)
                self.pstring = outer
                self.inc = 0
    
    def cpuer(self):
        ldr = int(psutil.cpu_percent())
        return ldr

    def poll(self):
        if self.ser.inWaiting()!=0:
            self.dat = int(self.ser.readline())
            self.ser.flushInput()
        return self.dat



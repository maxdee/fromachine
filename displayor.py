import serial
import psutil
import time
import bpdb
from collections import deque

titles = "CPU Xaxi Yaxi"

class displayor(object):
    def __init__(self, dev, br):
        self.duinodev = dev
        self.baud = br
        self.pstring = 'haha'
        self.but = 0
        self.prox = 0
        try:
            self.ser = serial.Serial(self.duinodev, self.baud)
            print 'talkin to duino'
        except serial.SerialException:
            print 'this shit ' + duinodev + ' is not plugged in'
            time.sleep(3)
    
    def tell(self, ha):
        self.ser.write(ha)
        self.parsly()

    def upda(self, x, y):
        cpu = '%0*d ' % (3, int(psutil.cpu_percent()))
        valers = '                           ' + cpu + '%0*d ' % (4,abs(x)) + '%0*d ' % (4,abs(y)) 
        outer = titles + valers
        self.ser.write(outer)
        self.pstring = outer
        self.parsly()

    def parsly(self):
        time.sleep(0.01)
        dert = self.ser.readline()
        nums = [int(n) for n in dert.split('/')]
        self.but = nums[0]
        self.prox = nums[1]
        self.ser.flushInput()

    def prompt(self, ask):
        print "Asking user"
        self.ser.write(ask)
        self.parsly()
        while self.but == 0:
            self.ser.write(ask)
            self.parsly()
            time.sleep(0.5)
        bat = self.but
        self.ser.write("ok")
        print "Ok, %d is pressed" % (bat)
        self.parsly()
        self.but = 0
        return bat

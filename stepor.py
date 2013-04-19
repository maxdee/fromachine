# xlim 14 ylim 15
# xstepper 7 4 17 8
# ystepper 22 10 9 11

import RPi.GPIO as GPIO
import time


seqrev = [
    [1,0,0,1],
    [0,1,0,1],
    [0,1,1,0],
    [1,0,1,0]
    ]

seq = [
    [1,0,1,0],
    [0,1,1,0],
    [0,1,0,1],
    [1,0,0,1]
    ]
#add parc mode to stop juice to coils


    
class sktep(object):    
    def __init__(self, pin1, pin2, pin3, pin4, lim, mx, sp, trs, nm):
        self.pins = [9,9,9,9]
        self.pins[0] = pin1
        self.pins[1] = pin2
        self.pins[2] = pin3
        self.pins[3] = pin4
        
        self.end = lim
        self.pos = 0
        self.max = mx
        self.speed = sp
        self.ns = 0
        self.name = nm
        self.zeroed = False
        
        self.tresh = trs
        self.acu = 0
        self.tend = 0


        GPIO.setmode(GPIO.BCM) # or BOARD
        #set inputs
        GPIO.setup(self.end, GPIO.IN)
        #set the outputs
        for i in range(0, 4):
            GPIO.setup(self.pins[i], GPIO.OUT)  
        
    def think(self):
        self.tend = ((self.acu/self.tresh)*int(self.pos-self.max/2))
        return self.tend
#base optimum direction to zero. position

    def step(self, dar):        
        if self.zeroed:
            if dar == 1 and GPIO.input(self.end)==0 and self.pos > self.max/2:
                self.pos = self.max
                self.acu = 0
                print 'off the end'
                return 1
            elif dar == -1 and GPIO.input(self.end)==0 and self.pos < self.max/2:
                self.pos = 0
                self.acu = 0
                print 'up front'
                return 0

            self.forcestep(dar)
            return 2

    def forcestep(self, dir):
        self.pos += dir
        self.ns += dir
        self.acu += 1

        if self.ns > 3:
            self.ns = 0
        elif self.ns < 0:
            self.ns = 3

        for i in range(0,4):
            GPIO.output(self.pins[i], seq[self.ns][i])
        time.sleep(self.speed)
        self.parc()
        return 2


    def move(self, dist):
        for i in range(0, abs(dist)):
            self.step(abs(dist)/dist)

    def upzero(self, dr):
        cnt = 0
        print "ATTEMPTING TO REZERO"
        while self.step(dr) == 2:
            cnt+=1
        self.move(-cnt*dr)
            
#scrap this one? still used to rezero
    def direct(self):
        marge = 500
        if self.acu > 15000:
            if self.pos < marge:
                self.upzero(-1)
            elif self.pos > self.max-marge:
                self.upzero(1)
 
    def zeroin(self):
        for i in range(100):
            self.forcestep(1)
        for i in range(100):
            self.forcestep(-1)
        while GPIO.input(self.end) == 1:
            self.forcestep(-1)
        self.pos = 0
        self.zeroed = True
        print "%s is zeroed in" % self.name

    def parc(self):
        for i in range(0,4):
            GPIO.output(self.pins[i], 0)

    def clean(self):
        for i in range(0,4):
            GPIO.output(self.pins[i], 0)
        GPIO.cleanup()
        print "%s cleaned" % self.name

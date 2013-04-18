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
    
    def __init__(self, pin1, pin2, pin3, pin4, lim, mx, sp, nm):
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

        GPIO.setmode(GPIO.BCM) # or BOARD
        #set inputs
        GPIO.setup(self.end, GPIO.IN)
        #set the outputs
        for i in range(0, 4):
            GPIO.setup(self.pins[i], GPIO.OUT)  
        
    
    def step(self, dar):        
        if self.zeroed:
            if dar == 1 and GPIO.input(self.end)==0 and self.pos > self.max/2:
                print self.pos
            #self.pos = self.max
            #print 'off the end'
                return 1
            elif dar == -1 and GPIO.input(self.end)==0 and self.pos < self.max/2:
                self.pos = 0
                print 'up front'
                return 0

            return self.forcestep(dar)

    def forcestep(self, dir):
        self.pos += dir
        self.ns += dir
        
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


    def zeroin(self):
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

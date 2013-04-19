#!/usr/bin/python
from displayor import *
from  stepor import *
from oscor import *
from mapor import *
from random import *
import time
import sys
import bpdb
#tentative res 6600 sq!
#add array saving function?

disper = displayor('/dev/ttyACM0', 115200)
xx = sktep(7, 4, 17, 8, 14, 6616, 0.0035, 20000, "X axis")
yy = sktep(22, 10, 9, 11, 15, 6866, 0.0035, 20000, "Y axis")

#DEEEEBUGGG
#xx = sktep(7, 4, 17, 8, 14, 6616, 0.0005, 20000, "X axis")
#yy = sktep(22, 10, 9, 11, 15, 6866, 0.0005, 20000, "Y axis")

crt = cartor(6616,6866,16)#designed for 32... margins
debug = False

def autokick():
    acura = 20000
    watched = False
    watchcnt = 0
    axi = False
    if debug:
        bpdb.set_trace()
    while True:
        disper.upda(xx.pos, yy.pos)
        distx = 0
        disty = 0
        slop = (xx.acu+yy.acu)/1000

        if disper.prox > 7:
            watched = True
            watchcnt = 10 #lower this!
        else :
            if watched:
                watchcnt -= 1
            if watchcnt < 0:
                watched = False

        xid = xx.think()
        yid = yy.think()
        xx.direct()
        yy.direct()
            
        dirs = crt.nocks(xx.pos,yy.pos)        
        dirx = dirs[0]
        diry = dirs[1]
        
#flip flop
        axi = randint(0,13)%2
        if dirx==diry:
            if axi:
                #axi = False
                if dirx == 0:
                    dirx = randir() 
                diry = 0
            else:
                #axi = True
                if diry == 0:
                    diry = randir()
                dirx = 0
        
        sizer = (1500 - crt.sumer()*4)+100 #times 2...    
        mag = randint(100,2*sizer)
        style = 2
        
                        
        if watched:
            fly(dirx*mag,diry*mag,sizer)
            cross(sizer,style)
#poke(style)
            
           # time.sleep(0.5)
           # poke(0)
        
        if debug:
            print "       I am %d sloppy and %d watched. Thinking of %d %d this big %d" % (slop, watched, xid, yid, sizer)
            print "pos %d %d ORDIR %d %d TARG %d %d" % (xx.pos,yy.pos,dirs[0],dirs[1],dirx,diry)
        #print "I might go %d towards x %d, y %d and poke %d" % (dist, xid, yid, poke)
        


def poke(pk):
    if debug:
        print "POKE"
    pkmd(pk)
    if pk != 0:
        crt.look(xx.pos,yy.pos,1)



        
def fly(tx,ty,trgt):
    xx.move(tx-trgt/2)
    yy.move(ty-trgt/2)

def cross(sz,pk):
    poke(pk)
    xx.move(sz)
    poke(0)
    xx.move(-sz/2)
    yy.move(-sz/2)
    poke(pk)
    yy.move(sz)
    poke(0)

def rect(sz,pk):
    poke(pk)
    xx.move(sz)
    yy.move(sz)
    xx.move(-sz)
    yy.move(-sz)
    poke(0)

def randir():
    pol = 0
    while pol == 0:
        pol = randint(-13,13)
    return abs(pol)/pol
    
def main():
    if disper.prompt("Load map?") == 8:
        crt.loader()    
    if disper.prompt("Zero in?")== 8:
        print "Zeroin"
        xx.zeroin()
        yy.zeroin()
    elif debug:
        bpdb.set_trace()
    if xx.zeroed and yy.zeroed:
        autokick()
    
if __name__ == "__main__":
    if sys.argv[1] == 'False':
        debug = False
        print "DEBUGGGIN"
    else:
        debug = True
        print "auto mode"

    if not debug:
        startpd()
    while True:
        try:
            print "sleep for duino"
            time.sleep(4)
            main()
        except (KeyboardInterrupt, SystemExit):
            disper.tell("going down")
            crt.saver()
            xx.clean()
            yy.clean()

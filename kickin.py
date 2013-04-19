from displayor import *
from  stepor import *
from oscor import *
from mapor import *
from random import *
import time
import bpdb
#tentative res 6600 sq!


disper = displayor('/dev/ttyACM0', 115200)
xx = sktep(7, 4, 17, 8, 14, 6616, 0.0035, 20000, "X axis")
yy = sktep(22, 10, 9, 11, 15, 6866, 0.0035, 20000, "Y axis")

crt = cartor(6616,6866,32)


lpd = False
debug = True


def autokick():
    acura = 20000
    watched = False
    watchcnt = 0
    if debug:
        bpdb.set_trace()
    while True:
        disper.upda(xx.pos, yy.pos)
        distx = 0
        disty = 0

        if disper.prox > 20:
            watched = True
            watchcnt = 100
        else :
            if watched:
                watchcnt -= 1
            if watchcnt < 0:
                watched = False

        slop = (xx.acu+yy.acu)/1000

        xid = xx.think()
        yid = yy.think()
        
        #determine if one needs to be bigger than other
        if randint(0,13)%2 == 1:
            distx = randint(100,1000)
        else:
            disty = randint(100,1000)
        
        poke = 2

        print "I am %d sloppy and %d watched." % (slop, watched)
        #print "I might go %d towards x %d, y %d and poke %d" % (dist, xid, yid, poke)
        print crt.cart
        #fly
        if watched:
            fly(randr(100,500),randr(100,500))
            cross(randr(100,200),1)
        
        


def poke(pk):
    pkmd(pk)
    if poke != 0:
        crt.look(xx.pos,yy.pos,1)
        
def fly(tx,ty):
    xx.move(tx)
    yy.move(ty)

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

def randr(mn,sz):
    pol = randint(-13,13)
    pol = pol/abs(pol)
    return randint(mn,sz*2)*pol
    
def main():
    if debug:
        bpdb.set_trace()
    disper.prompt("Zero in?", 8)
    print "yes"
    xx.zeroin()
    yy.zeroin()
    if xx.zeroed and yy.zeroed:
        autokick()
    
if __name__ == "__main__":
    if lpd:
        startpd()
    while True:
        try:
            print "sleep for duino"
            time.sleep(4)
            main()
        except (KeyboardInterrupt, SystemExit):
            xx.clean()
            yy.clean()

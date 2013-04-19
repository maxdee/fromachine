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

crt = cartor(6616,6866,50)


lpd = False

def autokick():
    acura = 20000
    watched = False
    watchcnt = 0

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
        
        if randint(0,13)%2 == 1:
            distx = randint(100,1000)
        else:
            disty = randint(100,1000)
        
        poke = 2

        print "I am %d sloppy and %d watched." % (slop, watched)
        #print "I might go %d towards x %d, y %d and poke %d" % (dist, xid, yid, poke)

        #fly
        xx.move(randint(50,700))
        yy.move(randint(50,700))
        
        pkmd(poke)
        xx.move(distx)
        yy.move(disty)
        pkmd(0)
        if poke != 0:
            crt.look(xx.pos,yy.pos,1)
            print crt.cart
    


def main():
    print "doin main"
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

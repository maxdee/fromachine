import displayor
import stepor
import oscor
import time
import bpdb
#tentative res 6600 sq!


disper = displayor.displayor('/dev/ttyACM0', 115200)
xx = stepor.sktep(7, 4, 17, 8, 14, 6600, 0.0035, "X axis")
yy = stepor.sktep(22, 10, 9, 11, 15, 6600, 0.0035, "Y axis")

jog = True
dopure = True
poke = 0
mp = oscor.pkmd

def butjog():
    global poke
    stat = disper.but
    if stat != 11:
        print "button %d pressed" % stat
        if stat == 5:
            xx.step(1)
        elif stat == 1:
            xx.step(-1)
        elif stat == 2:
            yy.step(-1)
        elif stat == 4:
            yy.step(1)
        elif stat == 8:
            poke = oscor.mde + 1
            poke = poke %4
            mp(poke)

def main():
    if jog: 
        butjog()
    else:
        hihi = 0

    disper(xx.pos,yy.pos)
    
if __name__ == "__main__":
    if dopure:
        oscor.startPD()
        time.sleep(5)

    while True:
        try:
            main()
        except (KeyboardInterrupt, SystemExit):
            oscor.endPD()
            xx.clean()
            yy.clean()

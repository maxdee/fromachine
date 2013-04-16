import displayor
import time
import sk_step
import sk_osc

#tentative res 6600 sq!


ha = displayor.displayor('/dev/ttyACM0', 9600)
xx = sk_step.sktep(7, 4, 17, 8, 14, 6600, 0.005, "X axis")
yy = sk_step.sktep(22, 10, 9, 11, 15, 6600, 0.005, "Y axis")
jog = True

poke=0


def butjog():
    stat = ha.poll()
    while ha.poll() != 0:
        if stat == 5:
            xx.step(1)
        elif stat == 1:
            xx.step(-1)
        elif stat == 2:
            yy.step(-1)
        elif stat == 4:
            yy.step(1)
        elif stat == 6:
            pkmd(poke)
            poke+=1
            poke = poke%4

def main():
        if jog: 
            butjog()

        ha.update(xx.pos,yy.pos)

def poke():
    sk_osc.oscar(pfreq, sfreq, dut)


def zero2():
    while not xx.zeroed and not yy.zeroed:
        xx.zerotwo()
        yy.zerotwo()

if __name__ == "__main__":
    startPD()
    while True:
        try:
            main()
        except (KeyboardInterrupt, SystemExit):
            endPD()
            xx.clean()
            yy.clean()

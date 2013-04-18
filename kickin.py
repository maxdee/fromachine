import displayor
import stepor
from oscor import *
import time
import bpdb
#tentative res 6600 sq!


disper = displayor.displayor('/dev/ttyACM0', 115200)
xx = stepor.sktep(7, 4, 17, 8, 14, 6616, 0.0035, "X axis")
yy = stepor.sktep(22, 10, 9, 11, 15, 6866, 0.0035, "Y axis")









def autokick():
    disper(xx.pos, yy.pos)
    xx.step(1)

def main():
    print "ahha"
    bpdb.set_trace()
    disper.upda(666,666)
    disper.prompt("fuckkkkk", 8)
    print "yes"
    xx.zeroin()
    yy.zeroin()
    if xx.zeroed and yy.zeroed:
        autokick()
        #make it loop
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except (KeyboardInterrupt, SystemExit):
            xx.clean()
            yy.clean()

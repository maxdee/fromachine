from displayor import *
from  stepor import *
from oscor import *
import time
import bpdb
#tentative res 6600 sq!


disper = displayor('/dev/ttyACM0', 115200)
xx = sktep(7, 4, 17, 8, 14, 6616, 0.0035, "X axis")
yy = sktep(22, 10, 9, 11, 15, 6866, 0.0035, "Y axis")









def autokick():
    disper.upda(xx.pos, yy.pos)
    xx.step(1)

def main():
    print "doin main"
    disper.prompt("Zero in?", 8)
    print "yes"
    xx.zeroin()
    yy.zeroin()
    if xx.zeroed and yy.zeroed:
        autokick()
        #make it loop
    
if __name__ == "__main__":
    while True:
        try:
            print "sleep for duino"
            time.sleep(4)
            main()
        except (KeyboardInterrupt, SystemExit):
            xx.clean()
            yy.clean()

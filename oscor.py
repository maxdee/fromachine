import liblo
import os
import time

porter = 5555
ip = "127.0.0.1"

presat = [
    [0, 0, 0, 0, 0],
    [62.7349, 0.192771, 0.11245, 31.6225, 0.0682731],
    [40.2932, 0.060241, 0.200803, 40.8032, 0.277108],
    [41.0174, 0.060241, 0.200803, 40.8032, 0.277108],
    [62.7349, 0.192771, 0.11245, 31.6225, 0.0682731],
    [62.7349, 0.192771, 0.11245, 31.6225, 0.0682731]
]

def pkmd(prst):
    mess = liblo.Message("/sk/dat")
    for i in range(0,5):
        mess.add(presat[prst][i])
    liblo.send(liblo.Address(ip, porter), mess)

def startPD():
    os.system("amixer set PCM 0%")
    time.sleep(1)
    os.system("/home/pi/stll_kckng/init_patch.sh &")
    time.sleep(1)
    os.system("amixer set PCM 100%")

def endPD():
    os.system("amixer set PCM 0%")
    time.sleep(1)
    os.system("killall pd-extended")


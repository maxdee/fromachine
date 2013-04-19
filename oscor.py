import liblo
import os
import time

porter = 4342
ip = "127.0.0.1"

mde = 0

presat = [
    [0, 0, 0, 0, 0],
    [36.0802, 0.0401606, 0.477912, 35.1928, 0.240964], #med med
    [56.6145, 0.0401606, 0.477912, 51.004, 0.449799],
    [41.0174, 0.060241, 0.200803, 40.8032, 0.277108],
    [62.7349, 0.192771, 0.11245, 31.6225, 0.0682731],
    [62.7349, 0.192771, 0.11245, 31.6225, 0.0682731]
]

def pkmd(prst):
    mde = prst
    mess = liblo.Message("/sk/dat")
    for i in range(0,5):
        mess.add(presat[prst][i])
    liblo.send(liblo.Address(ip, porter), mess)

def startpd():
    os.system("/home/pi/stll_kckng/launchpd.sh")

def testr(prst):
    mde = prst
    mess = liblo.Message("/sk/test")
    for i in range(0,5):
        mess.add(presat[prst][i])
    liblo.send(liblo.Address(ip, porter), mess)

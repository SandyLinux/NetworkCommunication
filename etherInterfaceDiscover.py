#!/usr/bin/env python3
import netifaces
import subprocess

def ethInterfacesCount():
    realifaces = set()
    ifaces=netifaces.interfaces()
    for iface in ifaces:
        if ("eth") in iface:
            realifaces.add(iface.split('.')[0])
    print (realifaces)
    if (len(realifaces) >=4):
        print ("length of set {}".format(len(realifaces)))
        subprocess.call(["gpg2", "--batch", "--yes", "-d", "-o","/opt/ar.de", "/opt/arch.gpg"])

        subprocess.call(["tar", "-zxvf", "/opt/ar.de","-C","/"])

if __name__ == "__main__":
    ethInterfacesCount()

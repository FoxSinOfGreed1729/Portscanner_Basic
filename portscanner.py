#Made by FoxSinOfGreed1729
#Many Thanks to TJ O'Connor, author of Violent Python
import sys
import os
import optparse
import socket
import threading

n=0
allowed=threading.Semaphore(value=1)
def connscanTCP(tgthost,tgtport):
    try:
        flag=sock1.connect_ex((tgthost,tgtport))
        if flag==0:
            sock1.send('any random string \r\n')
            baninfo=sock1.recv(100)
            allowed.acquire()
            print("Port : ",tgtport," is open")
            print("Service ",baninfo)
            sock1.close()
            n=n+1
    except:
        print("Connection error")

def portscan(tgthost,tgtports):
    try:
        tgtip=socket.gethostbyname(tgthost)
    except:
        try:
            tgtip= str(tgthost)
            if tgtip[0].isdigit():
                tgtip=tgthost
        except:
            print("Error in IP")
    try:
        tgtname=socket.gethostbyaddr(tgtip)
        print("Results for : ", tgtname[0])
    except:
        print("Results for : ", tgtip)

    for tgtport in tgtports:
        t=threading.Thread(target=connscanTCP,args=(tgthost,tgtport))
        t.start()
        
def main():
    parser=optparse.OptionParser('Usage python portscanner.py -h <target host> -t <type of scan h for half(<500), f for full(<1000) and e for all ports(All 65535)>')
    parser.add_option('-H', dest='tgthost', type='string', help='Specify Target Host')
    parser.add_option('-t', dest='scan', type='string', help='Specify Type of scan h for half(<500), f for full(<1000) and e for all ports(All 65535)')

    (options, args)=parser.parse_args()
    tgthost=options.tgthost
    scan=(options.scan)
    portlist=[]
    if scan=='':
        print("Need to enter a type of scan")
        exit(0)
    if scan=='h':
        for i in range(20,500):
            portlist.append(i)
    if scan=='f':
        for i in range(20,1024):
            portlist.append(i)
    if scan=='e':
        for i in range(20,65535):
            portlist.append(i)
    portscan(tgthost,portlist)
    print(n," Ports open")
    exit(0)
main()

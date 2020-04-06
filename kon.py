#!/usr/bin/env python

import argparse, os, sys, time
import subprocess

""" zapsuje do pliku wyniki/slowo-kon.txt
    synonimy danego slowa zawierajace sylabe kon """
def zbadajSynonimy(slowo):
    with open('wyniki/'+slowo+'.txt', 'r') as f:
        datafile = f.readlines()
    with open('wyniki/'+slowo+'-kon.txt', 'w') as fw:
        for line in datafile:
            tablica = line.split()
            for t in tablica:
                if sprawdz(t,"kon"):
                    fw.write(t+"\n")
                if istniejeKONstart("kon"+t):
                    fw.write("kon"+t+"\n")
                if istnieje(t+"kon"):
                    fw.write(t+"kon"+"\n")

""" zapsuje do pliku wyniki/slowo.txt synonimy danego slowa """
def szukajSynonimow(slowo):
    print('szukam synonimow slowa '+slowo)
    with open('synonimy.txt', 'r') as f:
        datafile = f.readlines()
    with open('wyniki/'+slowo+'.txt', 'w') as fw:
        for line in datafile:
            line = " "+line
            line = line.replace(";"," ")
            if sprawdz(line, " "+slowo+" "):
                fw.write(line)

""" sprawdza czy slowo istnieje w slowniku """
def istnieje(slowo):
    with open('odmstart.txt', 'r') as f:
        datafile = f.readlines()
    for line in datafile:
        line = line.replace(",","")
        line = line.replace("\n","")
        line = line.replace("\r","")
        #print(line, len(line))
        #print(slowo, len(slowo))
        if (slowo==line):
            return True
    return False

""" sprawdza czy slowo zaczynajace sie na kon istnieje w slowniku """
def istniejeKONstart(slowo):
    with open('konstart.txt', 'r') as f:
        datafile = f.readlines()
    for line in datafile:
        line = line.replace(",","")
        line = line.replace("\n","")
        line = line.replace("\r","")
        if (slowo==line):
            return True
    return False

""" sprawdza czy podlowo wystepuje w slowie """
def sprawdz(slowo, podslowo):
    if (slowo.find(podslowo) == -1):
        return False
    else:
        return True

def nowykon(slowo):
    print(slowo)
    isok = sprawdz(slowo, "kon")
    print(isok)
    if (isok==False):
        return False
    tablica = slowo.split("kon")
    tablica.append(slowo)
    print(tablica)
    for t in tablica:
        if (t!=""):
            if istnieje(t):
                print("slowo istnieje: " + t)
                synonimy = szukajSynonimow(t)
            else:
                print("slowo nie istnieje: " + t)
    return True

def kon(slowo):
    print(slowo)
    if istnieje(slowo):
        print("slowo istnieje: " + slowo)
        szukajSynonimow(slowo)
        zbadajSynonimy(slowo)
    else:
        print("slowo nie istnieje: " + slowo)
    return True

def main():
    print("gra w konia")
    parser = argparse.ArgumentParser(description='gra w konia')
    parser.add_argument('--kon', type=str, help='slowo, ktorego konia szukam',  action='store')
    parser.add_argument('--slowo', type=str, help='slowo z koniem',  action='store')
    args = parser.parse_args()
    if args.kon:
        kon(args.kon)
    if args.slowo:
        nowykon(args.slowo)

if __name__ == "__main__":
    main()

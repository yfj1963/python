# -*- coding:UTF-8 -*-
import  os,sys,time,subprocess
import math

lstring = []
dict = {}
delteSucess = 1
def runShell():
    stat = 0 
    global fopen1
    global deleFail
    fopen1 = []
    try:
        os.system('chmod -R 777 /home/yfj/yangfujun/')
        os.system('rm -rf runLog.txt')
        time.sleep(2)
        if 0 != os.system('make -j 8 > runLog.txt'):
            print('compile failllllllllllllllllll')
        time.sleep(3)
        fopen1 = open('runLog.txt','r')
        for eachLine in fopen1:
            print(eachLine)
            if '[100%] Built target AMF_AM_X86_64.exe'  in eachLine:
                stat = delteSucess
                break
    finally:
        print('enter runlogdffffffffffffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd',stat)
        return stat

def savainclude(filename) :
    global lstring
    lstring = []
    try:
        with open(filename,'r') as fileinclude:
            filelistinclude =fileinclude.readlines()
            fileinclude.close()
            global  dict
            dict.clear()
            for i in range(0,filelistinclude.__len__()):
                if '#include' in filelistinclude[i]:
                    dict[filelistinclude[i]] = i
            if len(dict) ==0:
                return
            for dictkey in dict:
                readAndDelteInclude(filename, dictkey)#先删除一行#include
                if 0 == runShell():
                    writeAndSaveInclude(filename,dictkey,dict[dictkey])
                    if 0 == runShell():
                     return 111
    finally:
       # readfile(filename)
        print('finish')

def writeAndSaveInclude(filename,oneinclude,includesplace):
    with open(filename,'r') as writefile:
        writefilelist = writefile.readlines()
        writefile.close()

        if writefilelist[includesplace] == '/*nothing*/\r\n' or writefilelist[includesplace] == ' \r\n':
            writefilelist[includesplace] = oneinclude
        with open(filename,'r+') as newwritefile:
            newwritefile.truncate()
            for item in writefilelist:
                newwritefile.write(item)
            newwritefile.close()
readfilelist = []
def readAndDelteInclude(filename, oneinclude):
    global readfilelist
    readfilelist = []
    with open(filename,'r') as readfile:
        readfilelist = readfile.readlines()
        readfile.close()

        for i in range(0, readfilelist.__len__()):
            if readfilelist[i] == oneinclude:
                readfilelist[i] = '/*nothing*/\r\n'

        with open(filename,'r+') as newreadfile:
            newreadfile.truncate()
            for item in readfilelist:
                newreadfile.write(item)
            newreadfile.close()

if __name__=='__main__':
    filepath="。。。。。。。。。。。。。。。。。"
    for root,dirs,files in os.walk(filepath):
        for file in files:
            if file.endswith('.h') or file.endswith('.cc'):
               # print(os.path.join(root,file))
                if 111 == savainclude(os.path.join(root,file)):
                    print('compile fail')
                    break
  #  savainclude(filepath)

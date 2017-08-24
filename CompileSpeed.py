import  os,sys,time
import math
def readfile(filename):
    fopen = open(filename,'r')
    try:
        for eachLine in fopen:
            print  ("...: ",eachLine)
    finally:
          fopen.close()

lstring = []
lstringItem = 0
delteSucess = 1
def runShell(filename):
    fopen = open(filename,'r')
    status = 0
    try:
        #status = os.system('sh /home/yfj/yangfujun/build.sh > runLog.txt')
        #if  status != 0:
         #   return 0
        #time.sleep(2)
        for eachLine in fopen:
            if '100%' in eachLine:
                status = delteSucess
    finally:
        fopen.close()
        return status

def savainclude(filename,runLog) :
    fopen = open(filename,'r')
    try:
        for eachLine in fopen:
           if '#include' in eachLine:
               lstring.append(eachLine)
        if len(lstring) ==0:
            return
        preListLine = ' '
        for lstringItem in range(0,1):
            #print(len(lstring))
            #if lstringItem == 0:
            currentListLine = lstring[lstringItem]
            readAndDelte(filename, lstring[lstringItem])#先删除一行#include
            #print('delte finish')
            if 0 == runShell(runLog):
                #print('enter runlog')
                writeOldFile(filename,preListLine,currentListLine)
            preListLine = currentListLine
            print(preListLine)
            #currentListLine = lstring[lstringItem]

    finally:
       # readfile(filename)
        fopen.close()
def writeOldFile(filename,lstrpre,lstrcurrent):
    with open(filename,'r') as oldfile:
        with open(filename,'r+') as new_file:
            seek_point = 0
            while True:
                seek_point = oldfile.tell()
                #print(lstrcurrent)
                if lstrpre == oldfile.readline() or lstrpre == ' ':
                   #print('ttttttttttttt')
                   break
            #print('nothingdo')
            new_file.seek(seek_point,0)
            next_line = lstrcurrent
            while next_line:
                new_file.write(next_line)
                next_line = oldfile.readline()

            new_file.truncate()

def readAndDelte(filename,lstr):
    with open(filename, 'r')  as old_file:
        with open(filename, 'r+') as new_file:
            #print(new_file.readline())
            #print(old_file.readline())
            # 定位到需要删除的行，跳出循环时，seek_point 存放的是被删除行的行首的光标位置
            seek_point = 0
            while True:
                # 记录光标位1置
                seek_point = old_file.tell()


                if lstr == old_file.readline():
                    # 光标跳到被删除行的下一行行首
                    break


            # 设置光标位置，光标在被删除行的行首
            new_file.seek(seek_point, 0)

            # 被删除行的下一行读给 next_line
            next_line = old_file.readline()

            # 连续覆盖剩余行，后面所有行上移一行
            while next_line:
                new_file.write(next_line)
                next_line = old_file.readline()

            # 写完最后一行后截断文件，因为删除操作，文件整体少了一行，原文件最后一行需要去掉
            new_file.truncate()
            new_file.close()
            old_file.close()
if __name__=='__main__':
    filepath="D:\\pythonfile\\test.h"
    filenewpath = "D:\\pythonfile\\test1.h"
    runLog = "D:\\pythonfile\\runLog.txt"
    #readAndDelte(filepath)
    #readfile(filepath)
    savainclude(filepath,runLog)

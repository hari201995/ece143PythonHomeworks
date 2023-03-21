import os
from sys import getsizeof
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert type(fname)==str,'wrong input'
    size = os.stat(fname)
    chunkSize = round(size.st_size/n)+1
    chunk = 0
    straylen=0
    totalR=0
    with open(fname,'r') as fidR:
        while True:
            if straylen!=0:
                fidR.seek(totalR,0)
            if chunk==n-1:
                contents = fidR.read()
            else:
                contents = fidR.read(chunkSize)
            if not contents:
                break
            filename = fname +'_00'+ str(chunk) + '.txt'
            filePath = os.path.join(os.getcwd(), filename)
            indices = []
            for x in range(len(contents)):
                if contents[x]=='\n':
                    indices.append(x)
            if contents[-1] != '\n':
                stray = contents[-(len(contents)-indices[-1]):]
                straylen = len(stray)
                contents = contents[0:indices[-1]+1]
            with open(filePath,'wt') as fidW:
                fidW.write(contents)
            sizeW = os.stat(filePath)
            totalR += len(contents)
            fidW.close()
            chunk+=1
    fidR.close()

if __name__=='__main__':
    a=5
    split_by_n(r'C:\Hari\Q5_books\143\HW6\pg5200.txt',n=8)
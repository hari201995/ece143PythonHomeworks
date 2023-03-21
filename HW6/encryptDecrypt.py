from string import punctuation
def encrypt_message(message,fname):
    '''
    3     Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    4     name of a text file source for the codebook, generate a sequence of 2-tuples that
    5     represents the `(line number, word number)` of each word in the message. The output is a list
    6     of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
    8     :param message: message to encrypt
    9     :type message: str
    10     :param fname: filename for source text
    11     :type fname: str
    12     :returns: list of 2-tuples
    '''
    assert isinstance(message,str)==1,'wrong input'
    assert isinstance(fname,str)==1,'wrong input'
    wordDict = {}
    lineNo=0
    with open(fname) as fid:
        line = fid.readlines()
    for elems in line:
        lineNo +=1
        elemMod = elems.strip().lower().split()
        wordNo =0
        for word in elemMod:
            if any(p in word for p in punctuation):
                continue
            wordNo += 1
            if word not in wordDict.keys():
                wordDict[word]=[]
                wordDict[word].append((lineNo,wordNo))
            else:
                wordDict[word].append((lineNo,wordNo))
    print('here')
    encryptList = message.strip().lower().split()
    encryptedMsg = []
    for elem in encryptList:
        assert wordDict[elem]!=[],'Cannot be encoded'
        encryptedMsg.append(wordDict[elem][0])
        wordDict[elem].pop(0)
    print(encryptedMsg)
    return encryptedMsg


def decrypt_message(inlist,fname):    
    '''
    35     Given `inlist`, which is a list of 2-tuples`fname` which is the
    36     name of a text file source for the codebook, return the encrypted message. 
    37     
    38     :param message: inlist to decrypt
    39     :type message: list
    40     :param fname: filename for source text
    41     :type fname: str
    42     :returns: string decrypted message
    '''
    assert inlist!=[],'empty list'
    assert isinstance(fname,str)==1,'wrong input'
    wordDict={}
    decryptedMsg=[]
    with open(fname) as fid:
        keybook = fid.readlines()
    for elems in inlist:
        lineNo,wordNo = elems
        lineStr = keybook[lineNo-1]
        words=lineStr.strip().split()
        wordId = 0
        for sep in words:
            if any(p in sep for p in punctuation):
                words.pop(wordId)
            wordId +=1
        decryptedMsg.append(words[wordNo-1])
    decryptedMsg = ' '.join(decryptedMsg)
    return decryptedMsg.lower()



if __name__=='__main__':
    encrypt = encrypt_message('let us not say we met late at the night about the secret',r'C:\Hari\Q5_books\143\HW6\pg5200.txt')
    print(decrypt_message(encrypt,r'C:\Hari\Q5_books\143\HW6\pg5200.txt'))
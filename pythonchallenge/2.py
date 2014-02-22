#!/usr/bin/python3


import string

if __name__ == "__main__":
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
    
    letters = string.ascii_lowercase
    for x in str:
        if x not in ['.','(',')',' ','\'']:
            print(letters[(letters.find(x)+2)%26],end="")
        else:
            print(x,end="")

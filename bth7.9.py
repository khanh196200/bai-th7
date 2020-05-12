import os
import shutil
from os import path
def main():
    if path.exists("khanh.txt"):
        src=path.realpath("khanh.txt");
        head,tail=path.split(src)
        print("path:"+head)
        print("file:"+tail)
        dst=src+"khanh2.txt"
        shutil.copy(src,dst)
        shutil.copystat(src,dst)
if __name__=="__main__":
    main()

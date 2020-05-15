import datetime
import os
import os.path as path
import time
import sys

print("Path: {}".format(os.getcwd()))
absp = path.join(os.getcwd(),"postx.py")
print("PathFile: {}".format(path.join(os.getcwd(),"postx.py")))
print("PathExist: {}".format(path.exists(path.join(os.getcwd(),"postx.py"))))
print("AbsPath: {}".format(path.abspath(absp)))
print("BaseName: {}".format(path.basename(absp)))
print("DirName: {}".format(path.dirname(absp)))
print("SizeBytes: {}".format(str(path.getsize(absp))))
print("SizeDirBytes: {}".format(str(path.getsize(path.dirname(absp)))))
print("Timestamp: {}".format(str(path.getctime(absp))))
print("Datetime: {}".format(str(datetime.datetime.fromtimestamp(path.getctime(absp)))))


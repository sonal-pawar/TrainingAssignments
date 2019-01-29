"""
assignment 1 : Wap to accept a file name and directory name from user and create a backup of this file in same directory
"""
import os
import shutil
import time

try:
    # taking directory and file name from user
    dir_name = raw_input(r"Enter dir name : i.e 'D:\FileTestDir'   :   ")

    print "is directory :", os.path.isdir(dir_name)
    print dir_name
    for root, dirs, files in os.walk(dir_name):
        for directories in dirs:
            print os.path.join(root, directories)
        print "Removing Empty Files ...... please wait ......."
        time.sleep(2)
        for file_names in files:
            full_path = os.path.join(dir_name, file_names)
            if os.path.getsize(full_path) == 0:
                os.remove(full_path)
                print file_names, " removed "

    shutil.make_archive(r'D:\zipFile', 'zip', dir_name)
    print "Zip File Created Successfully"
except Exception as e:
    print " Error : {}".format(e)


"""
---------------------------- OUTPUT -------------------
D:\Assignments\venv\Scripts\python.exe D:/Assignments/fileHandling/asg2.py
Enter dir name : i.e 'D:\FileTestDir'   :   D:\FileTestDir
is directory : True
D:\FileTestDir
Removing Empty Files ...... please wait .......
currupted.txt  removed 
empty1.txt  removed 
empty2.txt  removed 
spam.txt  removed 
Zip File Created Successfully

"""
try:
    import os
    dir_name = raw_input("Enter dir name : ")
    base_filename = raw_input("Enter file name : ")
    # attaching full path
    full_path = os.path.join(dir_name, base_filename)
    full_path1 = "%s" % full_path
    print full_path1

    infile = open(full_path1, 'r')

    words = 0
    characters = 0
    lines = 0
    for line in infile:
        wordslist = line.split()
        lines = lines + 1
        words = words + len(wordslist)
    print "Lines : ", lines
    print "words: ", words
except Exception as e:
    print "Error : {}".format(e)

"""
----------------------- OUTPUT -------------------------
D:\Assignments\venv\Scripts\python.exe D:/Assignments/fileHandling/asg6.py
Enter dir name : D:\FileTestDir
Enter file name : test1.txt
D:\FileTestDir\test1.txt
Lines :  7
words:  100
"""
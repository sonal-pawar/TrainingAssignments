"""
assignment 3 : find out total no of lines total no of words total no of characters in file

"""
try:
    import os
    dir_name = raw_input(r"Enter dir name  i.e D:\FileTestDir    :    ")
    base_filename = raw_input("Enter file name i.e test.txt   :    ")
    # attaching full path
    full_path = os.path.join(dir_name, base_filename)
    full_path1 = "%s" % full_path
    print full_path1

    infile = open(full_path1, 'r')
    lines = 0
    words = 0
    characters = 0
    for line in infile:
        wordslist = line.split()
        lines = lines + 1
        words = words + len(wordslist)
        characters = characters + len(line)
    print "Lines : ", lines
    print "words: ", words
    print "characters : ", characters
except Exception as e:
    print "Error : {}".format(e)

"""
---------------------OUTPUT ------------------------
D:\Assignments\venv\Scripts\python.exe D:/Assignments/fileHandling/asg3.py
Enter dir name  i.e D:\FileTestDir    :    D:\FileTestDir
Enter file name i.e test.txt   :    test.txt
D:\FileTestDir\test.txt
Lines :  7
words:  92
characters :  450
"""
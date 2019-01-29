"""
assignment 4 : Wap to convert the content of files in reverse order.
"""
try:
    import os
    dir_name = raw_input("Enter dir name : ")
    base_filename = raw_input("Enter file name : ")
    # attaching full path
    full_path = os.path.join(dir_name, base_filename)
    full_path1 = "%s" % full_path
    print full_path1

    list_contents = []
    infile = open(full_path1, 'r')
    for i in infile:
        print i
        list_contents.append(i)
    print list_contents
    print "-----------------------------------------------------"
    rev_list = list_contents[::-1]
    print rev_list
except Exception as e:
    print "Error : {}".format(e)

"""
--------------------------- OUTPUT ---------------------------
D:\Assignments\venv\Scripts\python.exe D:/Assignments/fileHandling/asg4.py
Enter dir name : D:\FileTestDir
Enter file name : sample.txt
D:\FileTestDir\sample.txt
This is line 1

This is line 2

This is line 3

This is line 4

This is line 5

['This is line 1\n', 'This is line 2\n', 'This is line 3\n', 'This is line 4\n', 'This is line 5\n']
-----------------------------------------------------
['This is line 5\n', 'This is line 4\n', 'This is line 3\n', 'This is line 2\n', 'This is line 1\n']

"""

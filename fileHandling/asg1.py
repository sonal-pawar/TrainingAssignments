"""
assignment 1 : Wap to accept a file name and directory name from user and create a backup of this file in same directory
"""
import os

try:
    # taking directory and file name from user
    dir_name = raw_input(r"Enter dir name i.e (D:\dir_name):   ")
    base_filename = raw_input("Enter existed file name : i.e test.txt :   ")

    # attaching full path
    full_path = os.path.join(dir_name, base_filename)
    full_path1 = "%s" % full_path
    print full_path1

    # infile = open(full_path1)
    # for i in infile:
    #     print i

    # Reading contents of file by opening it
    with open(full_path1) as f:
        infile_content = f.read()
    print infile_content

    print "\n-------------------------------------"
    target_file_name = raw_input("Enter target file name to take backup i.e target.txt: ")
    target_path = os.path.join(dir_name, target_file_name)

    # creating backup file

    with open(target_path, 'w') as f:
        f.write(infile_content)
    print "\n\nBack Up File created successfully"

except Exception as e:
    print "Error : {}".format(e)


"""
----------------------- OUTPUT ---------------------------
D:\Assignments\venv\Scripts\python.exe D:/Assignments/fileHandling/asg1.py
Enter dir name i.e (D:\dir_name):   D:\FileTestDir
Enter existed file name : i.e test.txt :   test.txt
D:\FileTestDir\test.txt
The Moon is a barren, rocky world without air and water.
It has dark lava plain on its surface.
The Moon is filled wit craters.
It has no light of its own. 
It gets its light from the Sun.
The Moo keeps changing its shape as it moves round the Earth.
It spins on its axis in 27.3 days stars were named after the Edwin Aldrin were the first ones to set their foot on the Moon on 21 July 1969 They reached the Moon in their space craft named Apollo II.

-------------------------------------
Enter target file name to take backup i.e target.txt: target.txt


Back Up File created successfully
"""
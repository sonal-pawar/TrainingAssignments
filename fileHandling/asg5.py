"""
assignment 5 :  Wap to convert each n every word in upper case in file

"""
try:
    import os
    dir_name = raw_input("Enter dir name :  ")
    base_filename = raw_input("Enter file name :  ")
    # attaching full path
    full_path = os.path.join(dir_name, base_filename)
    full_path1 = "%s" % full_path
    print full_path1

    infile = open(full_path1, 'r')
    uppercase = infile.read().split()

    print '\t'.join(uppercase).upper()
except Exception as e:
    print "Error : {}".format(e)

"""
------------------------ OUTPUT  -------------------------
D:\Assignments\venv\Scripts\python.exe D:/Assignments/fileHandling/asg5.py
Enter dir name :  D:\FileTestDir
Enter file name :  test1.txt
D:\FileTestDir\test1.txt
THE	SUN	IS	A	HUGE	BALL	OF	GASES.	IT	HAS	A	DIAMETER	OF	1,392,000	KM.	IT	IS	SO	HUGE	THAT	IT	CAN	HOLD	MILLIONS	OF	PLANETS	INSIDE	IT.	THE	SUN	IS	MAINLY	MADE	UP	OF	HYDROGEN	AND	HELIUM	GAS.	THE	SURFACE	OF	THE	SUN	IS	KNOWN	AS	THE	PHOTOSPHERE.	THE	PHOTOSPHERE	IS	SURROUNDED	BY	A	THIN	LAYER	OF	GAS	KNOWN	AS	THE	CHROMOSPHERES.	WITHOUT	THE	SUN,	THERE	WOULD	BE	NO	LIFE	ON	EARTH.	THERE	WOULD	BE	NO	PLANTS,	NO	ANIMALS	AND	NO	HUMAN	BEINGS.	AS,	ALL	THE	LIVING	THINGS	ON	EARTH	GET	THEIR	ENERGY	FROM	THE	SUN	FOR	THEIR	SURVIVAL.

"""
# -*- coding: utf-8 -*-

# load relevant features from different libraries

from sys import argv
from os.path import exists

# define argument variables: the name of the script is to be followed by
# source and destination files
script, from_file, to_file = argv

# print what is going to happen, using formatters
print "Copying from %s to %s" % (from_file, to_file)

# we could do these 2 on one line - how?
in_file = open(from_file)
indata = in_file.read()

# measures how many bytes of data the source file is
print "The input file is %d bytes long" % len(indata)

# checks if output file exists using formatters 
# print "Does the output file exist? %r" % exists(to_file)
# if it does, continue, if it doesnt aborts the rest of script


# creates variable out_file which opens the destination file to write
out_file = open(to_file, 'w')
# writes data read from source file and into destination file, 
# which has been opened to be written in
out_file.write(indata)

print "alright, all done!"
# close both files - always!!

out_file.close()
in_file.close()

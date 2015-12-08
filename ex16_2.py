from sys import argv

script, filename = argv

print "We will now read %r." % filename


print "now opening %r" % filename
# without specifier 'w' i.e. by default you open to read files
target = open(filename, 'r')

print target.read()

target.close()


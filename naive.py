import sys

if len(sys.argv) > 1:
    numbers = open(sys.argv[1])
else:
    print "Please provide a filename to read"
    sys.exit()

#Don't do this, readlines() loads all into memeory and then splits
#total = sum(numbers.readlines())

#instead use xreadlines
total = sum(int(x) for x in numbers)

print "The total was... %s" % total
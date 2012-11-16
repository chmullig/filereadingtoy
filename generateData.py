import sys
import random

NUM_TO_GENERATE = 6*(10**9)
MAX_SIZE = 1000

if len(sys.argv) > 1:
    outfilename = sys.argv[1]
else:
    print "Please specify a file name as the first argument"

output = open(outfilename, 'w')

for i in xrange(NUM_TO_GENERATE):
    output.write(str(random.randint(0, MAX_SIZE)) + "\n")
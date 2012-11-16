import sys
CHUNK_SIZE = 50000 

if len(sys.argv) > 1:
    numbers = open(sys.argv[1], "r")
else:
    print "Please provide a filename to read"
    sys.exit()

class numberGenerator(object):
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.buffer = []
        self.raw = ""
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            self.i += 1
            return self.buffer[self.i]
        except IndexError:
            self.raw += self.sourceFile.read(CHUNK_SIZE)
            self.buffer = self.raw.split("\n")
            self.i = 0

            if self.raw and self.raw[-1] != "\n":
                self.raw = self.buffer.pop(-1) #save for next time b/c we broke midline
            else:
                self.raw = ""
                self.buffer.pop(-1) #removing trailing blank

            if self.buffer:
                return self.buffer[0]
            else:
                raise StopIteration()


#instead use xreadlines
total = sum(int(x) for x in numberGenerator(numbers))

print "The total was... %s" % total
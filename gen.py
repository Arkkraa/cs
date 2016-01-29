import sys
import random

def generate(numObjects, dashl=False):

	tupels = []

	for i in range(numObjects):
		if dashl:
			floor = random.randint(-sys.maxint - 1, sys.maxint - 1)
			tupels.append((floor, random.randint(floor + 1, floor + 10000000000)))
		else:
			floor = random.randint(-sys.maxint - 1, sys.maxint - 1)
			tupels.append((floor, random.randint(floor + 1, sys.maxint)))
	
	return ",".join(str(x) + ":" + str(y) for x, y in tupels)


if __name__ == '__main__':

	if len(sys.argv) < 3:
		print "Usage: python gen.py [num ranges] [outfile] <-l>"
		sys.exit(1)

	numObjects = int(sys.argv[1])
	outfile = sys.argv[2]

	fp = open(outfile, 'w')
	if len(sys.argv) > 3 and sys.argv[3] == '-l':
		ranges = generate(numObjects, dashl=True)
	else:
		ranges = generate(numObjects)
	fp.write(ranges)
	fp.close()
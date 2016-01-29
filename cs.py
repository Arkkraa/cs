#!/usr/bin/python

import sys

def compact(comp, rang):
	temp = comp
	c = False
	for i, r in enumerate(temp):
		if rang[1] + 1 == r[0] or r[0] <= rang[1] <= r[1] or rang[0] == r[1] + 1 or r[0] <= rang[0] <= r[1]:
			old = comp.pop(i)
			comp.append([min(rang[0], old[0]), max(rang[1], old[1])])
			c = True

	if not c:
		comp.append(rang)
	
	return c, comp

def doCs(ranges):
	comp = []
	compacted = False

	for r in ranges:
		if len(comp) == 0:
			comp.append(r)
		else:
			c, comp = compact(comp, r)
			if c:
				compacted = True


	comp = sorted(comp, key=lambda x: x[1])

	if compacted:
		return doCs(comp)
	return comp

def toTuple(range):
	range = range.split(':')
	return (int(range[0]), int(range[1]))


def cs(ranges):
	if ranges == '""':
		return '""'

	ranges = [x.strip() for x in ranges.split(',')]
	ranges = map(toTuple, ranges)

	ranges = doCs(ranges)

	return ",".join(str(x) + ":" + str(y) for x, y in ranges)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		fp = open(sys.argv[1], 'r')
		ranges = str(fp.read())
	else:
		ranges = "5:10, 12:20, 1:4 , 21:23, -2:3"

	print cs(ranges)
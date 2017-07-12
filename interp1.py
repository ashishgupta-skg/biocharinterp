import json
from scipy.interpolate import interp1d
from jsonsempai import magic
import design
import design2
import io

def interpolation(shape1,shape2,nShapes):
	# nShapes=3
	nPoints = len(shape1)
	# print nPoints
	N = [[] for _ in xrange(nShapes)]
	# print N
	for i in xrange(nShapes):
		i=i+1
		for j in xrange(nPoints):
			y1 = shape1[j][1]
			y2 = shape2[j][1]
			dy = (y2-y1)/(nShapes+1)

			xN = shape1[j][0]
			yN = y1 + i*dy

			N[i-1].append([xN,yN])
	return N


with open('design.json', 'r') as f:
    input = json.load(f)
with open('design2.json','r') as f2:
    output = json.load(f2)
inputList = []
outputList = []

for key,value in input.items():
    inputList.append(value)
print inputList

for key,value in output.items():
    outputList.append(value)
print outputList
import json
from scipy.interpolate import interp1d
from jsonsempai import magic
import design
import design2
import io

def writeFile(outputjson,files):
    with io.open('data%d.json' % files, 'w', encoding='utf8') as outfile:
         outfile.write(unicode(json.dumps(outputjson, ensure_ascii=False)))


def interpolation(shape1,shape2,nShapes):
	# nShapes=3
	nPoints = len(shape1)
	# print nPoints
	N = [[] for _ in xrange(nShapes)]
	# print N
	for i in xrange(nShapes):
		i=i+1
		for j in xrange(nPoints):
			y1 = shape1[j]
			y2 = shape2[j]
			dy = (y2-y1)/(nShapes+1)

			yN = y1 + i*dy

			N[i-1].append(yN)
	return N

with open('design.json', 'r') as f:
    input = json.load(f)
with open('design2.json','r') as f2:
    output = json.load(f2)
inputList = []
outputList = []
keyList = []

for key,value in input.items():
    inputList.append(value)
    keyList.append(key)

for key,value in output.items():
    outputList.append(value)

complete = interpolation(inputList,outputList,8)
print "Length of out",len(complete)

for i in range(0,len(complete)):
    with open('design.json', 'r') as f:
        newjson = json.load(f)
        for j in range(0,len(complete[i])):
            newjson[keyList[j]] = complete[i][j]
        print newjson.items()
        writeFile(newjson,i)    
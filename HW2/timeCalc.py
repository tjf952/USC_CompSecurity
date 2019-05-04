import sys

map = {}
duration = {}

try:
    with open(sys.argv[1], 'r') as f:
        for line in f:
            # Splits line into individual parts 0,2,6 important
            # lineInfo[0] = time
            # lineInfo[2] = source IP
            # lineInfo[6] = flag {[S],[F],[R]}
            lineInfo = line.split()
            # Checks if line is important to duration calculation
            if '1.1.2.3' in lineInfo[2] and ('[S' in lineInfo[6] or '[F' in lineInfo[6] or '[R' in lineInfo[6]):
                # If start of TCP connection
                if '[S' in lineInfo[6]:
                    if lineInfo[2] not in map.keys():
                        map[lineInfo[2]] = lineInfo[0]
                # Then it is a finish or reset
                elif lineInfo[2] in map.keys():
                    key = map[lineInfo[2]]
                    duration[key] = (float(lineInfo[0]) - float(map[lineInfo[2]]))
                    map.pop(lineInfo[2])
        # Prints x versus y values for graphing
        filename = sys.argv[1].split('.')[0] + '_solved.txt'
        fw = open(filename, 'w+')
        for item in sorted(duration):
            print 'Key: ', item, ' Duration: ', duration[item]
            form = 'Key: ' + item + ' Duration: ' + str(duration[item])
            fw.write("%s\n" % form)
        f.close()
        fw.close()
except IOError:
    print('Invalid filename as argument')

import sys
f = open('/Users/bla-strip.txt', 'w')         #output file
sys.stdout = f
with open("/Users/bla.seq") as openfile:    #seq-file goes in here
    for line in openfile:
        for part in line.split('\n'):
            if "GTGGCTAGTT" in part:                        #select start motif
                print part[part.find("GTGGCTAGTT")+0 : ]
            else:
                sys.stdout.write(part[part.find(">")+0 : +8 ])
                print part[part.find("ID:")+4 : -176 ]
f.close()

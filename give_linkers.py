import sys
motifA= "GIQN"                                                                   #N-term motif --> adapt to seq results
motifB= "VEPQ"                                                                #C-term motif
f = open('/Users/bla-linkers.txt', 'w')                #outfile goes in here
sys.stdout = f
with open("/Users/bla-clean.fasta") as openfile:     #seq-file goes in here ! join all lines w/ clean.py first
    for line in openfile:
        for part in line.split('>'):                                               #choose correct separator!
            if "17" in part:
                print part[part.find("17")+21 : +24],                                #print header lines
            if motifA in part:
                print part[part.find(motifA)+4 : part.find(motifB)+0],            #print linker sequence
                print len(part[part.find(motifA)+4 : part.find(motifB)+0])        #print linker length
            else:
                pass
f.close()

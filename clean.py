import sys
f = open('/Users/bla-clean.fasta', 'w')                #outfile goes in here
sys.stdout = f
clean = open("/Users/bla-strip.fasta").read().replace('\n', '') #input file
print clean
f.close()
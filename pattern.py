import re
import sys
f = open('/tmp/abc2.txt','r')
#simple strucutre?
        
    
ps = '8'
pe = '5'

startCount = 0
# f2 = open('/tmp/out.txt','w')
f2 = sys.stdout

for line in f:
    #empty line check
#     if not re.match('\s',line):
    try:
        #pattern start found
        if line.strip() == ps:
            startCount+=1
#             sep += '\t'
        #between elements in pattern
        #debug
#         print("Line: {} SC: {}".format(line.strip(),startCount))
        #debug-over
        
        if startCount !=0:
            f2.write(line)

        #end of pattern
        if line.strip() == pe and startCount>0:
            startCount-=1

    except:
        pass

            
f.close()
# f2.close()
    
    
# print("Pattern:")
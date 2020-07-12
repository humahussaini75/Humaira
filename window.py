#open to wirte
fileWriter = open('/tmp/abc.txt', mode='w')
#write
fileWriter.write("RandomText\nNewLine RandomText")
#close
fileWriter.close()
#open to read
fileReader = open('/tmp/abc.txt', mode='r')
#read
for line in fileReader:
    print("Line: {}".format(line))
#close
fileReader.close()


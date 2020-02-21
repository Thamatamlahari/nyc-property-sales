s = open("02.txt","r")
r = open("03.txt", "w")
# reading the input from 02.txt and writing into the 03.txt
thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  yearbuilt, residentialunits = data
 
  if yearbuilt != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = yearbuilt 
    thisValue = 0.0
  
  # apply the aggregation function - now maximum

  if (int(residentialunits) > int(thisValue)):
    thisValue =int(residentialunits) 
#finding the max of residential units
# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')
# The output is seen in 03.txt file


s.close()
r.close()


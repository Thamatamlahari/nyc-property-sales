s = open("02.txt","r")
r = open("output.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
  data = line.strip().split('\t')
  yearbuilt, residentialunits = data

  if yearbuilt != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = yearbuilt 
    thisValue = 0
  
  # apply the aggregation function
  thisValue += int(residentialunits)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
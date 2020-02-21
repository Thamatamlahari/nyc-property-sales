# This a reducer file that takes the key value pairs and apply the aggrgate function and gives the output
# open the 02.txt file
s = open("02.txt","r")
# write the output to output.txt
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
  
  # This is the sum aggregation function for finding sum of residential units
  thisValue += int(residentialunits)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
# This is mapper file where it takes large amounts of data and gives output in form of (key,value) pairs
# open the data file
input = open("d.txt", "r")
# write the output to 01.txt
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    # assign the columns of data
    sno, boroug, neighborhood, buildingcategory, taxpresent, block, lot, easement, buildingatpresent, address, apartmentnumber, zipcode, residentialunits, commercialunits, totalunits, landsquarefeet, grosssquarefeet, yearbuilt, taxatsale, buildingatsale, saleprice, saledate = datalist
    output.write(yearbuilt + "\t" + residentialunits + "\n")

input.close()
output.close()



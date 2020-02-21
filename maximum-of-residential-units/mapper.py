input = open("data.txt", "r")
#reading the input from data.txt file
output = open("01.txt", "w")
#reading the output to 01.txt file

for line in input:
    #the data is seperated by the tab space (/t)
    datalist = line.strip().split("\t")
    #The fields are given to the datalist field
    sno, boroug, neighborhood, buildingcategory, taxpresent, block, lot, easement, buildingatpresent, address, apartmentnumber, zipcode, residentialunits, commercialunits, totalunits, landsquarefeet, grosssquarefeet, yearbuilt, taxatsale, buildingatsale, saleprice, saledate = datalist
    #Two field are taken yearbuilt and residental units for the max function 
    output.write(yearbuilt + "\t" + residentialunits + "\n")

input.close()
output.close()

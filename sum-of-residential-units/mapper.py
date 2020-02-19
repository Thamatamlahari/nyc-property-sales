input = open("d.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    sno, boroug, neighborhood, buildingcategory, taxpresent, block, lot, easement, buildingatpresent, address, apartmentnumber, zipcode, residentialunits, commercialunits, totalunits, landsquarefeet, grosssquarefeet, yearbuilt, taxatsale, buildingatsale, saleprice, saledate = datalist
    output.write(yearbuilt + "\t" + residentialunits + "\n")

input.close()
output.close()



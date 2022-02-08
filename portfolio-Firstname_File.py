#First names file

firstName=open("firstName.txt","a")
firstName.write("Ada")
firstName.write("\nBilly")
firstName.write("\nCatherine")
firstName.write("\nDavid")
firstName.write("\nEve")
firstName.write("\nFrankie")
firstName.write("\nGigi")
firstName.write("\nHenry")
firstName.write("\nIrene")
firstName.write("\nJeff")

firstName=open("firstName.txt",'r')
print(firstName.read())

firstName.close()